import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

pro = [q for q in questions if q['bigSubject'] == '专业基础']
year_2024 = [q for q in pro if q['year'] == '2024']
year_2024_sorted = sorted(year_2024, key=lambda x: x.get('yearQnum', 0))

print("2024年题目列表:")
for q in year_2024_sorted:
    print(f"  {q['year']}-{q.get('yearQnum')}: {q.get('question', '')[:80]}...")
