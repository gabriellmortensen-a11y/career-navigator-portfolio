#!/usr/bin/env bash
# Render every ```mermaid block in the portfolio with mermaid-cli, so a
# diagram with a syntax error is caught before GitHub shows it as an error
# box. Optionally writes the SVGs to assets/diagrams/ (--export).
#
# Needs mermaid-cli: set MMDC to its path, or have `mmdc` on PATH
# (npx @mermaid-js/mermaid-cli works too).
#
# Usage: tools/check_mermaid.sh [--export]
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
mmdc="${MMDC:-$(command -v mmdc || true)}"
if [[ -z "$mmdc" ]]; then
  echo "mermaid-cli not found: set MMDC=/path/to/mmdc" >&2
  exit 2
fi
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
export_dir=""
[[ "${1:-}" == "--export" ]] && export_dir="$root/assets/diagrams"

python3 - "$root" "$work" <<'PY'
import re, sys
from pathlib import Path
root, work = Path(sys.argv[1]), Path(sys.argv[2])
count = 0
for md in sorted(root.rglob("*.md")):
    if ".git" in md.parts:
        continue
    text = md.read_text(encoding="utf-8")
    for index, block in enumerate(
            re.findall(r"```mermaid\n(.*?)```", text, re.S), 1):
        name = f"{md.relative_to(root).with_suffix('')}".replace("/", "__")
        (work / f"{name}__{index}.mmd").write_text(block, encoding="utf-8")
        count += 1
print(f"mermaid blocks found: {count}")
PY

failed=0
for file in "$work"/*.mmd; do
  [[ -e "$file" ]] || continue
  out="${file%.mmd}.svg"
  if ! "$mmdc" -q -i "$file" -o "$out" >"$file.log" 2>&1; then
    echo "FAILED $(basename "$file")"; sed 's/^/    /' "$file.log" | head -20
    failed=$((failed + 1))
  elif [[ -n "$export_dir" ]]; then
    cp "$out" "$export_dir/$(basename "$out")"
  fi
done
total=$(ls "$work"/*.mmd 2>/dev/null | wc -l)
echo "mermaid blocks rendered: $((total - failed)) of $total"
[[ $failed -eq 0 ]]
