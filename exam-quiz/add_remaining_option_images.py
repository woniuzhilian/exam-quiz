import json
import os
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

image_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'
all_images = set(os.listdir(image_dir))

# 为有相关图片的题目添加配图
count = 0
for q in questions:
    for field in ['A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if text in ['选项A', '选项B', '选项C', '选项D', 'A', 'B', 'C', 'D', '']:
            if q.get('A') and '<img' in q.get('A', ''):
                continue
            year = q['year']
            qnum = q.get('yearQnum', q['id'])
            # 查找相关图片（包括_crop.png等格式）
            related_images = sorted([img for img in all_images if f'{year}_{qnum}' in img])
            if related_images:
                # 过滤掉题干配图（index=1）
                option_images = []
                for img in related_images:
                    match = re.match(r'id\d+_\d+_\d+_(\d+)\.', img)
                    if match:
                        index = int(match.group(1))
                        if index >= 2:
                            option_images.append(f'/images/{img}')
                    elif '_crop' in img:
                        option_images.append(f'/images/{img}')
                    elif 'q' in img:
                        option_images.append(f'/images/{img}')
                
                if option_images:
                    if len(option_images) >= 4:
                        q['A'] = f'<img src="{option_images[0]}" style="max-width:100%;" />'
                        q['B'] = f'<img src="{option_images[1]}" style="max-width:100%;" />'
                        q['C'] = f'<img src="{option_images[2]}" style="max-width:100%;" />'
                        q['D'] = f'<img src="{option_images[3]}" style="max-width:100%;" />'
                    else:
                        combined = '<br>'.join([f'<img src="{img}" style="max-width:100%;" />' for img in option_images])
                        q['A'] = combined
                        q['B'] = ''
                        q['C'] = ''
                        q['D'] = ''
                    count += 1
                    print(f"已添加选项配图: {year}-{qnum} ({len(option_images)}张)")
            break

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

print(f"\n仍有 {remaining} 道题选项缺失（需要从PDF中提取配图）")
