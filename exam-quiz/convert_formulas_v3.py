import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 补充缺失的字符映射
extra_map = {
    # 数学粗体希腊字母 U+1D6C2-U+1D6E1 (小写)
    '\U0001D6C2': r'\alpha', '\U0001D6C3': r'\beta', '\U0001D6C4': r'\gamma',
    '\U0001D6C5': r'\delta', '\U0001D6C6': r'\epsilon', '\U0001D6C7': r'\zeta',
    '\U0001D6C8': r'\eta', '\U0001D6C9': r'\theta', '\U0001D6CA': r'\iota',
    '\U0001D6CB': r'\kappa', '\U0001D6CC': r'\lambda', '\U0001D6CD': r'\mu',
    '\U0001D6CE': r'\nu', '\U0001D6CF': r'\xi', '\U0001D6D0': r'\omicron',
    '\U0001D6D1': r'\pi', '\U0001D6D2': r'\rho', '\U0001D6D3': r'\varsigma',
    '\U0001D6D4': r'\sigma', '\U0001D6D5': r'\tau', '\U0001D6D6': r'\upsilon',
    '\U0001D6D7': r'\varphi', '\U0001D6D8': r'\chi', '\U0001D6D9': r'\psi',
    '\U0001D6DA': r'\omega', '\U0001D6DB': r'\partial', '\U0001D6DC': r'\epsilon',
    '\U0001D6DD': r'\vartheta', '\U0001D6DE': r'\varkappa', '\U0001D6DF': r'\phi',
    '\U0001D6E0': r'\varrho', '\U0001D6E1': r'\varpi',
    # 数学粗体希腊字母 U+1D6E2-U+1D6FB (大写)
    '\U0001D6E2': 'A', '\U0001D6E3': 'B', '\U0001D6E4': r'\Gamma',
    '\U0001D6E5': r'\Delta', '\U0001D6E6': 'E', '\U0001D6E7': 'Z',
    '\U0001D6E8': 'H', '\U0001D6E9': r'\Theta', '\U0001D6EA': 'I',
    '\U0001D6EB': 'K', '\U0001D6EC': r'\Lambda', '\U0001D6ED': 'M',
    '\U0001D6EE': 'N', '\U0001D6EF': r'\Xi', '\U0001D6F0': 'O',
    '\U0001D6F1': r'\Pi', '\U0001D6F2': 'P', '\U0001D6F3': r'\Theta',
    '\U0001D6F4': r'\Sigma', '\U0001D6F5': 'T', '\U0001D6F6': r'\Upsilon',
    '\U0001D6F7': r'\Phi', '\U0001D6F8': 'X', '\U0001D6F9': r'\Psi',
    '\U0001D6FA': r'\Omega', '\U0001D6FB': r'\nabla',
    # 其他缺失
    '\U0001D4BE': 'i', '\U0001D4CA': 'u',
    '\u03F0': r'\varkappa', '\u03F1': r'\varrho', '\u03F5': r'\varepsilon',
}

count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        original = q.get(field, '')
        converted = original
        for ch, repl in extra_map.items():
            if ch in converted:
                converted = converted.replace(ch, repl)
        if converted != original:
            q[field] = converted
            count += 1

print(f"补充转换了 {count} 个字段")

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

# 验证
remaining = set()
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        for ch in text:
            if ord(ch) > 127 and not ('\u4e00' <= ch <= '\u9fff'):
                if ch not in '，。、；：（）【】《》""''！？…—-':
                    remaining.add(ch)

print(f"仍有 {len(remaining)} 个特殊字符")
if remaining:
    for ch in sorted(remaining):
        print(f"  {ch} (U+{ord(ch):04X})")
