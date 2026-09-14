import json

with open(r'D:\应用程序开发\刷题\exam-quiz\pub_final.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

unmatched = [q for q in questions if not q['smallSubject']]
print(f"匹配失败题目: {len(unmatched)}")

from collections import Counter
year_counts = Counter(q['year'] for q in unmatched)
print(f"\n按年份分布:")
for y, c in sorted(year_counts.items()):
    print(f"  {y}: {c}题")

print(f"\n所有匹配失败的题目:")
for q in unmatched:
    # 计算实际题号
    year = q['year']
    year_starts = {'2013': 0, '2014': 120, '2016': 240, '2017': 360, '2018': 480,
                   '2019': 600, '2020': 720, '2021': 840, '2022': 960, '2022补': 1080,
                   '2023': 1200, '2024': 1320}
    actual_qnum = q['id'] - year_starts.get(year, 0)
    print(f"  {year}-{actual_qnum}: {q['question'][:60]}")
