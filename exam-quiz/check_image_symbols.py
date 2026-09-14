import json
import os
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离公共基础
public = [q for q in questions if q['bigSubject'] == '公共基础']

# 检查空字段题目的图片引用
print("=== 检查空字段题目的图片引用 ===")
empty_check = [
    ('2021', 21), ('2021', 22), ('2022', 58), ('2022', 60)
]

image_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'

for year, qnum in empty_check:
    q = next((x for x in public if x['year'] == year and x.get('yearQnum') == qnum), None)
    if q:
        print(f"\n{year}-{qnum}:")
        # 检查题干中的图片
        img_tags = re.findall(r'<img[^>]*src="([^"]*)"', q['question'])
        print(f"  题干图片: {img_tags}")
        for img in img_tags:
            img_path = os.path.join(image_dir, os.path.basename(img))
            exists = os.path.exists(img_path)
            print(f"    {img}: {'存在' if exists else '不存在'}")
        
        # 检查选项中的图片
        for opt in ['A', 'B', 'C', 'D']:
            opt_text = q.get(opt, '')
            opt_imgs = re.findall(r'<img[^>]*src="([^"]*)"', opt_text)
            if opt_imgs:
                print(f"  选项{opt}图片: {opt_imgs}")
                for img in opt_imgs:
                    img_path = os.path.join(image_dir, os.path.basename(img))
                    exists = os.path.exists(img_path)
                    print(f"    {img}: {'存在' if exists else '不存在'}")

# 检查特殊符号问题的题目
print("\n=== 检查特殊符号问题的题目 ===")
symbol_check = [
    ('2013', 61, 'D'), ('2017', 12, 'analysis'), ('2017', 24, 'question'),
    ('2018', 81, 'B'), ('2018', 81, 'C'), ('2019', 9, 'question'),
    ('2019', 14, 'analysis'), ('2024', 9, 'analysis'), ('2024', 10, 'question'),
    ('2024', 73, 'question')
]

for year, qnum, field in symbol_check:
    q = next((x for x in public if x['year'] == year and x.get('yearQnum') == qnum), None)
    if q:
        text = q.get(field, '')
        print(f"\n{year}-{qnum} {field}:")
        print(f"  内容: {text[:100]}...")
