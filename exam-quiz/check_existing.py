import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 检查这8道题的内容
check_list = [
    ('公共基础', '2017', 40),
    ('公共基础', '2017', 56),
    ('公共基础', '2018', 19),
    ('公共基础', '2018', 64),
    ('公共基础', '2021', 14),
    ('公共基础', '2021', 58),
    ('公共基础', '2023', 34),
    ('专业基础', '2024', 56),
]

for big, year, qnum in check_list:
    for q in questions:
        if q['bigSubject'] == big and q['year'] == year and q.get('yearQnum') == qnum:
            print(f"\n=== {big} {year}-{qnum} ===")
            print(f"题干: {q['question'][:100]}")
            print(f"选项A: {q['A'][:50]}")
            print(f"选项B: {q['B'][:50]}")
            print(f"答案: {q['answer']}")
            print(f"解析: {q['analysis'][:100]}")
            print(f"小科目: {q.get('smallSubject', '空')}")
            break
