import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 检查题干末尾有多余数字/符号的题目
print('=== 题干末尾有多余数字/符号的题目 ===')
count = 0
issues = []
for q in questions:
    text = q.get('question', '').strip()
    # 检查末尾是否有类似 '数字 数字 数字' 或 '数字 ; 数字 数字' 的模式
    if re.search(r'[\d;]\s+[\d;]\s+[\d;]?\s*$', text) and not text.endswith('。') and not text.endswith('）'):
        count += 1
        issues.append((q['year'], q.get('yearQnum'), text[-60:]))
        if count <= 30:
            print(f"{q['year']}-{q.get('yearQnum')}: ...{text[-60:]}")

print(f'总计: {count} 道题')

print()
print('=== 题干中包含空公式的题目 ===')
count = 0
for q in questions:
    text = q.get('question', '')
    if re.search(r'\$\s*[=:]\s*\$', text) or re.search(r'\$\s*=\s*=\s*\$', text):
        count += 1
        if count <= 10:
            print(f"{q['year']}-{q.get('yearQnum')}: {text[:80]}")

print(f'总计: {count} 道题')

# 保存问题清单
with open(r'D:\应用程序开发\刷题\exam-quiz\question_issues.json', 'w', encoding='utf-8') as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)
