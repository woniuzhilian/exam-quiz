import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离公共基础
public = [q for q in questions if q['bigSubject'] == '公共基础']
print(f"公共基础总题数: {len(public)}")

# 1. 检查题号问题
print("\n=== 1. 题号问题检查 ===")
year_qnums = {}
for q in public:
    year = q['year']
    qnum = q.get('yearQnum', q['id'])
    if year not in year_qnums:
        year_qnums[year] = []
    year_qnums[year].append(qnum)

for year in sorted(year_qnums.keys()):
    qnums = sorted(year_qnums[year])
    expected = list(range(1, 121))  # 每年120题
    missing = [x for x in expected if x not in qnums]
    duplicates = [x for x in qnums if qnums.count(x) > 1]
    over_120 = [x for x in qnums if x > 120]
    
    issues = []
    if missing:
        issues.append(f"缺少: {missing}")
    if duplicates:
        issues.append(f"重复: {list(set(duplicates))}")
    if over_120:
        issues.append(f"超过120: {over_120}")
    
    if issues:
        print(f"  {year}年({len(qnums)}题): {', '.join(issues)}")
    else:
        print(f"  {year}年({len(qnums)}题): 正常")

# 2. 检查公式问题
print("\n=== 2. 公式LaTeX问题检查 ===")
formula_issues = []
for q in public:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        
        # 检查$符号配对
        dollar_count = text.count('$')
        if dollar_count % 2 != 0:
            formula_issues.append((q['year'], q.get('yearQnum', ''), field, '$符号不配对'))
        
        # 检查未包裹的LaTeX命令
        latex_cmds = ['\\frac', '\\sqrt', '\\sum', '\\int', '\\lim', '\\alpha', '\\beta', 
                      '\\gamma', '\\delta', '\\theta', '\\pi', '\\omega', '\\mu', '\\sigma',
                      '\\lambda', '\\rho', '\\tau', '\\phi', '\\varphi', '\\epsilon',
                      '\\times', '\\div', '\\pm', '\\leq', '\\geq', '\\neq', '\\approx',
                      '\\cdot', '\\circ', '\\degree', '\\text', '\\mathrm', '\\mathbf']
        
        for cmd in latex_cmds:
            # 找到命令位置
            pos = 0
            while True:
                pos = text.find(cmd, pos)
                if pos == -1:
                    break
                # 检查是否在$...$内
                before = text[:pos]
                dollar_before = before.count('$')
                if dollar_before % 2 == 0:
                    # 不在公式内
                    formula_issues.append((q['year'], q.get('yearQnum', ''), field, f'{cmd}未包裹在$内'))
                    break
                pos += 1

print(f"  发现 {len(formula_issues)} 个公式问题")
for issue in formula_issues[:20]:
    print(f"    {issue[0]}-{issue[1]} {issue[2]}: {issue[3]}")
if len(formula_issues) > 20:
    print(f"    ... 还有 {len(formula_issues) - 20} 个")

# 3. 检查图片问题
print("\n=== 3. 图片问题检查 ===")
image_issues = []
for q in public:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        
        # 检查"见PDF"标记（应该已替换为img标签）
        if '见PDF' in text or '见pdf' in text or 'PDF第' in text:
            image_issues.append((q['year'], q.get('yearQnum', ''), field, '仍有PDF引用标记'))
        
        # 检查img标签
        img_tags = re.findall(r'<img[^>]*>', text)
        for img in img_tags:
            # 检查src属性
            if 'src=' not in img:
                image_issues.append((q['year'], q.get('yearQnum', ''), field, 'img标签缺少src'))
            elif 'src=""' in img or "src=''" in img:
                image_issues.append((q['year'], q.get('yearQnum', ''), field, 'img标签src为空'))

print(f"  发现 {len(image_issues)} 个图片问题")
for issue in image_issues[:20]:
    print(f"    {issue[0]}-{issue[1]} {issue[2]}: {issue[3]}")
if len(image_issues) > 20:
    print(f"    ... 还有 {len(image_issues) - 20} 个")

# 4. 检查空字段
print("\n=== 4. 空字段检查 ===")
empty_fields = []
for q in public:
    for field in ['question', 'A', 'B', 'C', 'D', 'answer', 'analysis']:
        if not q.get(field, '').strip():
            empty_fields.append((q['year'], q.get('yearQnum', ''), field))

print(f"  发现 {len(empty_fields)} 个空字段")
for issue in empty_fields[:20]:
    print(f"    {issue[0]}-{issue[1]}: {issue[2]}为空")
if len(empty_fields) > 20:
    print(f"    ... 还有 {len(empty_fields) - 20} 个")

# 5. 检查answer字段
print("\n=== 5. answer字段检查 ===")
invalid_answers = []
for q in public:
    ans = q.get('answer', '')
    if ans not in ['A', 'B', 'C', 'D']:
        invalid_answers.append((q['year'], q.get('yearQnum', ''), ans))

print(f"  发现 {len(invalid_answers)} 个无效answer")
for issue in invalid_answers[:10]:
    print(f"    {issue[0]}-{issue[1]}: answer='{issue[2]}'")

# 6. 检查特殊符号问题
print("\n=== 6. 特殊符号问题检查 ===")
symbol_issues = []
for q in public:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        
        # 检查乱码字符
        if '\ufffd' in text:
            symbol_issues.append((q['year'], q.get('yearQnum', ''), field, '有乱码字符'))
        
        # 检查未转换的Unicode数学符号（应该转为LaTeX）
        unicode_math = ['√', '∑', '∫', '∞', '≠', '≤', '≥', '≈', '±', '×', '÷',
                        'α', 'β', 'γ', 'δ', 'θ', 'π', 'ω', 'μ', 'σ', 'λ', 'ρ', 'τ', 'φ',
                        '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩']
        for sym in unicode_math:
            if sym in text:
                # 检查是否在$内
                pos = text.find(sym)
                before = text[:pos]
                if before.count('$') % 2 == 0:
                    symbol_issues.append((q['year'], q.get('yearQnum', ''), field, f'Unicode符号{sym}未转LaTeX'))
                    break

print(f"  发现 {len(symbol_issues)} 个特殊符号问题")
for issue in symbol_issues[:20]:
    print(f"    {issue[0]}-{issue[1]} {issue[2]}: {issue[3]}")
if len(symbol_issues) > 20:
    print(f"    ... 还有 {len(symbol_issues) - 20} 个")

# 保存所有问题到文件
all_issues = {
    'formula_issues': formula_issues,
    'image_issues': image_issues,
    'empty_fields': empty_fields,
    'invalid_answers': invalid_answers,
    'symbol_issues': symbol_issues,
}

with open(r'D:\应用程序开发\刷题\exam-quiz\public_issues.json', 'w', encoding='utf-8') as f:
    json.dump(all_issues, f, ensure_ascii=False, indent=2)

print("\n问题清单已保存到 public_issues.json")
