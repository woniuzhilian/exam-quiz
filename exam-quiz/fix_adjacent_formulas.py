import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

def merge_adjacent_formulas(text):
    """合并相邻的公式，如 $cos$$t -> $cos t$"""
    if not text:
        return text

    # 模式1：$xxx$$yyy -> $xxx yyy$
    # 重复多次直到没有变化
    prev = None
    while prev != text:
        prev = text
        # 合并两个相邻的公式
        text = re.sub(r'\$([^$]+)\$\$([^$]+)\$', r'$\1 \2$', text)

    return text

def fix_empty_formulas(text):
    """修复空公式问题"""
    if not text:
        return text

    # 移除空的 $ $
    text = re.sub(r'\$\s*\$', '', text)

    return text

# 修复所有字段
fixed_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        original = q.get(field, '')
        if original:
            fixed = merge_adjacent_formulas(original)
            fixed = fix_empty_formulas(fixed)
            if fixed != original:
                q[field] = fixed
                fixed_count += 1

print(f"修复了 {fixed_count} 个字段")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")
