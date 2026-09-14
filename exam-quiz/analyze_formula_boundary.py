import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分析检查3的具体模式
print("=== 分析 $=开头 的模式 ===")
count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        # 查找 $= 或 $: 模式
        matches = re.findall(r'.{0,20}\$[=:].{0,20}', text)
        if matches:
            count += 1
            if count <= 10:
                print(f"\n{q['year']}-{q.get('yearQnum')} {field}:")
                for m in matches[:3]:
                    print(f"  {m}")

print(f"\n共 {count} 个字段有 $=或$:开头 模式")

print("\n=== 分析 =$结尾 的模式 ===")
count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        # 查找 =$ 或 :$ 模式（不在$$中间）
        matches = re.findall(r'.{0,20}[=:]\$.{0,20}', text)
        if matches:
            count += 1
            if count <= 10:
                print(f"\n{q['year']}-{q.get('yearQnum')} {field}:")
                for m in matches[:3]:
                    print(f"  {m}")

print(f"\n共 {count} 个字段有 =$或:$结尾 模式")
