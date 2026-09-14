import json, re, os
from collections import Counter

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 检查选项中使用图片的题目
option_img_questions = []
for q in data:
    for opt in ['A', 'B', 'C', 'D']:
        val = q.get(opt, '')
        if '<img' in val:
            option_img_questions.append(q)
            break

print(f"选项中含图片的题目: {len(option_img_questions)}道")

# 检查是否有多个选项使用同一张图片（可能是错误的大截图）
same_img_count = 0
for q in option_img_questions:
    imgs = []
    for opt in ['A', 'B', 'C', 'D']:
        val = q.get(opt, '')
        m = re.search(r'<img[^>]+src="/images/([^"]+)"', val)
        if m:
            imgs.append(m.group(1))
    if len(imgs) > 1 and len(set(imgs)) == 1:
        same_img_count += 1
        if same_img_count <= 10:
            print(f"  {q['year']}-{q['id']} [{q['smallSubject']}]: 所有选项都是同一张图 {imgs[0]}")

print(f"\n多个选项使用同一张图片的题目: {same_img_count}道")

# 检查图片文件名规律
img_names = []
for q in option_img_questions:
    for opt in ['A', 'B', 'C', 'D']:
        val = q.get(opt, '')
        m = re.search(r'<img[^>]+src="/images/([^"]+)"', val)
        if m:
            img_names.append(m.group(1))

print(f"\n选项图片文件名分布:")
name_patterns = Counter()
for name in set(img_names):
    if name.startswith('q'):
        name_patterns['q{id}_{year}.png'] += 1
    elif name.startswith('pdf_'):
        name_patterns['pdf_render/*.png'] += 1
    elif name.startswith('id'):
        name_patterns['id*_*.png'] += 1
    else:
        name_patterns['other'] += 1

for pattern, count in name_patterns.items():
    print(f"  {pattern}: {count}个文件")
