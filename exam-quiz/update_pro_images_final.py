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

# 2024年题号映射：题库中的题号 -> PDF中的题号
# 题库中2024-17到2024-60实际上是PDF中的2024-21到2024-64
# 但由于专业基础每年只有60道题，这里需要仔细处理
# 从PDF来看，2024-22是几何组成，2024-25是超静定次数，2024-26是结构动力反应分析
# 从题库来看，2024-18是几何组成，2024-21是超静定次数，2024-22是结构动力反应分析
# 这说明题库中的2024年题号从17开始都小了4

# 先更新题库中的配图
count = 0
for q in pro:
    year = q['year']
    qnum = q.get('yearQnum')
    
    # 对于2024年，需要映射到PDF中的题号
    if year == '2024' and qnum >= 17:
        pdf_qnum = qnum + 4
        key = (year, pdf_qnum)
    else:
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
                print(f'已替换 {year}-{qnum} {field} (PDF题号: {pdf_qnum if year == "2024" and qnum >= 17 else qnum})')

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
