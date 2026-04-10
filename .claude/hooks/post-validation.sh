#!/usr/bin/env bash
# AiTechBlog Post Validation Hook
# Triggered on Write/Edit — checks only _posts/ and _drafts/ files

set -uo pipefail

# Read tool input from stdin
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('tool_name',''))" 2>/dev/null || echo "")
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); inp=d.get('tool_input',{}); print(inp.get('file_path', inp.get('path','')))" 2>/dev/null || echo "")

# Only apply to _posts/ or _drafts/ markdown files
if [[ "$FILE_PATH" != *"/_posts/"* ]] && [[ "$FILE_PATH" != *"/_drafts/"* ]]; then
  exit 0
fi
if [[ "$FILE_PATH" != *.md ]]; then
  exit 0
fi

# File must exist to validate
if [[ ! -f "$FILE_PATH" ]]; then
  exit 0
fi

ERRORS=()
WARNINGS=()

# --- Extract front matter fields ---
TITLE=$(grep -m1 '^title:' "$FILE_PATH" 2>/dev/null | sed 's/^title:[[:space:]]*//' | tr -d '"' || echo "")
DESCRIPTION=$(grep -m1 '^description:' "$FILE_PATH" 2>/dev/null | sed 's/^description:[[:space:]]*//' | tr -d '"' || echo "")
DATA_UPDATED=$(grep -m1 '^data_updated:' "$FILE_PATH" 2>/dev/null | sed 's/^data_updated:[[:space:]]*//' || echo "")
FORMAT_TYPE=$(grep -m1 '^format_type:' "$FILE_PATH" 2>/dev/null | sed 's/^format_type:[[:space:]]*//' || echo "")

# ==========================================================
# SECTION A: SEO / Front Matter Rules
# ==========================================================

# --- Rule A1: Title length (<= 60 chars) ---
if [[ -n "$TITLE" ]]; then
  TITLE_LEN=${#TITLE}
  if (( TITLE_LEN > 60 )); then
    ERRORS+=("TITLE TOO LONG: ${TITLE_LEN} chars (max 60) — \"${TITLE}\"")
  fi
fi

# --- Rule A2: Title must contain "2026" ---
if [[ -n "$TITLE" ]] && [[ "$TITLE" != *"2026"* ]]; then
  ERRORS+=("TITLE MISSING YEAR: '2026' must appear in title — \"${TITLE}\"")
fi

# --- Rule A3: Meta description length (140-165 chars) ---
if [[ -n "$DESCRIPTION" ]]; then
  DESC_LEN=${#DESCRIPTION}
  if (( DESC_LEN < 140 )); then
    ERRORS+=("DESCRIPTION TOO SHORT: ${DESC_LEN} chars (min 140) — \"${DESCRIPTION:0:60}...\"")
  elif (( DESC_LEN > 165 )); then
    ERRORS+=("DESCRIPTION TOO LONG: ${DESC_LEN} chars (max 165) — \"${DESCRIPTION:0:60}...\"")
  fi
fi

# --- Rule A4: Must have a comparison table (JSON blocks now forbidden — see Rule B1) ---
HAS_TABLE=0; grep -qE '^\|.+\|.+\|' "$FILE_PATH" 2>/dev/null && HAS_TABLE=1 || true
if (( HAS_TABLE == 0 )); then
  ERRORS+=("MISSING STRUCTURED DATA: Post must include a comparison table (|col|col|)")
fi

# --- Rule A5: Word count >= 600 (excluding code/data blocks) ---
WORD_COUNT=$(python3 - "$FILE_PATH" <<'PYEOF' 2>/dev/null || echo 0
import re, sys
try:
    content = open(sys.argv[1], encoding='utf-8').read()
    content = re.sub(r'^---.*?---', '', content, flags=re.DOTALL)
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    content = re.sub(r'<[^>]+>', '', content)
    print(len(content.split()))
except Exception:
    print(0)
PYEOF
)
WORD_COUNT=$(echo "$WORD_COUNT" | tr -d '[:space:]\r')
WORD_COUNT=${WORD_COUNT:-0}
if ! [[ "$WORD_COUNT" =~ ^[0-9]+$ ]]; then WORD_COUNT=0; fi
if (( WORD_COUNT < 600 )); then
  ERRORS+=("WORD COUNT TOO LOW: ${WORD_COUNT} words (min 600, excluding code blocks)")
fi

# --- Rule A6: FAQ section (>= 3 question headings) ---
FAQ_COUNT=0
while IFS= read -r line; do
  if [[ "$line" =~ ^#{1,4}\ (How|What|Why|When|Is|Are|Can|Does|Should|Which|Where|Who) ]] || [[ "$line" =~ ^#{1,4}\ .*\?$ ]]; then
    (( FAQ_COUNT++ )) || true
  fi
done < "$FILE_PATH"
if (( FAQ_COUNT < 3 )); then
  WARNINGS+=("FAQ WEAK: Only ${FAQ_COUNT} question heading(s) found (recommend >= 3 for People Also Ask)")
fi

# --- Rule A7: TL;DR section ---
HAS_TLDR=0; grep -qE 'TL;DR|tl;dr|TLDR' "$FILE_PATH" 2>/dev/null && HAS_TLDR=1 || true
if (( HAS_TLDR == 0 )); then
  WARNINGS+=("MISSING TL;DR: Add a TL;DR section with 3-5 bullets for Featured Snippet targeting")
fi

# --- Rule A8: data_updated field present ---
if [[ -z "$DATA_UPDATED" ]]; then
  ERRORS+=("MISSING data_updated: front matter must include 'data_updated: YYYY-MM-DD'")
fi

# --- Rule A9: Internal links (>= 2 recommended) ---
INTERNAL_LINKS=0
while IFS= read -r line; do
  if [[ "$line" =~ \]\(/posts/ ]]; then
    (( INTERNAL_LINKS++ )) || true
  fi
done < "$FILE_PATH"
if (( INTERNAL_LINKS < 2 )); then
  WARNINGS+=("FEW INTERNAL LINKS: ${INTERNAL_LINKS} found (recommend 2-3 within same topic cluster)")
fi

# ==========================================================
# SECTION B: Content Quality Rules (Python)
# ==========================================================

PY_RESULTS=$(python3 - "$FILE_PATH" <<'PYEOF' 2>/dev/null || echo ""
import re, sys

try:
    content = open(sys.argv[1], encoding='utf-8').read()
except Exception as e:
    sys.exit(0)

errors = []
warnings = []

# --- Rule B1: JSON 코드 블록 금지 ---
if re.search(r'```json', content):
    errors.append("JSON CODE BLOCK FOUND: Convert to a markdown table or prose (```json blocks are forbidden)")

# --- Rule B2: 코드 블록 앞에 설명 없음 ---
triggered_b2 = False
for m in re.finditer(r'(.*)\n```', content):
    prev = m.group(1).strip()
    if not triggered_b2 and (prev.startswith('#') or prev == ''):
        errors.append("CODE BLOCK MISSING INTRO: Add 1-2 sentences before the code block explaining what it does")
        triggered_b2 = True

# --- Rule B3: 코드 블록 뒤에 설명 없음 ---
triggered_b3 = False
for m in re.finditer(r'```\n(.*)', content):
    next_line = m.group(1).strip()
    if not triggered_b3 and (next_line.startswith('#') or next_line == ''):
        errors.append("CODE BLOCK MISSING OUTRO: Add at least one sentence after the code block highlighting the key point")
        triggered_b3 = True

# --- Rule B4: 소제목 바로 아래 코드 블록 ---
if re.search(r'#{1,6} .+\n+```', content):
    errors.append("HEADING DIRECTLY BEFORE CODE: Insert an explanatory paragraph between the heading and code block")

# --- Rule B5: Risk landscape vs checklist coverage ---
risk_items = re.findall(r'"name":\s*"(.+?)"', content)
checklist_items = re.findall(r'\*\*LLM\d+', content)
if len(risk_items) > 0 and len(checklist_items) < len(risk_items):
    errors.append(
        f"CHECKLIST COVERAGE GAP: Risk landscape has {len(risk_items)} items "
        f"but checklist covers only {len(checklist_items)} — add the missing entries"
    )

# --- Rule B6: FAQ "미해결 문제" + 확정적 코드 블록 불일치 ---
has_open_problem_faq = bool(re.search(
    r'(open|unsolved|remains|no.*solution|not.*solved)', content, re.IGNORECASE
))
has_definitive_code = bool(re.search(r'```python', content))
if has_open_problem_faq and has_definitive_code:
    warnings.append(
        "FAQ/CODE MISMATCH: FAQ implies an open problem but post contains definitive Python code — "
        "add caveats or limitations to the code block"
    )

# --- Rule B7: 소제목 대비 섹션 내용 너무 적음 ---
sections = re.split(r'^#{2,3} .+$', content, flags=re.MULTILINE)
short_sections = []
for i, section in enumerate(sections[1:], 1):
    lines = [l for l in section.strip().split('\n') if l.strip()]
    if len(lines) < 3:
        short_sections.append(str(i))
if short_sections:
    warnings.append(
        f"THIN SECTIONS: Section(s) {', '.join(short_sections)} have fewer than 3 lines — "
        "add more content or merge with adjacent section"
    )

for e in errors:
    print(f"ERROR:{e}")
for w in warnings:
    print(f"WARN:{w}")
PYEOF
)

# Parse Python output into ERRORS/WARNINGS arrays
while IFS= read -r line; do
  [[ -z "$line" ]] && continue
  if [[ "$line" == ERROR:* ]]; then
    ERRORS+=("${line#ERROR:}")
  elif [[ "$line" == WARN:* ]]; then
    WARNINGS+=("${line#WARN:}")
  fi
done <<< "$PY_RESULTS"

# ==========================================================
# OUTPUT
# ==========================================================

BASENAME=$(basename "$FILE_PATH")

if (( ${#ERRORS[@]} > 0 )); then
  echo ""
  echo "=========================================="
  echo "  POST VALIDATION FAILED: $BASENAME"
  echo "=========================================="
  for err in "${ERRORS[@]}"; do
    echo "  [ERROR] $err"
  done
  if (( ${#WARNINGS[@]} > 0 )); then
    echo ""
    for warn in "${WARNINGS[@]}"; do
      echo "  [WARN]  $warn"
    done
  fi
  echo "=========================================="
  echo "  Fix all errors before publishing."
  echo "=========================================="
  echo ""
  exit 0
fi

if (( ${#WARNINGS[@]} > 0 )); then
  echo ""
  echo "  POST VALIDATION PASSED (with warnings): $BASENAME"
  for warn in "${WARNINGS[@]}"; do
    echo "  [WARN] $warn"
  done
  echo ""
fi

exit 0
