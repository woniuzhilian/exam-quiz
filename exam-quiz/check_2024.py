import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离专业基础
pro_questions = [q for q in questions if q['bigSubject'] == '专业基础']

# 查看2024年的题目
year_2024 = [q for q in pro_questions if q['year'] == '2024']
print(f"2024年题数: {len(year_2024)}")
qnums = sorted([q.get('yearQnum', 0) for q in year_2024])
print(f"2024年题号: {qnums}")

# 检查重复
from collections import Counter
qnum_counts = Counter(qnums)
duplicates = {k: v for k, v in qnum_counts.items() if v > 1}
print(f"重复题号: {duplicates}")

# 查看2024年每道题的小科目
print("\n2024年题目详情:")
for q in sorted(year_2024, key=lambda x: x.get('yearQnum', 0)):
    print(f"  2024-{q.get('yearQnum')}: {q['smallSubject']} - {q['question'][:30]}...")
