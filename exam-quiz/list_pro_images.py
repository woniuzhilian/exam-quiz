import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

pro = [q for q in questions if q['bigSubject'] == '专业基础']

# 查找所有包含图片标记的题目
image_questions = []
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if '本题配图' in text or '见本题配图' in text:
            # 提取页码
            page_match = re.search(r'PDF第(\d+)页', text)
            page = page_match.group(1) if page_match else '未知'
            image_questions.append({
                'year': q['year'],
                'qnum': q.get('yearQnum'),
                'field': field,
                'page': page,
                'text': text[:100]
            })
            break

print(f'共{len(image_questions)}道题有图片标记')
print('\n题目列表:')
for item in image_questions:
    print(f"  {item['year']}-{item['qnum']} (PDF第{item['page']}页)")
