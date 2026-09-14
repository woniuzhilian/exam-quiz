import pymupdf
import re, json

pdf_path = r'D:\证件相关\一级岩土工程师\真题空白卷\岩土专业基础历年真题试题册（2024版）.pdf'
doc = pymupdf.open(pdf_path)

# 提取所有题目
all_questions = []
current_year = None
current_q = None

for page_idx in range(len(doc)):
    page = doc[page_idx]
    text = page.get_text()

    # 查找年份标记
    year_match = re.search(r'(\d{4})\s*年注册岩土专业基础真题', text)
    if year_match:
        current_year = year_match.group(1)
        print(f"找到年份: {current_year} (第{page_idx+1}页)")

    if not current_year:
        continue

    # 按行处理
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 查找题目开始：数字+、
        q_match = re.match(r'^(\d+)[、.]\s*(.*)', line)
        if q_match:
            # 保存上一题
            if current_q:
                all_questions.append(current_q)
            qnum = int(q_match.group(1))
            question_text = q_match.group(2)
            current_q = {
                'year': current_year,
                'qnum': qnum,
                'question': question_text,
                'options': {'A': '', 'B': '', 'C': '', 'D': ''}
            }
        elif current_q:
            # 查找选项
            opt_match = re.match(r'[（(]([A-D])[）)]\s*(.*)', line)
            if opt_match:
                opt_letter = opt_match.group(1)
                opt_content = opt_match.group(2)
                current_q['options'][opt_letter] = opt_content
            else:
                # 追加到题干
                current_q['question'] += ' ' + line

    if current_q:
        all_questions.append(current_q)
        current_q = None

doc.close()

print(f"\n提取题目总数: {len(all_questions)}")

# 按年份统计
from collections import Counter
year_counts = Counter(q['year'] for q in all_questions)
print(f"按年份分布:")
for y, c in sorted(year_counts.items()):
    print(f"  {y}: {c}题")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\prof_blank_questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"\n已保存到 prof_blank_questions.json")
