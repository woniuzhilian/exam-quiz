import json
from collections import defaultdict

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 按大科目+年份分组，分配年份内题号
by_subject_year = defaultdict(list)
for q in questions:
    key = (q['bigSubject'], q['year'])
    by_subject_year[key].append(q)

# 为每道题添加yearQnum
for key, qs in by_subject_year.items():
    for i, q in enumerate(qs):
        q['yearQnum'] = i + 1

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"已为{len(questions)}道题添加yearQnum字段")

# 验证2014年的题号
print(f"\n2014年公共基础前10题:")
count = 0
for q in questions:
    if q['bigSubject'] == '公共基础' and q['year'] == '2014':
        count += 1
        if count <= 10:
            print(f"  yearQnum={q['yearQnum']}, id={q['id']}, {q['question'][:40]}")
