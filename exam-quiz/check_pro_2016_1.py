import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 查找专业基础2016-1题
for q in questions:
    if q['bigSubject'] == '专业基础' and q['year'] == '2016' and q.get('yearQnum') == 1:
        print('=== 2016-1 ===')
        print('id:', q['id'])
        print('smallSubject:', q['smallSubject'])
        print('question:', q['question'])
        print('A:', q['A'])
        print('B:', q['B'])
        print('C:', q['C'])
        print('D:', q['D'])
        print('answer:', q['answer'])
        print('analysis:', q['analysis'])
        break
