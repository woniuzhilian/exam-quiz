import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 检查每年的前5题和后5题，判断题号是否对应
years = ['2013', '2014', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']

for year in years:
    year_questions = [q for q in data if q['bigSubject'] == '公共基础' and q['year'] == year]
    if not year_questions:
        continue
    print(f"\n=== {year}年（共{len(year_questions)}题）===")
    print(f"  前3题:")
    for q in year_questions[:3]:
        print(f"    id={q['id']}, [{q['smallSubject']}], {q['question'][:50]}")
    print(f"  后3题:")
    for q in year_questions[-3:]:
        print(f"    id={q['id']}, [{q['smallSubject']}], {q['question'][:50]}")
