import json
import re
import os

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

pro = [q for q in questions if q['bigSubject'] == '专业基础']
public = [q for q in questions if q['bigSubject'] == '公共基础']

# 已提取配图的题目
image_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images\pro'
extracted_images = {}

# 扫描已提取的图片
for f in os.listdir(image_dir):
    if f.endswith('.png'):
        # 解析文件名，格式：年份_题号.png
        parts = f.replace('.png', '').split('_')
        if len(parts) == 2:
            year = parts[0]
            qnum = int(parts[1])
            extracted_images[(year, qnum)] = f'/images/pro/{f}'

print(f'已提取配图: {len(extracted_images)} 张')
for key in sorted(extracted_images.keys()):
    print(f'  {key[0]}-{key[1]}: {extracted_images[key]}')

# 更新题库
count = 0
for q in pro:
    year = q['year']
    qnum = q.get('yearQnum')
    key = (year, qnum)
    if key in extracted_images:
        for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
            text = q.get(field, '')
            if not text:
                continue
            if '本题配有示意图' in text or '本题配图' in text:
                img_tag = f'<img src="{extracted_images[key]}" style="max-width:100%;" />'
                q[field] = re.sub(r'【本题配有示意图】|【本题配图，PDF第\d+页】', img_tag, text)
                count += 1
                print(f'已替换 {year}-{qnum} {field}')

print(f'\n共替换 {count} 个字段')

# 重新排序和分配id
pro.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))
public.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))

for i, q in enumerate(public):
    q['id'] = i + 1

pro_start = len(public) + 1
for i, q in enumerate(pro):
    q['id'] = pro_start + i

final = public + pro

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print('\n题库已更新')
