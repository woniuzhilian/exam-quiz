import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

def fix_formula_boundary(text):
    """修复公式边界问题"""
    if not text:
        return text

    # 模式1：字母/数字$= -> 字母/数字=$ （把等号移到公式内）
    # 例如：Q$=\Delta$E -> Q=$\Delta$E
    text = re.sub(r'([a-zA-Z0-9\)\]])\$=', r'\1=$', text)

    # 模式2：=$字母/数字 -> $=字母/数字 （把等号移到公式内）
    # 例如：$\epsilon=$c -> $\epsilon=c$
    # 这个比较复杂，需要谨慎

    # 模式3：$= 开头的公式，把前面的内容合并
    # 例如：公式Q$=\Delta$E+A= -> 公式$Q=\Delta E+A=$

    return text

# 先看看模式1的效果
test_cases = [
    '等温变化公式Q$=\\Delta$E+A=',
    '由均匀流基本方程h$= 2\\tau0$f',
    'e$= 2\\times3;1 \\lambda=',
]

print("=== 测试模式1 ===")
for t in test_cases:
    print(f"原: {t}")
    print(f"修: {fix_formula_boundary(t)}")
    print()

# 修复所有字段
fixed_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        original = q.get(field, '')
        if original:
            fixed = fix_formula_boundary(original)
            if fixed != original:
                q[field] = fixed
                fixed_count += 1

print(f"修复了 {fixed_count} 个字段")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")
