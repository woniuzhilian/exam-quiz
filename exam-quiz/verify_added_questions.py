import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离专业基础
pro = [q for q in questions if q['bigSubject'] == '专业基础']

print(f"专业基础总题数: {len(pro)}")

# 检查新添加的题目（13-16题和其他缺少的题）
print("\n=== 抽查新添加的题目 ===")
check_questions = [
    ('2016', 13), ('2016', 45),
    ('2017', 13), ('2018', 13),
    ('2019', 13), ('2019', 51),
    ('2020', 13), ('2021', 13),
    ('2022', 13), ('2022', 44),
    ('2022补', 13), ('2023', 13),
]

for year, qnum in check_questions:
    q = next((x for x in pro if x['year'] == year and x.get('yearQnum') == qnum), None)
    if q:
        print(f"\n{year}-{qnum} ({q['smallSubject']})")
        print(f"  题干: {q['question'][:80]}")
        print(f"  A: {q['A'][:40]}")
        print(f"  B: {q['B'][:40]}")
        print(f"  C: {q['C'][:40]}")
        print(f"  D: {q['D'][:40]}")
        print(f"  答案: {q['answer']}")
        print(f"  解析: {q['analysis'][:80]}")
    else:
        print(f"\n{year}-{qnum}: 未找到")

# 检查字段完整性
required_fields = ['id', 'bigSubject', 'smallSubject', 'year', 'question', 'A', 'B', 'C', 'D', 'answer', 'analysis']
missing_fields = []
for q in pro:
    for field in required_fields:
        if field not in q:
            missing_fields.append((q.get('id'), field))

if missing_fields:
    print(f"\n缺少字段的题目: {missing_fields[:10]}")
else:
    print("\n所有题目字段完整")

# 检查answer字段
invalid_answers = [q for q in pro if q['answer'] not in ['A', 'B', 'C', 'D', '']]
if invalid_answers:
    print(f"无效answer的题目: {len(invalid_answers)}道")
else:
    print("所有answer字段有效")
