import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 常见化学式列表（用于精确匹配）
chemical_formulas = [
    'H2O', 'H2O2', 'CO2', 'CO', 'SO2', 'SO3', 'NO2', 'NO', 'N2O',
    'NH3', 'NH4', 'HCl', 'H2SO4', 'HNO3', 'H3PO4', 'H2CO3',
    'NaCl', 'NaOH', 'KOH', 'CaCl2', 'CaCO3', 'CaSO4', 'BaSO4',
    'BaCl2', 'AgCl', 'AgNO3', 'CuSO4', 'CuCl2', 'FeCl3', 'FeCl2',
    'Fe2O3', 'Fe3O4', 'Al2O3', 'AlCl3', 'Al2(SO4)3', 'MgCl2',
    'MgSO4', 'ZnSO4', 'ZnCl2', 'Na2CO3', 'NaHCO3', 'Na2SO4',
    'K2SO4', 'KNO3', 'KMnO4', 'K2Cr2O7', 'CH4', 'C2H6', 'C3H8',
    'C2H4', 'C2H2', 'C6H6', 'C6H12O6', 'CH3COOH', 'CH3OH',
    'C2H5OH', 'HOAc', 'NaOAc', 'NH4Cl', 'NH4NO3', '(NH4)2SO4',
    'Na3PO4', 'Na2HPO4', 'NaH2PO4', 'Ca(OH)2', 'Ba(OH)2',
    'Fe(OH)3', 'Fe(OH)2', 'Cu(OH)2', 'Al(OH)3', 'Mg(OH)2',
    'Ag2O', 'CuO', 'Cu2O', 'ZnO', 'MnO2', 'SiO2', 'P2O5',
    'N2', 'O2', 'H2', 'Cl2', 'Br2', 'I2', 'F2', 'O3',
    'HF', 'HBr', 'HI', 'H2S', 'H2Se', 'PH3', 'AsH3',
    'Na2O', 'Na2O2', 'K2O', 'CaO', 'MgO', 'SrO', 'BaO',
    'Li2O', 'BeO', 'B2O3', 'BF3', 'BCl3', 'SiF4', 'SiCl4',
    'PF3', 'PF5', 'PCl3', 'PCl5', 'SF6', 'SF4', 'OF2',
    'ClO2', 'Cl2O', 'Cl2O7', 'N2O4', 'N2O5', 'NO3',
    'HNO2', 'H2SO3', 'H2S2O3', 'HClO', 'HClO2', 'HClO3',
    'HClO4', 'HBrO', 'HBrO3', 'HIO', 'HIO3', 'H3BO3',
    'H2SiO3', 'H4SiO4', 'H3AsO4', 'H3AsO3', 'H2C2O4',
    'KClO3', 'KClO4', 'NaClO', 'Ca(ClO)2', 'K2CrO4',
    'K2MnO4', 'MnSO4', 'FeSO4', 'Fe2(SO4)3', 'CoCl2',
    'NiSO4', 'CrCl3', 'Cr2(SO4)3', 'TiCl4', 'V2O5',
    'WO3', 'MoO3', 'UO2', 'ThO2', 'La2O3', 'CeO2',
    'Nd2O3', 'Sm2O3', 'Eu2O3', 'Gd2O3', 'Tb4O7',
    'Dy2O3', 'Ho2O3', 'Er2O3', 'Tm2O3', 'Yb2O3', 'Lu2O3',
    'Sc2O3', 'Y2O3', 'ZrO2', 'HfO2', 'Ta2O5', 'Nb2O5',
]

# 按长度降序排列，优先匹配长化学式
chemical_formulas = sorted(chemical_formulas, key=len, reverse=True)

def fix_superscripts(text):
    """修复上标问题：数字;数字 -> 数字^{数字}"""
    if not text:
        return text

    # 模式1：10;5 -> 10^{-5}, 10;-5 -> 10^{-5}
    text = re.sub(r'(\d+);(-?\d+)', r'\1^{\2}', text)

    # 模式2：dm;3 -> dm^{-3}, m;2 -> m^{-2}, L;1 -> L^{-1}
    text = re.sub(r'([a-zA-Z]);(-?\d+)', r'\1^{\2}', text)

    # 模式3：e;2x -> e^{2x}, e;-x -> e^{-x}
    text = re.sub(r'\be;(-?[a-zA-Z0-9]+)', r'e^{\1}', text)

    return text

def fix_chemical_formulas(text):
    """修复化学式下标"""
    if not text:
        return text

    # 只修复不在$中的化学式
    parts = re.split(r'(\$[^$]*\$)', text)
    result = []

    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
        else:
            # 替换已知化学式
            for formula in chemical_formulas:
                if formula in part:
                    # 将化学式转换为带下标的形式
                    subscript_formula = re.sub(r'(\d+)', r'_{\1}', formula)
                    part = part.replace(formula, '$' + subscript_formula + '$')
            result.append(part)

    return ''.join(result)

def fix_parallel_symbols(text):
    """修复平行符号"""
    if not text:
        return text

    # // -> \parallel（在数学上下文中）
    # 只替换不在$中的//
    parts = re.split(r'(\$[^$]*\$)', text)
    result = []

    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
        else:
            # R1//R2 这种电路中的并联
            part = re.sub(r'([a-zA-Z0-9])\s*//\s*([a-zA-Z0-9])', lambda m: m.group(1) + '$\\parallel$' + m.group(2), part)
            # ∥ -> \parallel
            part = part.replace('∥', r'$\parallel$')
            result.append(part)

    return ''.join(result)

def fix_ion_symbols(text):
    """修复离子符号：Fe2: -> Fe^{2+}, SO2; -> SO_4^{2-}"""
    if not text:
        return text

    # 模式：元素符号+数字: -> 元素符号^{数字+}
    # 如 Fe2: -> Fe^{2+}, Cu2: -> Cu^{2+}
    text = re.sub(r'([A-Z][a-z]?)(\d+):', r'\1^{\2+}', text)

    # 模式：元素符号;: -> 元素符号^{-}
    # 如 Cl;: -> Cl^{-}, OH;: -> OH^{-}
    text = re.sub(r'([A-Z][a-z]?);:', r'\1^{-}', text)

    # 模式：SO42; -> SO_4^{2-}, NO3; -> NO_3^{-}
    # 先处理常见的阴离子
    anion_patterns = [
        (r'SO\s*4\s*2;', r'SO$_4^{2-}$'),
        (r'SO\s*3\s*2;', r'SO$_3^{2-}$'),
        (r'CO\s*3\s*2;', r'CO$_3^{2-}$'),
        (r'NO\s*3;', r'NO$_3^{-}$'),
        (r'NO\s*2;', r'NO$_2^{-}$'),
        (r'PO\s*4\s*3;', r'PO$_4^{3-}$'),
        (r'ClO\s*3;', r'ClO$_3^{-}$'),
        (r'ClO\s*4;', r'ClO$_4^{-}$'),
        (r'MnO\s*4;', r'MnO$_4^{-}$'),
        (r'Cr\s*2O\s*7\s*2;', r'Cr$_2$O$_7^{2-}$'),
        (r'CrO\s*4\s*2;', r'CrO$_4^{2-}$'),
        (r'OH;', r'OH$^{-}$'),
        (r'Cl;', r'Cl$^{-}$'),
        (r'Br;', r'Br$^{-}$'),
        (r'I;', r'I$^{-}$'),
        (r'F;', r'F$^{-}$'),
        (r'S\s*2;', r'S$^{2-}$'),
        (r'O\s*2;', r'O$^{2-}$'),
        (r'H;', r'H$^{+}$'),
        (r'Na;', r'Na$^{+}$'),
        (r'K;', r'K$^{+}$'),
        (r'Ag;', r'Ag$^{+}$'),
        (r'Ca\s*2;', r'Ca$^{2+}$'),
        (r'Mg\s*2;', r'Mg$^{2+}$'),
        (r'Ba\s*2;', r'Ba$^{2+}$'),
        (r'Zn\s*2;', r'Zn$^{2+}$'),
        (r'Cu\s*2;', r'Cu$^{2+}$'),
        (r'Fe\s*2;', r'Fe$^{2+}$'),
        (r'Fe\s*3;', r'Fe$^{3+}$'),
        (r'Al\s*3;', r'Al$^{3+}$'),
        (r'NH\s*4;', r'NH$_4^{+}$'),
    ]

    for pattern, replacement in anion_patterns:
        text = re.sub(pattern, replacement, text)

    return text

# 修复所有字段
fixed_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        original = q.get(field, '')
        if not original:
            continue

        fixed = original
        fixed = fix_superscripts(fixed)
        fixed = fix_chemical_formulas(fixed)
        fixed = fix_parallel_symbols(fixed)
        fixed = fix_ion_symbols(fixed)

        if fixed != original:
            q[field] = fixed
            fixed_count += 1

print(f"修复了 {fixed_count} 个字段")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")
