import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 先看几个典型的解析问题
print("=== 典型解析问题样本 ===")
count = 0
for q in questions:
    text = q.get('analysis', '')
    if not text:
        continue
    # 查找 $xxx$$yyy 模式
    if re.search(r'\$[a-zA-Z]+\$\$[a-zA-Z]+\$', text):
        count += 1
        if count <= 5:
            print(f"\n{q['year']}-{q.get('yearQnum')}:")
            print(f"  {text[:150]}")

print(f"\n共 {count} 个解析有 $xxx$$yyy$ 模式")

# 查找 \命令+字母 模式（未被$包裹且命令后紧跟字母）
print("\n=== 未被包裹的\\命令+字母模式 ===")
count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        cleaned = re.sub(r'\$[^$]*\$', '', text)
        matches = re.findall(r'\\[a-zA-Z]+[a-zA-Z]', cleaned)
        if matches:
            count += 1
            if count <= 5:
                print(f"\n{q['year']}-{q.get('yearQnum')} {field}:")
                print(f"  matches: {matches[:5]}")
                print(f"  text: {text[:100]}")

print(f"\n共 {count} 个字段有此问题")
