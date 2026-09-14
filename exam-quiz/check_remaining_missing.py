import json
import os
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

image_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'

# 扫描所有图片
all_images = set(os.listdir(image_dir))

# 检查剩余的选项缺失题目
print("剩余选项缺失的题目:")
for q in questions:
    for field in ['A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if text in ['选项A', '选项B', '选项C', '选项D', 'A', 'B', 'C', 'D', '']:
            if q.get('A') and '<img' in q.get('A', ''):
                continue
            year = q['year']
            qnum = q.get('yearQnum', q['id'])
            # 查找相关图片
            related_images = [img for img in all_images if f'{year}_{qnum}' in img]
            print(f"  {year}-{qnum} ({q['bigSubject']}): 相关图片{len(related_images)}张")
            if related_images:
                print(f"    {related_images[:5]}")
            break
