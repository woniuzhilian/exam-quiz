import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 查找剩余的平行符号问题
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text and ('//' in text or '∥' in text):
            year = q['year']
            qnum = q.get('yearQnum')
            print(f'{year}-{qnum} {field}: {text[:120]}')
            print()
