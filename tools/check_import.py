#!/usr/bin/env python3
"""Check the career-evidence file reads the way Career Navigator will read it.

Loads Career Navigator's own résumé reader (`app/evidence/resume_reading.py`,
pure Python, no database, no model) straight from a checkout of the
application, and runs it on `career-evidence/career-navigator-learnings.txt`.
Passes when the file reads as exactly one role, every line under that role
is a bullet, nothing is left unplaced, and the role's employer and title are
the ones the file declares.

Usage: APP_SRC=/path/to/career-evidence python3 tools/check_import.py
Skipped (exit 0, with a note) when APP_SRC is not set.
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

EXPECTED_EMPLOYER = "Career Navigator (Independent)"
EXPECTED_TITLE = "Founder / Product Leader"


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    source = os.environ.get("APP_SRC")
    if not source:
        print("import check skipped: set APP_SRC to a Career Navigator "
              "checkout to run it")
        return 0
    reader_path = Path(source) / "app" / "evidence" / "resume_reading.py"
    spec = importlib.util.spec_from_file_location("resume_reading",
                                                  reader_path)
    reader = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reader)

    target = root / "career-evidence" / "career-navigator-learnings.txt"
    data = target.read_bytes()
    held = reader.text_of(data, target.name)
    if held.get("failure"):
        print("FAILED to read:", held["failure"])
        return 1
    parsed = reader.parse(held["text"])
    roles = parsed.get("roles") or []
    problems = []
    if len(roles) != 1:
        problems.append(f"expected 1 role, read {len(roles)}")
    for role in roles:
        if role.get("employer") != EXPECTED_EMPLOYER:
            problems.append(f"employer read as {role.get('employer')!r}")
        if role.get("title") != EXPECTED_TITLE:
            problems.append(f"title read as {role.get('title')!r}")
    if parsed.get("unplaced"):
        problems.append(f"{len(parsed['unplaced'])} unplaced lines")
    bullets = [b for r in roles for b in (r.get("bullets") or [])]
    written = [line for line in held["text"].splitlines()
               if line.startswith("- ")]
    if len(bullets) != len(written):
        problems.append(f"{len(written)} bullet lines in the file, "
                        f"{len(bullets)} read as bullets")
    words = [len(b.split()) for b in bullets]
    print(f"roles: {len(roles)}; bullets read: {len(bullets)}; words per "
          f"bullet: {min(words, default=0)}–{max(words, default=0)}; "
          f"start: {roles[0].get('start') if roles else None}")
    for problem in problems:
        print("  PROBLEM", problem)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
