import json, re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 检查题干过短的题目（可能提取不完整）
short_questions = []
for q in data:
    text = q.get('question', '')
    # 去掉HTML标签和配图标记
    clean_text = re.sub(r'<[^>]+>', '', text)
    clean_text = re.sub(r'【[^】]+】', '', clean_text)
    clean_text = clean_text.strip()
    if len(clean_text) < 20:
        short_questions.append({
            'bigSubject': q['bigSubject'],
            'year': q['year'],
            'id': q['id'],
            'smallSubject': q.get('smallSubject', ''),
            'question': clean_text,
            'has_img': '<img' in text
        })

print(f'题干过短(<20字)的题目: {len(short_questions)}道')
print(f'\n按大科目分布:')
from collections import Counter
print(Counter(q['bigSubject'] for q in short_questions))

print(f'\n题目列表（前30道）:')
for q in short_questions[:30]:
    img_mark = '[有图]' if q['has_img'] else '[无图]'
    print(f'  {q["bigSubject"]} {q["year"]}-{q["id"]} {img_mark} [{q["smallSubject"]}]: {q["question"]}')
