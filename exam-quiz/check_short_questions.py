import json

with open(r'D:\应用程序开发\刷题\exam-quiz\pdf_image_mapping.json', 'r', encoding='utf-8') as f:
    pdf_mapping = json.load(f)

# 检查题干只有"图"字的题目
short_questions = ['2013-90', '2017-455', '2018-562', '2018-563', '2018-569', '2019-690', '2019-691', '2020-812']
print("=== 题干只有'图'字的题目 ===")
for q in short_questions:
    if q in pdf_mapping:
        print(f'  {q}: 有图片 {pdf_mapping[q]}')
    else:
        print(f'  {q}: 无图片')

# 检查184道未匹配题目的分布
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

import re
unmatched = []
for q in data:
    text = q.get('question', '')
    if '本题配图' in text and 'PDF第' in text:
        key = f'{q["year"]}-{q["id"]}'
        has_pdf_img = key in pdf_mapping
        clean_text = re.sub(r'【本题配图[，,]PDF第\d+页】', '', text).strip()
        is_short = len(clean_text) < 15
        unmatched.append({
            'key': key,
            'smallSubject': q.get('smallSubject', ''),
            'is_short': is_short,
            'text': clean_text[:50]
        })

print(f'\n=== 未匹配题目统计 ===')
print(f'总数: {len(unmatched)}')
print(f'题干过短(<15字): {sum(1 for u in unmatched if u["is_short"])}')
print(f'在pdf_mapping中有图片: {sum(1 for u in unmatched if u["key"] in pdf_mapping)}')

print(f'\n=== 题干过短的题目 ===')
for u in unmatched:
    if u['is_short']:
        print(f'  {u["key"]} [{u["smallSubject"]}]: {u["text"]}')
