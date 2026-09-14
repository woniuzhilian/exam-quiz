import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 化学相关小科目
chem_subjects = ['溶液', '氧化还原与电化学', '物质结构', '反应速率与化学平衡', '有机化学', '化学']

def is_chem_question(q):
    return any(s in q.get('smallSubject', '') for s in chem_subjects)

def fix_chem_formulas_in_text(text):
    """修复化学文本中的化学式"""
    if not text:
        return text

    # 只处理不在$中的内容
    parts = re.split(r'(\$[^$]*\$)', text)
    result = []

    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
            continue

        # 1. 修复化学式：大写字母+小写字母?+数字（如BaSO4, BaCl2, NH3, H2O）
        # 但要排除变量（如V1, R1, F1等）
        # 化学元素列表
        elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
                    'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
                    'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
                    'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
                    'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
                    'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
                    'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
                    'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
                    'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
                    'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
                    'Md', 'No', 'Lr']

        # 按长度降序排列
        elements = sorted(elements, key=len, reverse=True)

        # 匹配化学式：元素符号+数字
        for elem in elements:
            # 元素后面跟数字（下标）
            pattern = re.escape(elem) + r'(\d+)'
            def replace_func(m):
                return elem + '_{' + m.group(1) + '}'
            part = re.sub(pattern, replace_func, part)

        # 2. 修复离子符号：元素+数字+; -> 元素^{数字-} 或 元素+数字+: -> 元素^{数字+}
        # SO4 2; -> SO_4^{2-}
        part = re.sub(r'([A-Z][a-z]?\s*\d*)\s*(\d+);', r'\1^{\2-}', part)
        # Ag: -> Ag^+
        part = re.sub(r'([A-Z][a-z]?):', r'\1^+', part)
        # Cl; -> Cl^-
        part = re.sub(r'([A-Z][a-z]?);', r'\1^-', part)

        # 3. 修复单位上标：m2/s -> m^2/s, dm-3 -> dm^{-3}
        part = re.sub(r'\b([a-zA-Z]+)(\d+)/', r'\1^{\2}/', part)

        result.append(part)

    return ''.join(result)

def fix_unit_superscripts(text):
    """修复单位上标（所有题目）"""
    if not text:
        return text

    parts = re.split(r'(\$[^$]*\$)', text)
    result = []

    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
            continue

        # m2/s -> m^2/s, m3/s -> m^3/s
        part = re.sub(r'\b(m|cm|mm|km|dm|nm|um|μm)(\d+)/s\b', r'\1^{\2}/s', part)
        # mol/L -> mol/L (不需要改)
        # kN/m2 -> kN/m^2
        part = re.sub(r'/(m|cm|mm|dm)(\d+)\b', r'/\1^{\2}', part)

        result.append(part)

    return ''.join(result)

# 修复所有题目
fixed_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        original = q.get(field, '')
        if not original:
            continue

        fixed = original

        # 化学题目特殊处理
        if is_chem_question(q):
            fixed = fix_chem_formulas_in_text(fixed)

        # 所有题目修复单位上标
        fixed = fix_unit_superscripts(fixed)

        if fixed != original:
            q[field] = fixed
            fixed_count += 1

print(f"修复了 {fixed_count} 个字段")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")
