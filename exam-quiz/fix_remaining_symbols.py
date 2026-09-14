import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

def fix_false_ions(text):
    """修复被错误转换的离子符号（如R^{2+}应该是R2:）"""
    if not text:
        return text

    # 电路中的电阻比值 R1:R2 被错误转换成 R^{1+}R2
    # 模式：R^{数字+} 后面紧跟字母或数字
    text = re.sub(r'R\^\{(\d+)\+\}(?=[A-Za-z])', r'R\1:', text)

    return text

def fix_parallel_symbols(text):
    """修复平行符号：\parallel后面紧跟字母的情况"""
    if not text:
        return text

    # \parallelAg -> \parallel Ag
    text = re.sub(r'\\parallel([A-Za-z])', r'\\parallel \1', text)

    # 原电池符号中的 \parallel 应该在$中
    # 查找不在$中的 \parallel
    parts = re.split(r'(\$[^$]*\$)', text)
    result = []
    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
        else:
            if '\\parallel' in part:
                part = part.replace('\\parallel', '$\\parallel$')
            result.append(part)

    return ''.join(result)

def fix_remaining_chemicals(text):
    """修复剩余的化学式"""
    if not text:
        return text

    # Mn04 -> MnO_4
    text = text.replace('Mn04', '$MnO_4$')
    text = text.replace('Mn0;', '$MnO_4^{-}$')

    # A1(SO) -> Al2(SO4)3 (常见错误)
    text = text.replace('A1 (SO )', '$Al_2(SO_4)_3$')
    text = text.replace('A12(SO4)3', '$Al_2(SO_4)_3$')

    # Na0Ac -> NaOAc
    text = text.replace('Na0Ac', '$NaOAc$')

    # C5H11Cl -> C_5H_11Cl
    text = text.replace('C5H11Cl', '$C_5H_{11}Cl$')

    # Ca2+ -> Ca^{2+}（如果不在$中）
    parts = re.split(r'(\$[^$]*\$)', text)
    result = []
    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
        else:
            part = part.replace('Ca2+', '$Ca^{2+}$')
            result.append(part)

    return ''.join(result)

# 修复所有字段
fixed_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        original = q.get(field, '')
        if not original:
            continue

        fixed = original
        fixed = fix_false_ions(fixed)
        fixed = fix_parallel_symbols(fixed)
        fixed = fix_remaining_chemicals(fixed)

        if fixed != original:
            q[field] = fixed
            fixed_count += 1

print(f"修复了 {fixed_count} 个字段")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")
