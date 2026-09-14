import pymupdf
import re, json
from collections import defaultdict

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_题目.pdf'
doc = pymupdf.open(pdf_path)

all_questions = {}

for page_idx in range(len(doc)):
    page = doc[page_idx]
    # 使用dict模式获取更详细的文本信息
    blocks = page.get_text("dict")["blocks"]

    current_key = None
    current_text_parts = []
    current_opt = None

    for block in blocks:
        if "lines" not in block:
            continue
        for line in block["lines"]:
            line_text = ""
            for span in line["spans"]:
                line_text += span["text"]
            line_text = line_text.strip()
            if not line_text:
                continue

            # 查找题目开始标记 【YYYY-NN】或【YYYY 补-NN】
            q_match = re.search(r'【(\d{4})\s*(补)?\s*-(\d+)】', line_text)
            if q_match:
                # 保存上一题
                if current_key and current_text_parts:
                    all_questions[current_key] = '\n'.join(current_text_parts)

                year = q_match.group(1)
                is_supplement = q_match.group(2) is not None
                qnum = int(q_match.group(3))
                year_key = year + ('补' if is_supplement else '')
                current_key = (year_key, qnum)
                current_text_parts = []
                current_opt = None

                # 去掉题号标记后的内容
                remaining = re.sub(r'【\d{4}\s*(补)?\s*-\d+】', '', line_text).strip()
                if remaining:
                    current_text_parts.append(remaining)
            elif current_key:
                current_text_parts.append(line_text)

    # 页面结束时保存当前题
    if current_key and current_text_parts:
        all_questions[current_key] = '\n'.join(current_text_parts)
        current_key = None
        current_text_parts = []

doc.close()

print(f"提取题目总数: {len(all_questions)}")

# 按年份统计
year_counts = defaultdict(int)
for (year, qnum) in all_questions.keys():
    year_counts[year] += 1

print(f"\n按年份分布:")
for y, c in sorted(year_counts.items()):
    print(f"  {y}: {c}题")

# 转换为列表并保存
result = []
for (year, qnum), text in sorted(all_questions.items()):
    result.append({
        'year': year,
        'qnum': qnum,
        'text': text
    })

with open(r'D:\应用程序开发\刷题\exam-quiz\pub_questions_full.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"\n已保存到 pub_questions_full.json")

# 显示2014年第9题
print(f"\n2014-9题内容:")
for item in result:
    if item['year'] == '2014' and item['qnum'] == 9:
        print(f"  {item['text'][:200]}")
        break
