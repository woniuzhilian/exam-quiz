import pymupdf
import re, json

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_题目.pdf'
doc = pymupdf.open(pdf_path)

# 从PDF提取所有题目：题号 + 题干 + 选项
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

        # 查找题目开始标记 【YYYY-NN】
        q_match = re.search(r'【(\d{4})-(\d+)】', text)
        if q_match:
            # 保存上一题
            if current_q:
                all_questions.append(current_q)
            # 开始新题
            year = q_match.group(1)
            qnum = int(q_match.group(2))
            # 去掉题号标记后的题干
            question_text = re.sub(r'【\d{4}-\d+】', '', text).strip()
            current_q = {
                'year': year,
                'qnum': qnum,
                'question': question_text,
                'options': {'A': '', 'B': '', 'C': '', 'D': ''},
                'page': page_idx + 1,
                'y0': y0
            }
        elif current_q:
            # 追加到当前题
            # 检查是否是选项
            opt_match = re.match(r'[（(][A-D][）)]\s*(.*)', text)
            if opt_match:
                opt_letter = opt_match.group(0)[1]  # A/B/C/D
                opt_content = opt_match.group(1)
                # 可能一行有多个选项
                # 简单处理：整行作为该选项内容
                current_q['options'][opt_letter] = opt_content
            else:
                # 追加到题干
                current_q['question'] += ' ' + text

    if current_q:
        all_questions.append(current_q)

doc.close()

print(f"从PDF提取题目总数: {len(all_questions)}")

# 按年份+题号排序
all_questions.sort(key=lambda x: (x['year'], x['qnum']))

# 统计每年题数
from collections import Counter
year_counts = Counter(q['year'] for q in all_questions)
print(f"\n按年份分布:")
for y, c in sorted(year_counts.items()):
    print(f"  {y}: {c}题")

# 保存提取结果
with open(r'D:\应用程序开发\刷题\exam-quiz\pdf_questions_raw.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"\n已保存到 pdf_questions_raw.json")

# 显示前5题
print(f"\n前5题:")
for q in all_questions[:5]:
    print(f"  {q['year']}-{q['qnum']}: {q['question'][:60]}")
