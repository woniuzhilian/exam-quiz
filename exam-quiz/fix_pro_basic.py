import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离公共基础和专业基础
public = [q for q in questions if q['bigSubject'] == '公共基础']
pro = [q for q in questions if q['bigSubject'] == '专业基础']

# 1. 修复2024年题号：将17-60改为13-56
year_2024 = [q for q in pro if q['year'] == '2024']
year_2024_sorted = sorted(year_2024, key=lambda x: x.get('yearQnum', 0))

print("修复2024年题号:")
for q in year_2024_sorted:
    old_qnum = q.get('yearQnum', 0)
    if old_qnum >= 17:
        new_qnum = old_qnum - 4
        q['yearQnum'] = new_qnum
        print(f"  {old_qnum} -> {new_qnum}")

# 2. 自动转换特殊符号为LaTeX
unicode_math = {
    'α': '\\alpha', 'β': '\\beta', 'γ': '\\gamma', 'δ': '\\delta',
    'ε': '\\epsilon', 'θ': '\\theta', 'λ': '\\lambda', 'μ': '\\mu',
    'π': '\\pi', 'ρ': '\\rho', 'σ': '\\sigma', 'φ': '\\phi',
    'ω': '\\omega', 'Δ': '\\Delta', 'Σ': '\\Sigma', 'Ω': '\\Omega',
    '≤': '\\leq', '≥': '\\geq', '≠': '\\neq', '≈': '\\approx',
    '√': '\\sqrt', '∞': '\\infty', '∫': '\\int', '∑': '\\sum',
    '×': '\\times', '÷': '\\div', '±': '\\pm',
}

def convert_special_symbols(text):
    """将Unicode数学符号转换为LaTeX，并包裹在$...$中"""
    if not text:
        return text
    
    result = text
    for char, latex in unicode_math.items():
        if char in result:
            # 检查是否已经在$...$内
            # 简单处理：将符号替换为$latex$，但需要注意相邻符号的合并
            # 先替换为临时标记
            result = result.replace(char, f'${latex}$')
    
    # 合并相邻的$...$
    result = re.sub(r'\$\$([^$]+)\$\$', r'$\1$', result)
    result = re.sub(r'\$\\([a-zA-Z]+)\$\$\\([a-zA-Z]+)\$', r'$\\\1 \\2$', result)
    
    return result

print("\n转换特殊符号:")
count = 0
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        old_text = q.get(field, '')
        if not old_text:
            continue
        new_text = convert_special_symbols(old_text)
        if new_text != old_text:
            q[field] = new_text
            count += 1

print(f"  转换了 {count} 个字段")

# 重新排序专业基础
pro.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))

# 重新分配id
for i, q in enumerate(public):
    q['id'] = i + 1

pro_start = len(public) + 1
for i, q in enumerate(pro):
    q['id'] = pro_start + i

# 合并
final = public + pro

# 验证
print(f"\n公共基础题数: {len(public)}")
print(f"专业基础题数: {len(pro)}")
print(f"总题数: {len(final)}")

# 检查2024年题号
year_2024_new = [q for q in pro if q['year'] == '2024']
year_2024_new_sorted = sorted(year_2024_new, key=lambda x: x.get('yearQnum', 0))
qnums = [q.get('yearQnum') for q in year_2024_new_sorted]
print(f"\n2024年题号范围: {min(qnums)} - {max(qnums)}")
print(f"2024年题数: {len(year_2024_new)}")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print("\n题库已更新")
