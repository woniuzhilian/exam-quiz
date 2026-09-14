import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离公共基础
public = [q for q in questions if q['bigSubject'] == '公共基础']

# 检查2021年的题目
year_2021 = [q for q in public if q['year'] == '2021']
year_2021_sorted = sorted(year_2021, key=lambda x: x.get('yearQnum', 0))

print("2021年题目列表:")
for q in year_2021_sorted:
    print(f"  {q['year']}-{q.get('yearQnum')}: {q['question'][:50]}...")

# 检查是否有题号不连续的情况
qnums = [q.get('yearQnum') for q in year_2021_sorted]
print(f"\n题号列表: {qnums}")
print(f"题号范围: {min(qnums)} - {max(qnums)}")
print(f"题数: {len(qnums)}")
