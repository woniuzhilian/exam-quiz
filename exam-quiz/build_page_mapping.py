import pymupdf
import json
import os
import re

# 路径
question_pdf = r'D:\证件相关\一级岩土工程师\公共基础分类版真题详解（13~24）_题目.pdf'
analysis_pdf = r'D:\证件相关\一级岩土工程师\公共基础分类版真题详解（13~24）_答案解析.pdf'
output_dir = r'D:\应用程序开发\刷题\exam-quiz\question_images'

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 只处理公共基础题目
public_questions = [q for q in questions if q['bigSubject'] == '公共基础']
print(f"公共基础题目数: {len(public_questions)}")

# 建立题号到页面的映射
print("正在建立题目PDF的题号到页面映射...")
doc_q = pymupdf.open(question_pdf)
question_page_map = {}

for i, page in enumerate(doc_q):
    text = page.get_text()
    # 查找所有【YYYY-NN】标记
    matches = re.findall(r'【(\d{4})-(\d+)】', text)
    for year, qnum in matches:
        key = f"{year}-{qnum}"
        if key not in question_page_map:
            question_page_map[key] = i + 1  # 页码从1开始

doc_q.close()
print(f"题目PDF映射完成，共 {len(question_page_map)} 个题号")

# 建立答案解析PDF的题号到页面的映射
print("正在建立答案解析PDF的题号到页面映射...")
doc_a = pymupdf.open(analysis_pdf)
analysis_page_map = {}

for i, page in enumerate(doc_a):
    text = page.get_text()
    # 查找所有【YYYY-NN】标记
    matches = re.findall(r'【(\d{4})-(\d+)】', text)
    for year, qnum in matches:
        key = f"{year}-{qnum}"
        if key not in analysis_page_map:
            analysis_page_map[key] = i + 1

doc_a.close()
print(f"答案解析PDF映射完成，共 {len(analysis_page_map)} 个题号")

# 保存映射
with open(os.path.join(output_dir, 'page_mapping.json'), 'w', encoding='utf-8') as f:
    json.dump({
        'question': question_page_map,
        'analysis': analysis_page_map
    }, f, ensure_ascii=False, indent=2)

print("映射已保存到 page_mapping.json")

# 统计有多少题目可以找到
found_q = 0
found_a = 0
for q in public_questions:
    key = f"{q['year']}-{q.get('yearQnum')}"
    if key in question_page_map:
        found_q += 1
    if key in analysis_page_map:
        found_a += 1

print(f"题目PDF中找到: {found_q}/{len(public_questions)}")
print(f"答案解析PDF中找到: {found_a}/{len(public_questions)}")
