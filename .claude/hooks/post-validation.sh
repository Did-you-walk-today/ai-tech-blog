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
# 줄 수가 아니라 단어 수로 잰다. 마크다운 문단은 몇 문장이든 한 줄이라
# 줄 수로 재면 잘 쓴 FAQ 답변이 걸리고 337단어짜리 벽글이 통과한다.
# FAQ 답변(H3)과 구조적 섹션은 짧은 게 정상이므로 제외한다.
STRUCTURAL = ('faq', 'frequently asked', 'changelog', 'update cadence',
              'related resources', 'related posts', 'sources', 'references', 'tl;dr')

parts = re.split(r'^(#{2,3} .+)$', content, flags=re.MULTILINE)
sections = []          # (heading_text, level, body)
for i in range(1, len(parts), 2):
    h = parts[i].strip()
    level = len(h) - len(h.lstrip('#'))
    sections.append((h.lstrip('# ').strip(), level, parts[i + 1]))

in_faq = False
thin = []
dense = []
for idx, (title, level, sec) in enumerate(sections):
    low = title.lower()
    if level == 2:
        in_faq = ('faq' in low) or ('frequently asked' in low)
    # FAQ 하위 답변은 한 문단이 정상 — 제외
    if in_faq and level == 3:
        continue
    if any(k in low for k in STRUCTURAL):
        continue
    # 하위 소제목만 담는 컨테이너 제목은 본문이 없는 게 정상 — 제외
    nxt = sections[idx + 1] if idx + 1 < len(sections) else None
    if nxt and nxt[1] > level and not sec.strip():
        continue

    prose = re.sub(r'```.*?```', '', sec, flags=re.DOTALL)
    prose = re.sub(r'^\|.*$', '', prose, flags=re.MULTILINE)   # 표 제외
    prose = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', prose)         # 이미지 제외
    words = len(prose.split())
    paras = [p for p in re.split(r'\n\s*\n', prose.strip()) if p.strip()]

    has_table = bool(re.search(r'^\|', sec, flags=re.MULTILINE))
    if words < 40 and not has_table:
        thin.append(f"'{title}' ({words}w)")

    # B8: 벽글 — 개별 문단이 120단어를 넘으면 화면에서 통짜 블록이 된다.
    # 이 블로그 실측 분포(문단 426개)에서 중앙값 53w, 95분위 112w.
    for p in paras:
        n = len(p.split())
        if n > 120 and not p.lstrip().startswith(('-', '*', '>', '|')):
            dense.append(f"'{title}' ({n}w 문단)")

if thin:
    warnings.append(
        f"THIN SECTIONS: {', '.join(thin)} — under 40 words of prose. "
        "Expand or merge into the adjacent section"
    )
if dense:
    warnings.append(
        f"WALL OF TEXT: {', '.join(dense)} — single paragraph over 120 words "
        "(this blog's median is 53). Split it, or break out a sub-heading"
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
# SECTION C: Post Images (C1~C8 — see IMAGE_GUIDE.md)
# ==========================================================
# Delegated to image_validation.py, which emits the same ERROR:/WARN: protocol.
# It downgrades ERROR to WARN for _drafts/ on its own — artwork arrives late.

HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$HOOK_DIR/image_validation.py" ]]; then
  IMG_RESULTS=$(python3 "$HOOK_DIR/image_validation.py" "$FILE_PATH" 2>/dev/null || echo "")
  while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    if [[ "$line" == ERROR:* ]]; then
      ERRORS+=("${line#ERROR:}")
    elif [[ "$line" == WARN:* ]]; then
      WARNINGS+=("${line#WARN:}")
    fi
  done <<< "$IMG_RESULTS"
fi

# ==========================================================
# SECTION D: GEO / Citation Evidence (D1~D5 — see SEO_GUIDE.md §11-§13)
# ==========================================================
# Delegated to geo_validation.py, which emits the same ERROR:/WARN: protocol.
# It downgrades ERROR to WARN for _drafts/ on its own — a draft legitimately
# predates its data file and its source links.

if [[ -f "$HOOK_DIR/geo_validation.py" ]]; then
  GEO_RESULTS=$(python3 "$HOOK_DIR/geo_validation.py" "$FILE_PATH" 2>/dev/null || echo "")
  while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    if [[ "$line" == ERROR:* ]]; then
      ERRORS+=("${line#ERROR:}")
    elif [[ "$line" == WARN:* ]]; then
      WARNINGS+=("${line#WARN:}")
    fi
  done <<< "$GEO_RESULTS"
fi

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
