import json, re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

images_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'

# 处理选项包含配图的题目
fixed_count = 0
for q in questions:
    img_file = None
    img_fields = []
    
    # 找出所有包含配图标记的选项
    for field in ['A', 'B', 'C', 'D']:
        match = re.search(r'【见本题选项配图[:：]([^】]+)】', q.get(field, ''))
        if match:
            if img_file is None:
                img_file = match.group(1)
            img_fields.append(field)
    
    if img_file:
        # 将图片添加到题干末尾
        img_tag = f'<br><img src="/images/{img_file}" style="max-width:100%;">'
        if '<img' not in q['question']:
            q['question'] = q['question'] + img_tag
        
        # 清空选项中的配图标记，保留其他文字内容
        for field in img_fields:
            q[field] = re.sub(r'【见本题选项配图[:：][^】]+】', '', q[field]).strip()
            # 如果选项为空，设置为选项标签
            if not q[field]:
                q[field] = f'选项{field}'
        
        fixed_count += 1

print(f"已处理 {fixed_count} 道题的选项配图")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

# 验证
remaining = 0
for q in questions:
    for field in ['A', 'B', 'C', 'D']:
        if '见本题选项配图' in q.get(field, ''):
            remaining += 1
            break
print(f"剩余选项配图标记: {remaining} 道")

# 统计题干中的图片
img_in_question = 0
for q in questions:
    if '<img' in q.get('question', ''):
        img_in_question += 1
print(f"题干中包含图片的题目: {img_in_question} 道")
