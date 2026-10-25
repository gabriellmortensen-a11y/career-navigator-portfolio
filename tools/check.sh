#!/usr/bin/env bash
# Every publication check, in order. Run before any release or push.
#
#   tools/check.sh
#
# Optional environment:
#   MMDC=/path/to/mmdc          render-check the Mermaid diagrams
#   PRIVATE_TERMS=/outside.txt  denylist of private terms (kept outside the repo)
#   APP_SRC=/path/to/app        check the career-evidence file with the app's reader
set -uo pipefail
cd "$(dirname "$0")/.."
status=0
echo "== links";             python3 tools/check_links.py .   || status=1
echo "== sensitive content"; python3 tools/scan_sensitive.py . || status=1
echo "== career-evidence import"; python3 tools/check_import.py || status=1
echo "== mermaid"
if [[ -n "${MMDC:-}" ]] || command -v mmdc >/dev/null; then
  tools/check_mermaid.sh || status=1
else
  echo "skipped: mermaid-cli not available (set MMDC)"
fi
echo "== empty files"
empty=$(find . -path ./.git -prune -o -type f -empty -print)
if [[ -n "$empty" ]]; then echo "$empty"; status=1; else echo "none"; fi
exit $status
