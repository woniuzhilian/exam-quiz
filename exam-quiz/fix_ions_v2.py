import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

def fix_simple_ions(text):
    """修复简单离子符号的$包裹问题"""
    if not text:
        return text

    # 情况1：整个选项就是离子符号，如 "H^+" -> "$H^+$"
    if re.match(r'^[A-Z][a-z]?\^[+-]$', text.strip()):
        return '$' + text.strip() + '$'

    # 情况2：$包裹位置不对，如 "OH$^{-}$" -> "$OH^-$"
    text = re.sub(r'\b([A-Z][a-z]?)\$\^\{([+-])\}\$', r'$\1^\2$', text)

    # 情况3：离子符号未被$包裹，如 "H^+" -> "$H^+$"
    # 但要避免已经在$中的
    parts = re.split(r'(\$[^$]*\$)', text)
    result = []
    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
        else:
            # 简单离子：H^+, Na^+, K^+, OH^-, Cl^- 等
            part = re.sub(r'\b([A-Z][a-z]?)\^([+-])\b', r'$\1^\2$', part)
            # 复杂离子：SO4^2-, NO3^- 等（如果有）
            part = re.sub(r'\b([A-Z][a-z]?\d*)\^\{(\d+[+-])\}', r'$\1^{\2}$', part)
            result.append(part)

    return ''.join(result)

def fix_chemical_formula_trailing_numbers(text):
    """修复化学式中数字在末尾的情况"""
    if not text:
        return text

    # 常见模式：
    # "电解Na SO 水溶液时... 2 4" -> "电解Na2SO4水溶液时..."
    # "PCl 分子空间几何构型... 3" -> "PCl3分子空间几何构型..."

    # 只处理不在$中的内容
    parts = re.split(r'(\$[^$]*\$)', text)
    result = []

    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
            continue

        # 模式1："Na SO ... 2 4" -> "Na2SO4"
        # 这个比较复杂，先处理已知的具体情况

        # PCl 3 -> PCl3
        part = re.sub(r'\bPCl\s+(\d+)\b', r'PCl\1', part)

        # H 2 O -> H2O (如果数字紧跟在后面)
        # 这个已经在之前的脚本中处理了

        result.append(part)

    return ''.join(result)

# 修复所有题目
fixed_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D']:
        original = q.get(field, '')
        if not original:
            continue

        fixed = original
        fixed = fix_simple_ions(fixed)
        fixed = fix_chemical_formula_trailing_numbers(fixed)

        if fixed != original:
            q[field] = fixed
            fixed_count += 1
            print(f'修复 {q["year"]}-{q.get("yearQnum")} {field}: {original[:50]} -> {fixed[:50]}')

print(f'\n共修复 {fixed_count} 个字段')

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")
