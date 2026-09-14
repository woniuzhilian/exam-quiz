import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

pro = [q for q in questions if q['bigSubject'] == '专业基础']
public = [q for q in questions if q['bigSubject'] == '公共基础']

# 已提取配图的题目
extracted_images = {
    ('2016', 22): '/images/pro/2016_22.png',
    ('2017', 24): '/images/pro/2017_24.png',
    ('2018', 22): '/images/pro/2018_22.png',
    ('2022', 24): '/images/pro/2022_24.png',
}

# 更新题库
count_extracted = 0
count_remaining = 0

for q in pro:
    key = (q['year'], q.get('yearQnum'))
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        if '本题配图' in text or '见本题配图' in text:
            if key in extracted_images:
                # 替换为img标签
                img_tag = f'<img src="{extracted_images[key]}" style="max-width:100%;" />'
                q[field] = re.sub(r'【本题配图，PDF第\d+页】', img_tag, text)
                count_extracted += 1
                print(f'已替换 {key[0]}-{key[1]} {field} 为图片')
            else:
                # 保留提示，但简化
                q[field] = re.sub(r'【本题配图，PDF第\d+页】', '【本题配有示意图】', text)
                count_remaining += 1

print(f'\n已提取配图: {count_extracted} 个字段')
print(f'仍需处理配图: {count_remaining} 个字段')

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
