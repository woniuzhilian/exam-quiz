import json
import os
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

image_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'

# 扫描所有图片，按年份和题号分组
image_map = {}
for filename in os.listdir(image_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        # 解析文件名，格式：id{id}_{year}_{qnum}_{index}.png
        match = re.match(r'id\d+_(\d+)_(\d+)_(\d+)\.(png|jpg|jpeg)', filename)
        if match:
            year = match.group(1)
            qnum = int(match.group(2))
            index = int(match.group(3))
            key = (year, qnum)
            if key not in image_map:
                image_map[key] = {}
            image_map[key][index] = f'/images/{filename}'

print(f"扫描到 {len(image_map)} 道题的配图")

# 为选项配图缺失的题目添加配图
count = 0
for q in questions:
    year = q['year']
    qnum = q.get('yearQnum', q['id'])
    key = (year, qnum)  # 修复：qnum是整数
    
    # 检查选项是否缺失
    options_missing = False
    for field in ['A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if text in ['选项A', '选项B', '选项C', '选项D', 'A', 'B', 'C', 'D', '']:
            options_missing = True
            break
    
    if options_missing and key in image_map:
        # 找到选项配图（index从2开始，1是题干配图）
        option_images = []
        for index in sorted(image_map[key].keys()):
            if index >= 2:
                option_images.append(image_map[key][index])
        
        if len(option_images) >= 4:
            q['A'] = f'<img src="{option_images[0]}" style="max-width:100%;" />'
            q['B'] = f'<img src="{option_images[1]}" style="max-width:100%;" />'
            q['C'] = f'<img src="{option_images[2]}" style="max-width:100%;" />'
            q['D'] = f'<img src="{option_images[3]}" style="max-width:100%;" />'
            count += 1
            print(f"已添加选项配图: {year}-{qnum}")
        elif len(option_images) > 0:
            # 如果不足4张，将所有选项配图合并到A选项
            combined = '<br>'.join([f'<img src="{img}" style="max-width:100%;" />' for img in option_images])
            q['A'] = combined
            q['B'] = ''
            q['C'] = ''
            q['D'] = ''
            count += 1
            print(f"已添加选项配图（合并）: {year}-{qnum} ({len(option_images)}张)")

print(f"\n共为 {count} 道题添加选项配图")

# 重新排序和分配id
public = [q for q in questions if q['bigSubject'] == '公共基础']
pro = [q for q in questions if q['bigSubject'] == '专业基础']

public.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))
pro.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))

for i, q in enumerate(public):
    q['id'] = i + 1

pro_start = len(public) + 1
for i, q in enumerate(pro):
    q['id'] = pro_start + i

final = public + pro

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print("\n题库已更新")

# 检查还有多少道题选项缺失
remaining = 0
for q in final:
    for field in ['A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if text in ['选项A', '选项B', '选项C', '选项D', 'A', 'B', 'C', 'D', '']:
            if q.get('A') and '<img' in q.get('A', ''):
                continue
            remaining += 1
            break

print(f"\n仍有 {remaining} 道题选项缺失")
