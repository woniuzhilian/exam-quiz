import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

pro = [q for q in questions if q['bigSubject'] == '专业基础']

# 查看空字段题目
problem_questions = [
    ('2017', 40),
    ('2018', 19),
    ('2020', 16),
    ('2024', 22),  # 原2024-26
]

for year, qnum in problem_questions:
    q = next((x for x in pro if x['year'] == year and x.get('yearQnum') == qnum), None)
    if q:
        print(f'--- {year}-{qnum} ---')
        print(f'smallSubject: {q.get("smallSubject", "")}')
        print(f'question: {q.get("question", "")[:150]}')
        print(f'A: {q.get("A", "")[:80]}')
        print(f'B: {q.get("B", "")[:80]}')
        print(f'C: {q.get("C", "")[:80]}')
        print(f'D: {q.get("D", "")[:80]}')
        print(f'answer: "{q.get("answer", "")}"')
        print(f'analysis: {q.get("analysis", "")[:150]}')
        print()
