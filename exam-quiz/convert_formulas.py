import json, re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Unicode数学字符到LaTeX/普通字符的映射
char_map = {
    # 数学斜体大写字母
    '\U0001D434': 'A', '\U0001D435': 'B', '\U0001D436': 'C', '\U0001D437': 'D',
    '\U0001D438': 'E', '\U0001D439': 'F', '\U0001D43B': 'H', '\U0001D43C': 'I',
    '\U0001D43D': 'J', '\U0001D43E': 'K', '\U0001D43F': 'L', '\U0001D440': 'M',
    '\U0001D441': 'N', '\U0001D442': 'O', '\U0001D443': 'P', '\U0001D444': 'Q',
    '\U0001D445': 'R', '\U0001D446': 'S', '\U0001D447': 'T', '\U0001D449': 'V',
    '\U0001D44A': 'W',
    # 数学斜体小写字母
    '\U0001D44E': 'a', '\U0001D450': 'c', '\U0001D451': 'd', '\U0001D452': 'e',
    '\U0001D453': 'f', '\U0001D454': 'g', '\U0001D456': 'i', '\U0001D458': 'k',
    '\U0001D459': 'l', '\U0001D45A': 'm', '\U0001D45B': 'n', '\U0001D45C': 'o',
    '\U0001D45E': 'q', '\U0001D45F': 'r', '\U0001D460': 's', '\U0001D461': 't',
    '\U0001D462': 'u', '\U0001D463': 'v', '\U0001D465': 'x', '\U0001D466': 'y',
    '\U0001D467': 'z',
    # 数学粗体斜体
    '\U0001D47A': 'S', '\U0001D496': 'u', '\U0001D49B': 'z',
    # 数学斜体希腊字母
    '\U0001D6FC': r'\alpha', '\U0001D706': r'\lambda', '\U0001D707': r'\mu',
    '\U0001D70B': r'\pi', '\U0001D70D': r'\varsigma', '\U0001D711': r'\varphi',
    '\U0001D714': r'\omega',
    # 数学数字
    '\U0001D7CF': '1', '\U0001D7D0': '2',
    # 普通希腊字母
    '\u03B1': r'\alpha', '\u03B2': r'\beta', '\u03B3': r'\gamma', '\u03B4': r'\delta',
    '\u03B5': r'\epsilon', '\u03B6': r'\zeta', '\u03B7': r'\eta', '\u03B8': r'\theta',
    '\u03B9': r'\iota', '\u03BA': r'\kappa', '\u03BB': r'\lambda', '\u03BC': r'\mu',
    '\u03BD': r'\nu', '\u03BE': r'\xi', '\u03C0': r'\pi', '\u03C1': r'\rho',
    '\u03C2': r'\varsigma', '\u03C3': r'\sigma', '\u03C4': r'\tau', '\u03C5': r'\upsilon',
    '\u03C6': r'\varphi', '\u03C7': r'\chi', '\u03C8': r'\psi', '\u03C9': r'\omega',
    '\u0394': r'\Delta', '\u0398': r'\Theta', '\u039B': r'\Lambda', '\u039E': r'\Xi',
    '\u03A0': r'\Pi', '\u03A3': r'\Sigma', '\u03A6': r'\Phi', '\u03A8': r'\Psi',
    '\u03A9': r'\Omega',
    # 数学符号
    '\u2211': r'\sum', '\u222B': r'\int', '\u222C': r'\iint', '\u221A': r'\sqrt',
    '\u221E': r'\infty', '\u2260': r'\neq', '\u2264': r'\leq', '\u2265': r'\geq',
    '\u2248': r'\approx', '\u2261': r'\equiv', '\u222A': r'\cup', '\u2229': r'\cap',
    '\u2208': r'\in', '\u2209': r'\notin', '\u2282': r'\subset', '\u2283': r'\supset',
    '\u2286': r'\subseteq', '\u2287': r'\supseteq', '\u2220': r'\angle',
    '\u22C5': r'\cdot', '\u22EF': r'\cdots', '\u2212': '-', '\u2217': '*',
    '\u2219': r'\cdot', '\u22BF': r'\triangle',
    # 其他符号
    '\u00B0': r'^{\circ}', '\u00B1': r'\pm', '\u00D7': r'\times', '\u00F7': r'\div',
    '\u2032': "'", '\u2015': '-', '\u2016': r'\|', '\u2044': '/',
    '\u2190': r'\leftarrow', '\u2192': r'\rightarrow', '\u21CC': r'\rightleftharpoons',
    '\u21D2': r'\Rightarrow', '\u25AA': r'\bullet',
    # 西里尔字母误用
    '\u0424': r'\Phi',
    # 组合字符
    '\u0305': '', '\u0307': '',
    # 私有区域字符
    '\uF02B': '+', '\uF03D': '=',
    # 全角字符
    '\uFF08': '(', '\uFF09': ')', '\uFF0C': ',', '\uFF1A': ':', '\uFF1B': ';',
    '\u3001': ',', '\u3002': '.',
}

def convert_chars(text):
    """转换特殊字符"""
    result = []
    for ch in text:
        if ch in char_map:
            result.append(char_map[ch])
        else:
            result.append(ch)
    return ''.join(result)

def wrap_formulas(text):
    """尝试将包含LaTeX命令的片段用$...$包裹"""
    # 匹配包含LaTeX命令的连续片段
    # 这个比较复杂，先简单处理：将包含\alpha, \beta等的行用$包裹
    
    # 先转换字符
    text = convert_chars(text)
    
    # 检测是否包含LaTeX命令
    latex_commands = [r'\alpha', r'\beta', r'\gamma', r'\delta', r'\epsilon', r'\zeta',
                      r'\eta', r'\theta', r'\iota', r'\kappa', r'\lambda', r'\mu',
                      r'\nu', r'\xi', r'\pi', r'\rho', r'\sigma', r'\tau', r'\upsilon',
                      r'\varphi', r'\chi', r'\psi', r'\omega', r'\Delta', r'\Theta',
                      r'\Lambda', r'\Xi', r'\Pi', r'\Sigma', r'\Phi', r'\Psi', r'\Omega',
                      r'\sum', r'\int', r'\iint', r'\sqrt', r'\infty', r'\neq', r'\leq',
                      r'\geq', r'\approx', r'\equiv', r'\cup', r'\cap', r'\in', r'\notin',
                      r'\subset', r'\supset', r'\subseteq', r'\supseteq', r'\angle',
                      r'\cdot', r'\cdots', r'\pm', r'\times', r'\div', r'\leftarrow',
                      r'\rightarrow', r'\rightleftharpoons', r'\Rightarrow', r'\bullet',
                      r'\triangle', r'\circ', r'\Phi', r'\varsigma']
    
    has_latex = any(cmd in text for cmd in latex_commands)
    
    if has_latex and '$' not in text:
        # 简单处理：如果整段文本主要是公式，用$包裹
        # 但要避免把中文也包进去
        # 这里采用保守策略：不自动包裹，只转换字符
        pass
    
    return text

# 处理所有题目
count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        original = q.get(field, '')
        converted = wrap_formulas(original)
        if converted != original:
            q[field] = converted
            count += 1

print(f"转换了 {count} 个字段")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("公式字符转换完成")

# 验证：检查是否还有未转换的特殊字符
remaining = set()
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        for ch in text:
            if ord(ch) > 127 and not ('\u4e00' <= ch <= '\u9fff') and ch not in '，。、；：（）【】《》""''！？':
                if ch not in char_map.values():
                    remaining.add(ch)

if remaining:
    print(f"\n仍有特殊字符:")
    for ch in sorted(remaining):
        print(f"  {ch} (U+{ord(ch):04X})")
else:
    print("\n所有特殊字符已转换")
