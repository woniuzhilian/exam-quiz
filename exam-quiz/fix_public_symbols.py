import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离公共基础
public = [q for q in questions if q['bigSubject'] == '公共基础']

# 修复特殊符号问题
def fix_symbols(text):
    """修复Unicode符号未包裹在$内的问题"""
    if not text:
        return text
    
    # 希腊字母映射
    greek_map = {
        'α': '\\alpha', 'β': '\\beta', 'γ': '\\gamma', 'δ': '\\delta',
        'ε': '\\epsilon', 'θ': '\\theta', 'λ': '\\lambda', 'μ': '\\mu',
        'π': '\\pi', 'ρ': '\\rho', 'σ': '\\sigma', 'τ': '\\tau',
        'φ': '\\phi', 'ω': '\\omega', 'η': '\\eta', 'ξ': '\\xi',
        'ζ': '\\zeta', 'ν': '\\nu', 'κ': '\\kappa', 'ι': '\\iota',
    }
    
    # 数学符号映射
    math_map = {
        '√': '\\sqrt{}', '∑': '\\sum', '∫': '\\int', '∞': '\\infty',
        '≠': '\\neq', '≤': '\\leq', '≥': '\\geq', '≈': '\\approx',
        '±': '\\pm', '×': '\\times', '÷': '\\div',
    }
    
    # 找到所有不在$内的Unicode符号并替换
    result = []
    i = 0
    in_math = False
    
    while i < len(text):
        if text[i] == '$':
            in_math = not in_math
            result.append(text[i])
            i += 1
            continue
        
        if not in_math:
            # 检查是否是希腊字母或数学符号
            char = text[i]
            if char in greek_map:
                # 检查前后是否有$的迹象
                # 直接替换为$...$包裹的LaTeX
                result.append(f'${greek_map[char]}$')
                i += 1
                continue
            elif char in math_map:
                result.append(f'${math_map[char]}$')
                i += 1
                continue
        
        result.append(text[i])
        i += 1
    
    return ''.join(result)

# 需要修复的题目
fix_list = [
    ('2013', 61, 'D'),
    ('2017', 12, 'analysis'),
    ('2017', 24, 'question'),
    ('2019', 9, 'question'),
    ('2019', 14, 'analysis'),
    ('2024', 9, 'analysis'),
    ('2024', 10, 'question'),
    ('2024', 73, 'question'),
]

fixed_count = 0
for year, qnum, field in fix_list:
    q = next((x for x in public if x['year'] == year and x.get('yearQnum') == qnum), None)
    if q:
        original = q.get(field, '')
        fixed = fix_symbols(original)
        if original != fixed:
            q[field] = fixed
            fixed_count += 1
            print(f"修复: {year}-{qnum} {field}")

# 2018-81的①②是序号，不需要转LaTeX，保持原样

print(f"\n共修复 {fixed_count} 个字段")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("题库已更新")
