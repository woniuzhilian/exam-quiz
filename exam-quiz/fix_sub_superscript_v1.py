import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

def wrap_ions_in_dollar(text):
    """将未被$包裹的离子符号用$包裹"""
    if not text:
        return text

    # 模式1：简单离子 H^+, Na^+, K^+, OH^-, Cl^- 等
    # 只替换不在$中的
    parts = re.split(r'(\$[^$]*\$)', text)
    result = []
    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
        else:
            # 简单离子：元素符号^+ 或 元素符号^-
            part = re.sub(r'\b([A-Z][a-z]?)\^([+-])\b', r'$\1^\2$', part)
            # 复杂离子：元素符号^{数字+} 或 元素符号^{数字-}
            part = re.sub(r'\b([A-Z][a-z]?)\^\{(\d+[+-])\}', r'$\1^{\2}$', part)
            # 电对：Zn^{2+}/Zn 这种
            part = re.sub(r'\b([A-Z][a-z]?)\^\{(\d+[+-])\}/([A-Z][a-z]?)', r'$\1^{\2}/\3$', part)
            result.append(part)

    return ''.join(result)

def fix_chemical_formula_with_spaces(text):
    """修复化学式中数字和字母分开的情况"""
    if not text:
        return text

    # 常见的错误模式：
    # Na SO 2 4 -> Na2SO4
    # Ba SO 4 -> BaSO4
    # H 2 O -> H2O
    # N 2 -> N2

    # 只处理不在$中的内容
    parts = re.split(r'(\$[^$]*\$)', text)
    result = []

    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
            continue

        # 模式：Na2SO4, NaCl, H2O, CO2, SO2, NH3, BaSO4, BaCl2 等
        # 先尝试匹配已知化学式
        known_formulas = [
            ('Na SO 2 4', 'Na2SO4'),
            ('Na 2 SO 4', 'Na2SO4'),
            ('Ba SO 4', 'BaSO4'),
            ('Ba Cl 2', 'BaCl2'),
            ('H 2 O', 'H2O'),
            ('H 2 O 2', 'H2O2'),
            ('CO 2', 'CO2'),
            ('SO 2', 'SO2'),
            ('SO 3', 'SO3'),
            ('NO 2', 'NO2'),
            ('NH 3', 'NH3'),
            ('NH 4', 'NH4'),
            ('HCl', 'HCl'),
            ('NaCl', 'NaCl'),
            ('NaOH', 'NaOH'),
            ('KOH', 'KOH'),
            ('Ca Cl 2', 'CaCl2'),
            ('Ca CO 3', 'CaCO3'),
            ('Ag Cl', 'AgCl'),
            ('Cu SO 4', 'CuSO4'),
            ('Fe Cl 3', 'FeCl3'),
            ('Fe Cl 2', 'FeCl2'),
            ('Al 2 O 3', 'Al2O3'),
            ('Mg Cl 2', 'MgCl2'),
            ('Zn SO 4', 'ZnSO4'),
            ('Na 2 CO 3', 'Na2CO3'),
            ('Na H CO 3', 'NaHCO3'),
            ('Na 2 SO 4', 'Na2SO4'),
            ('K 2 SO 4', 'K2SO4'),
            ('K NO 3', 'KNO3'),
            ('CH 4', 'CH4'),
            ('C 2 H 6', 'C2H6'),
            ('C 2 H 4', 'C2H4'),
            ('C 2 H 2', 'C2H2'),
            ('C 6 H 6', 'C6H6'),
            ('HOAc', 'HOAc'),
            ('NaOAc', 'NaOAc'),
            ('NH 4 Cl', 'NH4Cl'),
            ('NH 4 NO 3', 'NH4NO3'),
            ('(NH 4) 2 SO 4', '(NH4)2SO4'),
            ('Na 3 PO 4', 'Na3PO4'),
            ('Ca(OH) 2', 'Ca(OH)2'),
            ('Fe(OH) 3', 'Fe(OH)3'),
            ('Cu(OH) 2', 'Cu(OH)2'),
            ('PCl 3', 'PCl3'),
            ('PCl 5', 'PCl5'),
            ('CCl 4', 'CCl4'),
            ('SiCl 4', 'SiCl4'),
            ('BF 3', 'BF3'),
            ('SF 6', 'SF6'),
            ('N 2', 'N2'),
            ('O 2', 'O2'),
            ('H 2', 'H2'),
            ('Cl 2', 'Cl2'),
            ('Br 2', 'Br2'),
            ('I 2', 'I2'),
            ('O 3', 'O3'),
            ('CO', 'CO'),
            ('NO', 'NO'),
            ('H 2 S', 'H2S'),
            ('PH 3', 'PH3'),
            ('HF', 'HF'),
            ('HBr', 'HBr'),
            ('HI', 'HI'),
        ]

        for wrong, correct in known_formulas:
            if wrong in part:
                part = part.replace(wrong, correct)

        result.append(part)

    return ''.join(result)

def fix_trailing_subscripts(text):
    """修复末尾的下标残留数字"""
    if not text:
        return text

    # 只处理不在$中的内容
    parts = re.split(r'(\$[^$]*\$)', text)
    result = []

    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
            continue

        # 模式：化学式后面跟单独的数字（下标）
        # 如 "PCl 分子空间几何构型... 3" -> "PCl3 分子空间几何构型..."
        # 如 "电解Na SO 水溶液时... 2 4" -> 已经被上面的函数处理

        # 处理 "PCl ... 3" 这种情况
        # 这个比较复杂，先不自动处理，避免误删

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
        fixed = wrap_ions_in_dollar(fixed)
        fixed = fix_chemical_formula_with_spaces(fixed)
        fixed = fix_trailing_subscripts(fixed)

        if fixed != original:
            q[field] = fixed
            fixed_count += 1
            print(f'修复 {q["year"]}-{q.get("yearQnum")} {field}')

print(f'\n共修复 {fixed_count} 个字段')

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")
