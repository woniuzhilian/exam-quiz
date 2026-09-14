import json

# 读取新题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"总题目数量: {len(questions)}")

# 按大科目统计
public = [q for q in questions if q['bigSubject'] == '公共基础']
pro = [q for q in questions if q['bigSubject'] == '专业基础']

print(f"公共基础: {len(public)}道")
print(f"专业基础: {len(pro)}道")

# 按年份统计专业基础
from collections import Counter
pro_years = Counter(q['year'] for q in pro)
print("\n专业基础各年份数量:")
for year in sorted(pro_years.keys()):
    print(f"  {year}: {pro_years[year]}道")

# 按小科目统计专业基础
pro_subjects = Counter(q['smallSubject'] for q in pro)
print("\n专业基础各小科目数量:")
for subject in sorted(pro_subjects.keys()):
    print(f"  {subject}: {pro_subjects[subject]}道")

# 检查字段完整性
required_fields = ['id', 'bigSubject', 'smallSubject', 'year', 'question', 'A', 'B', 'C', 'D', 'answer', 'analysis']
missing_fields = []
for q in questions:
    for field in required_fields:
        if field not in q:
            missing_fields.append((q.get('id', 'unknown'), field))

if missing_fields:
    print(f"\n缺少字段的题目: {missing_fields[:10]}")
else:
    print("\n所有题目字段完整")

# 检查answer字段
invalid_answers = []
for q in questions:
    if q['answer'] not in ['A', 'B', 'C', 'D', '']:
        invalid_answers.append((q['id'], q['year'], q.get('yearQnum', ''), q['answer']))

if invalid_answers:
    print(f"\n无效answer的题目: {invalid_answers[:10]}")
else:
    print("\n所有answer字段有效")

# 检查缺少答案解析的题目
missing_analysis = [q for q in pro if not q['analysis']]
print(f"\n专业基础缺少解析的题目: {len(missing_analysis)}道")
for q in missing_analysis:
    print(f"  {q['year']}-{q.get('yearQnum', q['id'])}")

# 抽查几道题
print("\n抽查专业基础前3道题:")
for q in pro[:3]:
    print(f"  id={q['id']}, {q['year']}-{q.get('yearQnum', '')}, {q['smallSubject']}")
    print(f"    题干: {q['question'][:50]}...")
    print(f"    答案: {q['answer']}")
    print(f"    解析: {q['analysis'][:50]}...")
