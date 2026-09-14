import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print("=" * 60)
print("扫描题干和选项中的上下标问题")
print("=" * 60)
print()

# 问题1：化学式中数字和字母分开（如 Na SO 2 4）
print("【问题1】化学式中数字和字母分开的情况")
print("-" * 40)
count1 = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if not text:
            continue
        # 移除$中的内容
        cleaned = re.sub(r'\$[^$]*\$', '', text)
        # 移除HTML标签
        cleaned = re.sub(r'<[^>]+>', '', cleaned)
        # 查找模式：字母 空格 数字 空格 字母 空格 数字（如 Na SO 2 4）
        # 或者：字母 空格 数字（如 Na 2）
        if re.search(r'[A-Z][a-z]?\s+\d+\s+[A-Z]', cleaned) or re.search(r'[A-Z][a-z]?\s+\d+$', cleaned.strip()):
            year = q['year']
            qnum = q.get('yearQnum')
            print(f"  {year}-{qnum} {field}: {text[:100]}")
            count1 += 1
            if count1 > 30:
                break
    if count1 > 30:
        break
print(f"共发现 {count1} 个（显示前30个）")
print()

# 问题2：离子符号未被$包裹（如 H^+, OH^-, Na^+）
print("【问题2】离子符号/化学式未被$包裹")
print("-" * 40)
count2 = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if not text:
            continue
        # 移除$中的内容
        cleaned = re.sub(r'\$[^$]*\$', '', text)
        # 查找 H^+, OH^-, Na^+, SO4^2- 等模式
        if re.search(r'[A-Z][a-z]?\^[+-]', cleaned) or re.search(r'[A-Z][a-z]?\^\{\d+[+-]\}', cleaned):
            year = q['year']
            qnum = q.get('yearQnum')
            print(f"  {year}-{qnum} {field}: {text[:100]}")
            count2 += 1
            if count2 > 30:
                break
    if count2 > 30:
        break
print(f"共发现 {count2} 个（显示前30个）")
print()

# 问题3：选项中只有离子符号（如 A: H^+, B: OH^-）
print("【问题3】选项中只有简单离子符号")
print("-" * 40)
count3 = 0
for q in questions:
    for field in ['A', 'B', 'C', 'D']:
        text = q.get(field, '').strip()
        if not text:
            continue
        # 选项内容只有离子符号或化学式
        if re.match(r'^[A-Z][a-z]?\^[+-]$', text) or re.match(r'^[A-Z][a-z]?\^\{\d+[+-]\}$', text):
            year = q['year']
            qnum = q.get('yearQnum')
            print(f"  {year}-{qnum} {field}: {text}")
            count3 += 1
print(f"共发现 {count3} 个")
print()

# 问题4：题干末尾有单独的数字行（下标残留）
print("【问题4】题干/选项末尾有单独的数字（下标残留）")
print("-" * 40)
count4 = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if not text:
            continue
        # 移除$中的内容
        cleaned = re.sub(r'\$[^$]*\$', '', text)
        # 末尾有单独的数字（可能是下标残留）
        if re.search(r'\s+\d+\s*$', cleaned.strip()) and len(cleaned.strip()) > 10:
            year = q['year']
            qnum = q.get('yearQnum')
            print(f"  {year}-{qnum} {field}: {text[-50:]}")
            count4 += 1
            if count4 > 30:
                break
    if count4 > 30:
        break
print(f"共发现 {count4} 个（显示前30个）")
print()

print("扫描完成")
