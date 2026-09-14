import pymupdf
import re, json
from collections import defaultdict

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_答案解析.pdf'
doc = pymupdf.open(pdf_path)

all_answers = {}

for page_idx in range(len(doc)):
    page = doc[page_idx]
    blocks = page.get_text("dict")["blocks"]

    current_key = None
    current_text_parts = []

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
                    all_answers[current_key] = '\n'.join(current_text_parts)

                year = q_match.group(1)
                is_supplement = q_match.group(2) is not None
                qnum = int(q_match.group(3))
                year_key = year + ('补' if is_supplement else '')
                current_key = (year_key, qnum)
                current_text_parts = []

                # 去掉题号标记后的内容
                remaining = re.sub(r'【\d{4}\s*(补)?\s*-\d+】', '', line_text).strip()
                if remaining:
                    current_text_parts.append(remaining)
            elif current_key:
                current_text_parts.append(line_text)

    # 页面结束时保存当前题
    if current_key and current_text_parts:
        all_answers[current_key] = '\n'.join(current_text_parts)
        current_key = None
        current_text_parts = []

doc.close()

print(f"提取答案解析总数: {len(all_answers)}")

# 按年份统计
year_counts = defaultdict(int)
for (year, qnum) in all_answers.keys():
    year_counts[year] += 1

print(f"\n按年份分布:")
for y, c in sorted(year_counts.items()):
    print(f"  {y}: {c}题")

# 转换为列表并保存
result = []
for (year, qnum), text in sorted(all_answers.items()):
    # 提取答案
    answer_match = re.search(r'答案[:：]\s*([A-D])', text)
    answer = answer_match.group(1) if answer_match else ''

    # 提取解析（去掉答案和考点分析）
    analysis = text
    analysis = re.sub(r'答案[:：]\s*[A-D]\s*', '', analysis)
    analysis = re.sub(r'【考点分析】.*?【解析】', '', analysis, flags=re.DOTALL)
    analysis = re.sub(r'【解析】', '', analysis)
    analysis = analysis.strip()

    result.append({
        'year': year,
        'qnum': qnum,
        'answer': answer,
        'analysis': analysis,
        'raw_text': text
    })

with open(r'D:\应用程序开发\刷题\exam-quiz\pub_answers_full.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"\n已保存到 pub_answers_full.json")

# 显示2014-9题的答案
print(f"\n2014-9题答案:")
for item in result:
    if item['year'] == '2014' and item['qnum'] == 9:
        print(f"  answer: {item['answer']}")
        print(f"  analysis: {item['analysis'][:100]}")
        break
