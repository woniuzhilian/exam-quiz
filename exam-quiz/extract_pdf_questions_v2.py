import pymupdf
import re, json
from collections import defaultdict

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_题目.pdf'
doc = pymupdf.open(pdf_path)

all_questions = []

for page_idx in range(len(doc)):
    page = doc[page_idx]
    blocks = page.get_text("blocks")

    current_q = None
    for b in blocks:
        x0, y0, x1, y1, text, block_no, block_type = b
        text = text.strip()
        if not text:
            continue

        # 匹配所有题目编号格式：【YYYY-NN】、【YYYY 补-NN】、【YYYY补-NN】
        q_match = re.search(r'【(\d{4})\s*(补)?\s*-(\d+)】', text)
        if q_match:
            if current_q:
                all_questions.append(current_q)
            year = q_match.group(1)
            is_supplement = q_match.group(2) is not None
            qnum = int(q_match.group(3))
            year_key = year + ('补' if is_supplement else '')
            question_text = re.sub(r'【\d{4}\s*(补)?\s*-\d+】', '', text).strip()
            current_q = {
                'year': year_key,
                'qnum': qnum,
                'question': question_text,
                'options': {'A': '', 'B': '', 'C': '', 'D': ''},
                'page': page_idx + 1,
                'y0': y0
            }
        elif current_q:
            opt_match = re.match(r'[（(][A-D][）)]\s*(.*)', text)
            if opt_match:
                opt_letter = opt_match.group(0)[1]
                opt_content = opt_match.group(1)
                current_q['options'][opt_letter] = opt_content
            else:
                current_q['question'] += ' ' + text

    if current_q:
        all_questions.append(current_q)

doc.close()

print(f"从PDF提取题目总数: {len(all_questions)}")

year_counts = defaultdict(int)
for q in all_questions:
    year_counts[q['year']] += 1

print(f"\n按年份分布:")
for y, c in sorted(year_counts.items()):
    print(f"  {y}: {c}题")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pdf_questions_raw.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"\n已保存到 pdf_questions_raw.json")
