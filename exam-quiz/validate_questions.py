import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f'总题目数: {len(questions)}')
print(f'公共基础: {sum(1 for q in questions if q["bigSubject"]=="公共基础")}')
print(f'专业基础: {sum(1 for q in questions if q["bigSubject"]=="专业基础")}')

# 检查字段完整性
required_fields = ['id', 'bigSubject', 'smallSubject', 'year', 'question', 'A', 'B', 'C', 'D', 'answer', 'analysis']
missing_fields = []
for q in questions:
    for field in required_fields:
        if field not in q:
            missing_fields.append((q.get('year'), q.get('yearQnum'), field))

if missing_fields:
    print(f'缺失字段: {missing_fields[:10]}')
else:
    print('字段完整性: 全部通过')

# 检查answer格式
invalid_answers = [(q['year'], q.get('yearQnum'), q['answer']) for q in questions if q['answer'] not in ['A','B','C','D']]
if invalid_answers:
    print(f'无效answer: {invalid_answers[:10]}')
else:
    print('answer格式: 全部通过')

# 检查bigSubject
invalid_subjects = [(q['year'], q.get('yearQnum'), q['bigSubject']) for q in questions if q['bigSubject'] not in ['公共基础','专业基础']]
if invalid_subjects:
    print(f'无效bigSubject: {invalid_subjects[:10]}')
else:
    print('bigSubject格式: 全部通过')

# 检查smallSubject为空的题目
empty_small = [(q['year'], q.get('yearQnum')) for q in questions if not q['smallSubject']]
print(f'smallSubject为空的题目数: {len(empty_small)}')
if empty_small:
    print(f'前10个: {empty_small[:10]}')

# 检查$配对
unpaired_dollar = []
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text.count('$') % 2 != 0:
            unpaired_dollar.append((q['year'], q.get('yearQnum'), field))
            break

if unpaired_dollar:
    print(f'$未配对的题目数: {len(unpaired_dollar)}')
    print(f'前10个: {unpaired_dollar[:10]}')
else:
    print('$配对: 全部通过')

print('\n验证完成！')
