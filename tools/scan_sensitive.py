#!/usr/bin/env python3
"""Scan the portfolio for content that must not be published.

Checks every text file in the repository for:

* credentials: API-key shapes (OpenAI, Anthropic, Tavily, Apify, Voyage,
  GitHub, AWS, Slack), private-key blocks, bearer tokens, passwords in
  URLs, and `KEY=value` assignments;
* personal contact data: email addresses (except the allow-list below),
  phone numbers, IPv4 addresses;
* infrastructure that is not public: SSH targets, server paths, database
  URLs, environment files;
* unfinished work: TODO, TBD, FIXME, lorem ipsum, unanswered placeholders;
* an optional private denylist: one term per line in a file named by the
  PRIVATE_TERMS environment variable. That file lives OUTSIDE the
  repository, because the terms it holds (names of people, employers in
  the owner's job search, record text) are the very thing being kept out.

Usage: PRIVATE_TERMS=/path/outside/repo.txt python3 tools/scan_sensitive.py
Exit status 1 when anything is found.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ALLOWED_EMAILS = {"noreply@anthropic.com"}

PATTERNS = {
    "openai/anthropic-style key": r"\bsk-(?:ant-|proj-)?[A-Za-z0-9_-]{16,}",
    "tavily key": r"\btvly-[A-Za-z0-9]{10,}",
    "apify token": r"\bapify_api_[A-Za-z0-9]{10,}",
    "voyage key": r"\bpa-[A-Za-z0-9_-]{20,}",
    "github token": r"\bgh[pousr]_[A-Za-z0-9]{20,}",
    "aws access key": r"\bAKIA[0-9A-Z]{16}\b",
    "slack token": r"\bxox[abprs]-[A-Za-z0-9-]{10,}",
    "private key block": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "bearer token": r"(?i)\bbearer\s+[A-Za-z0-9._-]{20,}",
    "password in url": r"[a-z]+://[^\s/:@]+:[^\s/@]+@",
    "secret assignment": r"(?i)\b[A-Z0-9_]*(?:API_KEY|SECRET|TOKEN|PASSWORD)\s*=\s*[^\s<`'\"]{6,}",
    "ipv4 address": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "phone number": r"(?<![\d.])(?:\+1[ .-]?)?\(?\d{3}\)?[ .-]\d{3}[ .-]\d{4}\b",
    "ssh target": r"\b[a-z_][a-z0-9_-]*@[a-z0-9.-]+:\S*|\bssh\s+[a-z_]+@",
    "server path": r"/srv/|/home/[a-z]+/|~/\.config/",
    "database url": r"postgres(?:ql)?(?:\+\w+)?://",
    "environment file": r"(?<![\w/])\.env\b(?!\.example)",
    "connections export": r"(?i)connections\.csv",
    "unfinished": r"\b(?:TODO|TBD|FIXME|XXX)\b|(?i:lorem ipsum)|\[NEEDS[ _]",
}
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
TEXT_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".csv", ".mmd",
                 ".svg", ".py", ".sh", ".html"}
#: The scanners themselves name the patterns they look for.
SKIP = {"tools/scan_sensitive.py"}


def private_terms() -> list[str]:
    path = os.environ.get("PRIVATE_TERMS")
    if not path:
        return []
    terms = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            terms.append(line)
    return terms


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    compiled = {name: re.compile(p) for name, p in PATTERNS.items()}
    terms = [(t, re.compile(r"(?i)(?<!\w)" + re.escape(t) + r"(?!\w)"))
             for t in private_terms()]
    findings: list[str] = []
    files = 0
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = str(path.relative_to(root))
        if rel in SKIP or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        files += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        is_svg = path.suffix.lower() == ".svg"
        for number, line in enumerate(text.splitlines(), 1):
            where = f"{rel}:{number}"
            for name, pattern in compiled.items():
                if is_svg and name in ("ipv4 address", "phone number"):
                    continue  # coordinates and version strings in SVG
                if pattern.search(line):
                    findings.append(f"{where}: {name}")
            for email in EMAIL.findall(line):
                if email.lower() not in ALLOWED_EMAILS and not is_svg:
                    findings.append(f"{where}: email address")
            for term, pattern in terms:
                if pattern.search(line):
                    findings.append(f"{where}: private term (denylist)")
    print(f"files scanned: {files}; private terms: {len(terms)}; "
          f"findings: {len(findings)}")
    for line in findings:
        print("  FOUND", line)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
