import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 列出所有还有问题的题目
issues = []

for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if not text:
            continue
        # 移除$中的内容
        cleaned = re.sub(r'\$[^$]*\$', '', text)
        # 移除HTML标签
        cleaned = re.sub(r'<[^>]+>', '', cleaned)
        # 末尾有单独的数字（下标残留）
        if re.search(r'\s+\d+\s*$', cleaned.strip()) and len(cleaned.strip()) > 10:
            year = q['year']
            qnum = q.get('yearQnum')
            issues.append((year, qnum, field, text[-80:]))

print(f"共发现 {len(issues)} 个有问题的字段")
print()
for year, qnum, field, preview in issues:
    print(f"{year}-{qnum} {field}: ...{preview}")
