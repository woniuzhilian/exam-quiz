import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

pro = [q for q in questions if q['bigSubject'] == '专业基础']
public = [q for q in questions if q['bigSubject'] == '公共基础']

# 检查特殊符号
special_chars = ['α', 'β', 'γ', 'δ', 'π', 'Δ', 'Σ', '≤', '≥', '±', '×', '÷', '≠', '≈', '∞', '∫', '∂', '∇', '√', '∠', '⊥', '∥', '∵', '∴']

print("包含特殊符号的字段:")
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text:
            found = [char for char in special_chars if char in text]
            if found:
                print(f"\n  {q['year']}-{q.get('yearQnum')} ({field}):")
                print(f"    特殊符号: {found}")
                print(f"    内容: {text[:100]}...")
