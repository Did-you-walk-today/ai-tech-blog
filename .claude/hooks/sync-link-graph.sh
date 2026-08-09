#!/usr/bin/env bash
# AiTechBlog — Internal Link Graph Sync Hook
#
# Keeps LINK_GRAPH.md in sync with _posts/.
# The graph is derived from post bodies, never hand-maintained, so the index
# document can never drift away from the actual links.
#
# Triggers (see .claude/settings.json) — same gating as sync-indexing-list.sh:
#   - Write/Edit to _posts/*.md   (a post's links may have changed)
#   - Bash commands touching _posts/ or git mv/commit/push  (publish-post skill)

set -uo pipefail

INPUT=$(cat)

TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_name',''))" 2>/dev/null || echo "")

case "$TOOL_NAME" in
  Write|Edit)
    FILE_PATH=$(echo "$INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); i=d.get('tool_input',{}); print(i.get('file_path', i.get('path','')))" 2>/dev/null || echo "")
    [[ "$FILE_PATH" == *"/_posts/"*.md ]] || exit 0
    ;;
  Bash)
    CMD=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('command',''))" 2>/dev/null || echo "")
    if ! echo "$CMD" | grep -qE '_posts|git[[:space:]]+(mv|commit|push|rm)'; then
      exit 0
    fi
    ;;
  *)
    exit 0
    ;;
esac

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || echo "")
[[ -n "$REPO_ROOT" ]] || exit 0
[[ -d "$REPO_ROOT/_posts" ]] || exit 0

python3 "$REPO_ROOT/.claude/hooks/link_graph.py" "$REPO_ROOT"

# Taxonomy conformance — an undeclared cluster or category, or a hub tab that has
# drifted from _data/taxonomy.yml. Reported alongside the graph because both are
# repo-level structure rather than per-post content.
TAX=$(python3 "$REPO_ROOT/.claude/hooks/taxonomy_validation.py" --report "$REPO_ROOT" 2>/dev/null || true)
TAX_ERRORS=$(printf '%s\n' "$TAX" | grep '^\[ERROR' || true)
if [[ -n "$TAX_ERRORS" ]]; then
  echo "분류 체계 ERROR — _data/taxonomy.yml 과 어긋납니다:" >&2
  printf '%s\n' "$TAX_ERRORS" >&2
fi

# Surface DANGLING links (broken internal links) loudly — that is the one finding
# that blocks publishing. Warnings stay in the document rather than the console.
#
# --report exits 1 when it finds an ERROR. Under `set -o pipefail` that non-zero
# would become the status of a `... | grep` pipeline and invert the test, so the
# report is captured first and matched separately.
REPORT=$(python3 "$REPO_ROOT/.claude/hooks/link_graph.py" --report 2>/dev/null || true)
ERROR_LINES=$(printf '%s\n' "$REPORT" | grep '^\[ERROR' || true)

if [[ -n "$ERROR_LINES" ]]; then
  echo "링크 그래프 ERROR — 존재하지 않는 슬러그로 연결된 내부 링크가 있습니다:" >&2
  printf '%s\n' "$ERROR_LINES" >&2
  echo "LINK_GRAPH.md 2번 섹션에서 전체 목록을 확인하십시오." >&2
fi

# Either class blocks publishing.
[[ -n "$ERROR_LINES" || -n "$TAX_ERRORS" ]] && exit 2
exit 0
