import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"总题目数: {len(questions)}")
print()

# ========== 检查1：化学式下标问题（字母+数字但没有下标标记） ==========
print("=" * 60)
print("检查1：化学式下标问题（如NH3, H2O, CO2等未用下标）")
print("=" * 60)

# 常见化学式模式：大写字母+小写字母?+数字
chemical_pattern = r'\b[A-Z][a-z]?\d+'
issues1 = []
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        # 移除$...$中的内容
        cleaned = re.sub(r'\$[^$]*\$', '', text)
        # 移除HTML标签
        cleaned = re.sub(r'<[^>]+>', '', cleaned)
        matches = re.findall(chemical_pattern, cleaned)
        if matches:
            issues1.append((q['year'], q.get('yearQnum'), field, matches[:5], text[:80]))

print(f"发现 {len(issues1)} 个字段有化学式下标问题")
for year, qnum, field, matches, preview in issues1[:30]:
    print(f"  {year}-{qnum} {field}: {matches} | {preview}")
if len(issues1) > 30:
    print(f"  ... 还有 {len(issues1)-30} 个")

print()

# ========== 检查2：上标问题（数字;数字 模式） ==========
print("=" * 60)
print("检查2：上标问题（如10;5, dm;3等模式）")
print("=" * 60)

superscript_pattern = r'[a-zA-Z0-9];-?\d'
issues2 = []
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        cleaned = re.sub(r'\$[^$]*\$', '', text)
        cleaned = re.sub(r'<[^>]+>', '', cleaned)
        matches = re.findall(superscript_pattern, cleaned)
        if matches:
            issues2.append((q['year'], q.get('yearQnum'), field, matches[:5], text[:80]))

print(f"发现 {len(issues2)} 个字段有上标问题")
for year, qnum, field, matches, preview in issues2[:30]:
    print(f"  {year}-{qnum} {field}: {matches} | {preview}")
if len(issues2) > 30:
    print(f"  ... 还有 {len(issues2)-30} 个")

print()

# ========== 检查3：∥平行符号问题 ==========
print("=" * 60)
print("检查3：平行符号∥问题")
print("=" * 60)

issues3 = []
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        if '∥' in text or '//' in text or '\parallel' in text:
            issues3.append((q['year'], q.get('yearQnum'), field, text[:100]))

print(f"发现 {len(issues3)} 个字段有平行符号")
for year, qnum, field, preview in issues3[:20]:
    print(f"  {year}-{qnum} {field}: {preview}")
if len(issues3) > 20:
    print(f"  ... 还有 {len(issues3)-20} 个")

print()

# ========== 检查4：下划线问题 ==========
print("=" * 60)
print("检查4：下划线问题")
print("=" * 60)

issues4 = []
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        # 查找不在$中的下划线
        cleaned = re.sub(r'\$[^$]*\$', '', text)
        if '_' in cleaned:
            issues4.append((q['year'], q.get('yearQnum'), field, text[:100]))

print(f"发现 {len(issues4)} 个字段有下划线")
for year, qnum, field, preview in issues4[:20]:
    print(f"  {year}-{qnum} {field}: {preview}")
if len(issues4) > 20:
    print(f"  ... 还有 {len(issues4)-20} 个")

print()

# ========== 检查5：化学科目题目专项检查 ==========
print("=" * 60)
print("检查5：化学/溶液科目题目专项")
print("=" * 60)

chem_subjects = ['溶液', '化学反应', '化学', '有机化学', '物质结构']
issues5 = []
for q in questions:
    if any(s in q.get('smallSubject', '') for s in chem_subjects):
        for field in ['question', 'A', 'B', 'C', 'D']:
            text = q.get(field, '')
            if not text:
                continue
            # 检查是否有未被$包裹的化学式
            cleaned = re.sub(r'\$[^$]*\$', '', text)
            cleaned = re.sub(r'<[^>]+>', '', cleaned)
            if re.search(r'[A-Z][a-z]?\d', cleaned) or re.search(r';-?\d', cleaned):
                issues5.append((q['year'], q.get('yearQnum'), field, q['smallSubject'], text[:100]))

print(f"发现 {len(issues5)} 个化学题目有问题")
for year, qnum, field, subj, preview in issues5[:30]:
    print(f"  {year}-{qnum} [{subj}] {field}: {preview}")
if len(issues5) > 30:
    print(f"  ... 还有 {len(issues5)-30} 个")

print()
print("检查完成")
