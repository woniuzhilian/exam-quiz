import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 只检查专业基础
pro_questions = [q for q in questions if q['bigSubject'] == '专业基础']
print(f"专业基础题目数: {len(pro_questions)}")

# 检查各类问题
issues = {
    'latex_no_dollar': [],      # 未被$包裹的LaTeX命令
    'dollar_mismatch': [],      # $符号不配对
    'superscript_semicolon': [], # 上标问题（数字;数字）
    'chemical_formula': [],     # 化学式问题
    'parallel_symbol': [],      # 平行符号问题
    'underscore': [],           # 下划线问题
    'variable_subscript': [],   # 变量下标问题
}

# LaTeX命令模式
latex_cmd_pattern = re.compile(r'\\[a-zA-Z]+')

# 上标模式（数字;数字）
superscript_pattern = re.compile(r'\d+;\d+')

# 常见化学式
chemical_formulas = [
    'Na2SO4', 'NaCl', 'H2O', 'CO2', 'O2', 'N2', 'H2', 'Cl2',
    'CaCO3', 'CaO', 'SiO2', 'Al2O3', 'Fe2O3', 'Fe3O4',
    'NH3', 'H2SO4', 'HNO3', 'HCl', 'NaOH', 'KOH',
    'CH4', 'C2H4', 'C2H2', 'C6H12O6',
    'PCl3', 'PCl5', 'SO2', 'SO3', 'NO2', 'NO',
    'BaSO4', 'AgNO3', 'AgCl', 'CuSO4', 'ZnSO4',
    'MgO', 'MgCl2', 'CaCl2', 'KCl', 'KNO3',
    'Na2CO3', 'NaHCO3', 'K2CO3', 'KHCO3',
    'H3PO4', 'H2S', 'HF', 'HBr', 'HI',
    'FeCl2', 'FeCl3', 'CuCl2', 'ZnCl2', 'AlCl3',
    'NH4Cl', 'NH4NO3', '(NH4)2SO4',
    'CH3COOH', 'C2H5OH', 'CH3OH',
    'C6H6', 'C7H8', 'C8H10',
]

fields_to_check = ['question', 'A', 'B', 'C', 'D', 'analysis']

for q in pro_questions:
    qid = f"{q['year']}-{q.get('yearQnum')}"
    for field in fields_to_check:
        text = q.get(field, '')
        if not text:
            continue
        
        # 检查$符号配对
        dollar_count = text.count('$')
        if dollar_count % 2 != 0:
            issues['dollar_mismatch'].append((qid, field, text[:100]))
        
        # 检查未被$包裹的LaTeX命令
        # 先移除$...$中的内容
        text_no_math = re.sub(r'\$[^$]*\$', '', text)
        latex_cmds = latex_cmd_pattern.findall(text_no_math)
        if latex_cmds:
            issues['latex_no_dollar'].append((qid, field, latex_cmds[:5], text[:100]))
        
        # 检查上标问题
        if superscript_pattern.search(text):
            issues['superscript_semicolon'].append((qid, field, text[:100]))
        
        # 检查化学式（数字字母分开的情况）
        for formula in chemical_formulas:
            # 检查是否有类似"Na SO 2 4"这样的错误格式
            parts = re.findall(r'([A-Z][a-z]?)(\d*)', formula)
            if len(parts) > 1:
                # 构建可能的错误格式模式
                error_pattern = r'\s+'.join([p[0] for p in parts if p[0]])
                if re.search(error_pattern, text):
                    issues['chemical_formula'].append((qid, field, formula, text[:100]))
                    break
        
        # 检查平行符号
        if '//' in text or '∥' in text:
            issues['parallel_symbol'].append((qid, field, text[:100]))

# 输出统计
print("\n=== 问题统计 ===")
for issue_type, issue_list in issues.items():
    print(f"{issue_type}: {len(issue_list)} 个字段")

# 输出详细问题（前20个）
print("\n=== 未被$包裹的LaTeX命令（前20个）===")
for item in issues['latex_no_dollar'][:20]:
    print(f"{item[0]} {item[1]}: {item[2]} -> {item[3]}")

print("\n=== $符号不配对（前20个）===")
for item in issues['dollar_mismatch'][:20]:
    print(f"{item[0]} {item[1]}: {item[2]}")

print("\n=== 上标问题（前20个）===")
for item in issues['superscript_semicolon'][:20]:
    print(f"{item[0]} {item[1]}: {item[2]}")
