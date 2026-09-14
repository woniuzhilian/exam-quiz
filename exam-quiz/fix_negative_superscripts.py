import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 需要修复负号的题目列表
negative_fix_list = [
    ('2013', 78),
    ('2014', 35),
    ('2016', 35),
    ('2018', 34),
    ('2018', 35),
    ('2019', 34),
    ('2020', 35),
]

fixed_count = 0
for q in questions:
    year = q['year']
    qnum = q.get('yearQnum')
    if (year, qnum) in negative_fix_list:
        for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
            text = q.get(field, '')
            if not text:
                continue
            # 10^{数字} -> 10^{-数字}（在物理上下文中）
            original = text
            text = re.sub(r'(\d+)\^\{(\d+)\}', r'\1^{-\\2}', text)
            # 上面的替换有问题，让我用正确的方式
            text = re.sub(r'(\d+)\^\{(\d+)\}', lambda m: m.group(1) + '^{-' + m.group(2) + '}', text)
            if text != original:
                q[field] = text
                fixed_count += 1
                print(f'修复 {year}-{qnum} {field}')

print(f'共修复 {fixed_count} 个字段')

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")
