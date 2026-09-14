import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 检查特定题目
targets = [
    ('2019', 1),
    ('2016', 4),
    ('2014', 9),
]

for year, qnum in targets:
    for q in questions:
        if str(q.get('year')) == year and q.get('yearQnum') == qnum:
            print(f"\n=== {year}-{qnum} ===")
            print(f"id: {q['id']}")
            print(f"smallSubject: {q.get('smallSubject', '')}")
            print(f"question: {q['question']}")
            print(f"A: {q['A']}")
            print(f"B: {q['B']}")
            print(f"C: {q['C']}")
            print(f"D: {q['D']}")
            print(f"answer: {q['answer']}")
            print(f"analysis: {q['analysis'][:300]}")
            break

# 统计包含"见本题选项配图"或"配图"的题目
print("\n\n=== 包含'配图'标记的题目 ===")
count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D']:
        if '配图' in q.get(field, '') or '见本题' in q.get(field, ''):
            print(f"  {q['year']}-{q.get('yearQnum', q['id'])}: {field} = {q[field][:80]}")
            count += 1
            break
print(f"共 {count} 题")
