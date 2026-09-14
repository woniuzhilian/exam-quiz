import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 检查10^{数字}但可能缺少负号的情况
count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        # 查找 10^{数字} 模式（没有负号）
        matches = re.findall(r'10\^\{(\d+)\}', text)
        if matches:
            # 检查上下文是否应该是负数（如粘度、波长等）
            if any(kw in text for kw in ['粘度', '波长', 'nm', 'μm', '厚度', '直径', '10;', '×10']):
                year = q['year']
                qnum = q.get('yearQnum')
                print(f'{year}-{qnum} {field}: {matches} | {text[:100]}')
                count += 1
                if count > 30:
                    break
    if count > 30:
        break
print(f'共发现 {count} 个可能缺少负号的上标')
