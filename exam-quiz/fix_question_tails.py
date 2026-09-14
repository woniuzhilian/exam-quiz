import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

def fix_question(text):
    """修复题干中的常见问题"""
    if not text:
        return text

    original = text

    # 1. 修复化学式下标：MgCl 2 -> MgCl$_2$, AlCl 3 -> AlCl$_3$, SiCl 4 -> SiCl$_4$
    text = re.sub(r'(MgCl|AlCl|SiCl|NaCl|HCl|H2SO|HNO|CH|C2H|C3H)\s+(\d)', r'\1$_{\2}$', text)

    # 2. 修复变量下标：P 0 -> P$_0$, x 1 -> x$_1$, y 2 -> y$_2$ 等
    # 只在中文或空格后面的单个字母+空格+数字时修复
    text = re.sub(r'([a-zA-Z])\s+(\d)(?=[\s,，。)）])', r'\1$_{\2}$', text)

    # 3. 删除题干末尾的多余数字（通常是下标被错误提取到末尾）
    # 匹配末尾的 "数字 数字 数字" 或 "数字 ; 数字 数字" 模式
    text = re.sub(r'\s+[\d;]+\s+[\d;]+\s+[\d;]*\s*$', '', text)

    # 4. 修复 NH3·H2O 等
    text = re.sub(r'NH\s*3\s*[·.]\s*H\s*2\s*O', lambda m: 'NH$_3$\\cdot H$_2$O', text)

    # 5. 修复 BaSO4, Na2SO4 等
    text = re.sub(r'(BaSO|Na2SO|NaSO)\s*(\d)', r'\1$_{\2}$', text)

    return text

# 修复所有题干
fixed_count = 0
for q in questions:
    original = q.get('question', '')
    if original:
        fixed = fix_question(original)
        if fixed != original:
            q['question'] = fixed
            fixed_count += 1
            print(f"修复 {q['year']}-{q.get('yearQnum')}")

print(f"\n共修复 {fixed_count} 道题")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")
