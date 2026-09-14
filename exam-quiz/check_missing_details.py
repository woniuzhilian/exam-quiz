import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离公共基础
public = [q for q in questions if q['bigSubject'] == '公共基础']

# 检查缺失题号的具体情况
print("=== 检查缺失题号的题目 ===")
for year in ['2017', '2018', '2021', '2023']:
    year_questions = [q for q in public if q['year'] == year]
    qnums = sorted([q.get('yearQnum', q['id']) for q in year_questions])
    
    print(f"\n{year}年:")
    print(f"  总题数: {len(year_questions)}")
    print(f"  题号范围: {min(qnums)} - {max(qnums)}")
    
    # 查看最后5道题
    last_5 = sorted(year_questions, key=lambda x: x.get('yearQnum', x['id']))[-5:]
    print(f"  最后5道题:")
    for q in last_5:
        print(f"    id={q['id']}, yearQnum={q.get('yearQnum')}, {q['question'][:40]}...")

# 检查空字段的题目
print("\n=== 检查空字段的题目 ===")
empty_check = [
    ('2021', 21), ('2021', 22), ('2022', 58), ('2022', 60)
]

for year, qnum in empty_check:
    q = next((x for x in public if x['year'] == year and x.get('yearQnum') == qnum), None)
    if q:
        print(f"\n{year}-{qnum}:")
        print(f"  题干: {q['question'][:80]}...")
        print(f"  A: '{q['A']}'")
        print(f"  B: '{q['B']}'")
        print(f"  C: '{q['C']}'")
        print(f"  D: '{q['D']}'")
        print(f"  答案: {q['answer']}")
        print(f"  解析: {q['analysis'][:80]}...")
