import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 问题1：选项或题干中包含 \pi 但没有被 $ 包裹
print("=== 问题1：包含 \\pi 但未被 $ 包裹 ===")
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        # 查找不在 $...$ 中的 \pi
        # 简单方法：移除所有 $...$ 后检查是否还有 \pi
        cleaned = re.sub(r'\$[^$]+\$', '', text)
        if '\\pi' in cleaned or 'π' in cleaned:
            print(f"{q['year']}-{q.get('yearQnum')} {field}: {text[:80]}")
            break

print("\n=== 问题2：题干末尾有多余数字/符号 ===")
for q in questions:
    text = q.get('question', '')
    # 检查末尾是否有类似 "数字 ; 数字 数字" 的模式
    if re.search(r'[\d;]\s*[\d;]\s*[\d;]?\s*$', text.strip()):
        print(f"{q['year']}-{q.get('yearQnum')}: {text[-50:]}")

print("\n=== 问题3：公式不完整（空的 $...$）===")
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if re.search(r'\$\s*[=:]\s*\$', text) or re.search(r'\$\s*=\s*=\s*\$', text):
            print(f"{q['year']}-{q.get('yearQnum')} {field}: {text[:80]}")
            break

print("\n=== 问题4：选项中包含 \\alpha, \\beta 等但未被 $ 包裹 ===")
latex_cmds = ['\\alpha', '\\beta', '\\gamma', '\\theta', '\\sigma', '\\mu', '\\lambda', '\\delta', '\\omega', '\\rho', '\\tau', '\\phi', '\\varphi']
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        cleaned = re.sub(r'\$[^$]+\$', '', text)
        for cmd in latex_cmds:
            if cmd in cleaned:
                print(f"{q['year']}-{q.get('yearQnum')} {field}: {text[:80]}")
                break
        else:
            continue
        break

print("\n扫描完成")
