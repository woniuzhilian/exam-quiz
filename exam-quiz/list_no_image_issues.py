import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 过滤掉带图片的题目，列出剩余的问题
issues = []

for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if not text:
            continue
        # 跳过带图片的题目
        if '<img' in text:
            continue
        # 移除$中的内容
        cleaned = re.sub(r'\$[^$]*\$', '', text)
        # 移除HTML标签
        cleaned = re.sub(r'<[^>]+>', '', cleaned)
        # 末尾有单独的数字（下标残留）
        if re.search(r'\s+\d+\s*$', cleaned.strip()) and len(cleaned.strip()) > 10:
            year = q['year']
            qnum = q.get('yearQnum')
            issues.append((year, qnum, field, text))

print(f"不带图片的问题字段: {len(issues)} 个")
print()
for year, qnum, field, text in issues:
    print(f"=== {year}-{qnum} {field} ===")
    print(text[:200])
    print()
