import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离专业基础
pro_questions = [q for q in questions if q['bigSubject'] == '专业基础']

print(f"专业基础总题数: {len(pro_questions)}")

# 按年份统计
from collections import defaultdict
year_questions = defaultdict(list)
for q in pro_questions:
    year_questions[q['year']].append(q)

# 各年份应有题数（2024年56题，其余60题）
expected = {
    '2016': 60, '2017': 60, '2018': 60, '2019': 60, '2020': 60,
    '2021': 60, '2022': 60, '2022补': 60, '2023': 60, '2024': 56
}

print("\n各年份题数统计:")
for year in sorted(year_questions.keys()):
    qs = year_questions[year]
    qnums = sorted([q.get('yearQnum', 0) for q in qs])
    exp = expected.get(year, 60)
    missing = [i for i in range(1, exp+1) if i not in qnums]
    print(f"  {year}: {len(qs)}题 (应有{exp}题), 缺少: {missing}")

# 2014年的题
year_2014 = [q for q in pro_questions if q['year'] == '2014']
print(f"\n2014年题数: {len(year_2014)}")
for q in year_2014:
    print(f"  id={q['id']}, yearQnum={q.get('yearQnum')}, {q['smallSubject']}")
