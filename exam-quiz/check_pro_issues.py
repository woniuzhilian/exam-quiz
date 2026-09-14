import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 筛选专业基础
pro = [q for q in questions if q['bigSubject'] == '专业基础']
print(f"专业基础总题数: {len(pro)}")

# 按年份分组
years = {}
for q in pro:
    year = q['year']
    if year not in years:
        years[year] = []
    years[year].append(q)

print("\n=== 1. 题号问题检查 ===")
for year in sorted(years.keys()):
    qs = sorted(years[year], key=lambda x: x.get('yearQnum', 0))
    qnums = [q.get('yearQnum', 0) for q in qs]
    expected = list(range(1, len(qs)+1))
    missing = [n for n in expected if n not in qnums]
    extra = [n for n in qnums if n > len(qs)]
    if missing or extra:
        print(f"  {year}年({len(qs)}题): 缺少{missing}, 超出{extra}")
    else:
        print(f"  {year}年({len(qs)}题): 正常")

print("\n=== 2. 公式LaTeX问题检查 ===")
formula_issues = []
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        # 检查$是否配对
        dollar_count = text.count('$')
        if dollar_count % 2 != 0:
            formula_issues.append(f"{q['year']}-{q.get('yearQnum')} {field}: $不配对({dollar_count}个)")
        # 检查未包裹的LaTeX命令
        latex_cmds = re.findall(r'\\[a-zA-Z]+', text)
        for cmd in latex_cmds:
            # 检查是否在$...$内
            idx = text.find(cmd)
            before = text[:idx]
            if before.count('$') % 2 == 0:
                formula_issues.append(f"{q['year']}-{q.get('yearQnum')} {field}: 命令{cmd}未在$...$内")
                break

print(f"  发现 {len(formula_issues)} 个公式问题")
for issue in formula_issues[:20]:
    print(f"    {issue}")

print("\n=== 3. 图片问题检查 ===")
image_issues = []
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        # 检查"见PDF"或"见本题配图"等标记
        if '见PDF' in text or '见本题配图' in text or 'PDF第' in text:
            image_issues.append(f"{q['year']}-{q.get('yearQnum')} {field}: 包含图片标记")
        # 检查img标签
        if '<img' in text:
            # 检查src是否有效
            src_match = re.search(r'src="([^"]+)"', text)
            if src_match:
                src = src_match.group(1)
                if not src.startswith('/images/') and not src.startswith('./images/'):
                    image_issues.append(f"{q['year']}-{q.get('yearQnum')} {field}: img路径异常{src}")

print(f"  发现 {len(image_issues)} 个图片问题")
for issue in image_issues[:20]:
    print(f"    {issue}")

print("\n=== 4. 空字段检查 ===")
empty_issues = []
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'answer', 'analysis']:
        if not q.get(field, '').strip():
            empty_issues.append(f"{q['year']}-{q.get('yearQnum')} {field}为空")

print(f"  发现 {len(empty_issues)} 个空字段")
for issue in empty_issues[:20]:
    print(f"    {issue}")

print("\n=== 5. answer字段检查 ===")
answer_issues = []
for q in pro:
    ans = q.get('answer', '')
    if ans not in ['A', 'B', 'C', 'D']:
        answer_issues.append(f"{q['year']}-{q.get('yearQnum')}: answer={ans}")

print(f"  发现 {len(answer_issues)} 个无效answer")
for issue in answer_issues[:20]:
    print(f"    {issue}")

print("\n=== 6. 特殊符号问题检查 ===")
special_issues = []
# Unicode数学符号
unicode_math = {
    'α': '\\alpha', 'β': '\\beta', 'γ': '\\gamma', 'δ': '\\delta',
    'ε': '\\epsilon', 'θ': '\\theta', 'λ': '\\lambda', 'μ': '\\mu',
    'π': '\\pi', 'ρ': '\\rho', 'σ': '\\sigma', 'φ': '\\phi',
    'ω': '\\omega', 'Δ': '\\Delta', 'Σ': '\\Sigma', 'Ω': '\\Omega',
    '≤': '\\leq', '≥': '\\geq', '≠': '\\neq', '≈': '\\approx',
    '√': '\\sqrt', '∞': '\\infty', '∫': '\\int', '∑': '\\sum',
    '×': '\\times', '÷': '\\div', '±': '\\pm',
}

for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        for char, latex in unicode_math.items():
            if char in text:
                # 检查是否在$...$内
                idx = text.find(char)
                before = text[:idx]
                if before.count('$') % 2 == 0:
                    special_issues.append(f"{q['year']}-{q.get('yearQnum')} {field}: Unicode符号{char}未转LaTeX")
                    break

print(f"  发现 {len(special_issues)} 个特殊符号问题")
for issue in special_issues[:30]:
    print(f"    {issue}")

# 保存问题清单
issues = {
    'formula_issues': formula_issues,
    'image_issues': image_issues,
    'empty_issues': empty_issues,
    'answer_issues': answer_issues,
    'special_issues': special_issues,
}

with open(r'D:\应用程序开发\刷题\exam-quiz\pro_issues.json', 'w', encoding='utf-8') as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("\n问题清单已保存到 pro_issues.json")
