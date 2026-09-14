import json, re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 检查各种图片标记方式
img_tag_count = 0
bracket_count = 0
peitu_count = 0
samples = []

for q in data:
    text = q.get('question','') + q.get('A','') + q.get('B','') + q.get('C','') + q.get('D','')
    if '<img' in text:
        img_tag_count += 1
        if len(samples) < 3:
            samples.append(('img标签', q['bigSubject'], q['year'], q['id'], text[:150]))
    if '【' in text and '配图' in text:
        bracket_count += 1
        if len(samples) < 6:
            samples.append(('【】标记', q['bigSubject'], q['year'], q['id'], text[:150]))
    if '配图' in text:
        peitu_count += 1

print(f'含<img>标签的题目: {img_tag_count}')
print(f'含【】配图标记的题目: {bracket_count}')
print(f'含"配图"字样的题目: {peitu_count}')
print()
for s in samples:
    print(f'[{s[0]}] {s[1]} {s[2]}-{s[3]}: {s[4]}')
    print()
