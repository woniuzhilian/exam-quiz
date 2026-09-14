import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 筛选专业基础
pro = [q for q in questions if q['bigSubject'] == '专业基础']

# 查看有问题的题目
problem_questions = [
    ('2017', 40),
    ('2018', 19),
    ('2020', 16),
    ('2024', 26),
]

print("=== 空字段题目详情 ===")
for year, qnum in problem_questions:
    q = next((x for x in pro if x['year'] == year and x.get('yearQnum') == qnum), None)
    if q:
        print(f"\n--- {year}-{qnum} ---")
        print(f"smallSubject: {q.get('smallSubject', '')}")
        print(f"question: {q.get('question', '')[:200]}")
        print(f"A: {q.get('A', '')[:100]}")
        print(f"B: {q.get('B', '')[:100]}")
        print(f"C: {q.get('C', '')[:100]}")
        print(f"D: {q.get('D', '')[:100]}")
        print(f"answer: '{q.get('answer', '')}'")
        print(f"analysis: {q.get('analysis', '')[:200]}")

# 查看2024年题号情况
print("\n\n=== 2024年题号情况 ===")
year_2024 = [q for q in pro if q['year'] == '2024']
year_2024_sorted = sorted(year_2024, key=lambda x: x.get('yearQnum', 0))
for q in year_2024_sorted:
    print(f"  {q['year']}-{q.get('yearQnum')}: {q.get('question', '')[:60]}...")

# 查看图片问题题目
print("\n\n=== 图片问题题目示例 ===")
image_questions = []
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if '见PDF' in text or '见本题配图' in text or 'PDF第' in text:
            image_questions.append((q['year'], q.get('yearQnum'), field, text[:100]))
            break

print(f"共{len(image_questions)}道题有图片标记")
for year, qnum, field, text in image_questions[:10]:
    print(f"  {year}-{qnum} {field}: {text}")
