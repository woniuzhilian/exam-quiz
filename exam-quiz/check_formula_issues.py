import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print("=" * 80)
print("公式格式问题全面检查")
print("=" * 80)

# 1. 检查$...$中缺少空格的问题
print("\n1. 公式中缺少空格的问题:")
issues = []
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        # 检查\int后面缺少空格
        if re.search(r'\\int[a-zA-Z]', text):
            issues.append((q['year'], q.get('yearQnum', q['id']), field, '\\int后缺少空格'))
        # 检查\frac后面缺少空格
        if re.search(r'\\frac[^ {]', text):
            issues.append((q['year'], q.get('yearQnum', q['id']), field, '\\frac后缺少空格'))
        # 检查\partial后面缺少空格
        if re.search(r'\\partial[a-zA-Z]', text):
            issues.append((q['year'], q.get('yearQnum', q['id']), field, '\\partial后缺少空格'))
        # 检查\sin, \cos, \tan后面缺少空格
        for func in ['sin', 'cos', 'tan', 'ln', 'log', 'exp']:
            if re.search(r'\\' + func + r'[a-zA-Z]', text):
                issues.append((q['year'], q.get('yearQnum', q['id']), field, f'\\{func}后缺少空格'))

if issues:
    print(f"  发现 {len(issues)} 个问题:")
    for year, qnum, field, issue in issues[:20]:
        print(f"    {year}-{qnum} ({field}): {issue}")
    if len(issues) > 20:
        print(f"    ... 还有 {len(issues) - 20} 个问题")
else:
    print("  未发现问题")

# 2. 检查上标下标丢失（如e2x应该是e^{2x}）
print("\n2. 上标下标丢失检查:")
superscript_issues = []
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text or '$' not in text:
            continue
        # 检查e后面直接跟数字
        if re.search(r'e\d', text):
            superscript_issues.append((q['year'], q.get('yearQnum', q['id']), field, 'e后直接跟数字，可能缺少上标'))
        # 检查x后面直接跟数字
        if re.search(r'[a-zA-Z]\d(?!\d)', text):
            # 排除一些常见情况
            if not re.search(r'(alpha|beta|gamma|delta|pi|sigma|tau|phi|omega|theta|lambda|mu|nu|xi|rho|epsilon|zeta|eta|chi|psi|Gamma|Theta|Lambda|Xi|Pi|Sigma|Phi|Psi|Omega|sqrt|frac|int|sum|prod|partial|nabla|infty|leq|geq|neq|approx|equiv|pm|times|div|angle|perp|parallel|because|therefore|cos|sin|tan|ln|log|exp)\d', text):
                superscript_issues.append((q['year'], q.get('yearQnum', q['id']), field, '变量后直接跟数字，可能缺少上标/下标'))

if superscript_issues:
    print(f"  发现 {len(superscript_issues)} 个问题:")
    for year, qnum, field, issue in superscript_issues[:20]:
        print(f"    {year}-{qnum} ({field}): {issue}")
    if len(superscript_issues) > 20:
        print(f"    ... 还有 {len(superscript_issues) - 20} 个问题")
else:
    print("  未发现问题")

# 3. 检查乱码字符
print("\n3. 乱码字符检查:")
garbage_issues = []
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        # 检查常见的乱码模式
        if re.search(r'[�□■●○◇◆★☆※]', text):
            garbage_issues.append((q['year'], q.get('yearQnum', q['id']), field, '包含乱码字符'))
        # 检查连续的特殊字符
        if re.search(r'[\\][a-zA-Z]{2,}[\\][a-zA-Z]{2,}', text):
            # 可能是公式格式问题
            pass

if garbage_issues:
    print(f"  发现 {len(garbage_issues)} 个问题:")
    for year, qnum, field, issue in garbage_issues[:20]:
        print(f"    {year}-{qnum} ({field}): {issue}")
else:
    print("  未发现问题")

# 4. 检查选项内容缺失
print("\n4. 选项内容缺失检查:")
option_issues = []
for q in questions:
    for field in ['A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if not text:
            # 排除选项配图合并的情况
            if q.get('A') and '<img' in q.get('A', ''):
                continue
            option_issues.append((q['year'], q.get('yearQnum', q['id']), field, '选项为空'))
        elif text in ['选项A', '选项B', '选项C', '选项D', 'A', 'B', 'C', 'D']:
            option_issues.append((q['year'], q.get('yearQnum', q['id']), field, f'选项内容异常: {text}'))

if option_issues:
    print(f"  发现 {len(option_issues)} 个问题:")
    for year, qnum, field, issue in option_issues[:20]:
        print(f"    {year}-{qnum} ({field}): {issue}")
else:
    print("  未发现问题")

# 5. 检查题号重复
print("\n5. 题号重复检查:")
for big_subject in ['公共基础', '专业基础']:
    subject_questions = [q for q in questions if q['bigSubject'] == big_subject]
    years = sorted(set(q['year'] for q in subject_questions))
    for year in years:
        year_questions = [q for q in subject_questions if q['year'] == year]
        qnums = [q.get('yearQnum', 0) for q in year_questions]
        duplicates = [qnum for qnum in set(qnums) if qnums.count(qnum) > 1]
        if duplicates:
            print(f"  {big_subject} {year}: 重复题号 {duplicates}")

print("\n" + "=" * 80)
print("检查完成")
print("=" * 80)
