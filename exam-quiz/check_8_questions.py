import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

targets = ['2017-455', '2018-562', '2018-563', '2018-569', '2018-600', '2019-690', '2019-691', '2020-812']

for q in data:
    key = f'{q["year"]}-{q["id"]}'
    if key in targets:
        print(f'\n=== {key} ===')
        print(f'bigSubject: {q["bigSubject"]}')
        print(f'smallSubject: {q.get("smallSubject", "")}')
        print(f'question: {q["question"][:100]}')
        print(f'A: {q.get("A", "")[:80]}')
        print(f'B: {q.get("B", "")[:80]}')
        print(f'C: {q.get("C", "")[:80]}')
        print(f'D: {q.get("D", "")[:80]}')
        print(f'answer: {q.get("answer", "")}')
        print(f'analysis: {q.get("analysis", "")[:100]}')
