import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 只检查专业基础
pro_questions = [q for q in questions if q['bigSubject'] == '专业基础']

# 查找包含公式的题目（包含$的）
print("=== 专业基础包含公式的题目（前30道）===")
count = 0
for q in pro_questions:
    qid = f"{q['year']}-{q.get('yearQnum')}"
    has_math = False
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if '$' in text:
            has_math = True
            break
    if has_math:
        print(f"\n--- {qid} ({q['smallSubject']}) ---")
        print(f"question: {q['question'][:120]}")
        if '$' in q.get('A', ''):
            print(f"A: {q['A'][:80]}")
        if '$' in q.get('B', ''):
            print(f"B: {q['B'][:80]}")
        count += 1
        if count >= 30:
            break

print(f"\n专业基础包含公式的题目数: 正在统计...")
math_count = sum(1 for q in pro_questions if any('$' in q.get(f, '') for f in ['question', 'A', 'B', 'C', 'D', 'analysis']))
print(f"总计: {math_count}道题包含公式")
