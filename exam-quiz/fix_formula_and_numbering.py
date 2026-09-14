import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 1. 修复公式中缺少空格的问题
def fix_formula_spaces(text):
    if not text:
        return text
    # \int后面加空格
    text = re.sub(r'\\int([a-zA-Z])', r'\\int \1', text)
    # \frac后面加空格
    text = re.sub(r'\\frac([^ {])', r'\\frac \1', text)
    # \partial后面加空格
    text = re.sub(r'\\partial([a-zA-Z])', r'\\partial \1', text)
    # \sin, \cos, \tan后面加空格
    for func in ['sin', 'cos', 'tan', 'ln', 'log', 'exp']:
        text = re.sub(r'\\' + func + r'([a-zA-Z])', r'\\' + func + r' \1', text)
    return text

count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text:
            new_text = fix_formula_spaces(text)
            if new_text != text:
                q[field] = new_text
                count += 1

print(f"修复公式空格: {count} 个字段")

# 2. 修复2013年题号64重复的问题
# 查找2013年题号为64的题目
year_2013 = [q for q in questions if q['year'] == '2013' and q['bigSubject'] == '公共基础']
q64_list = [q for q in year_2013 if q.get('yearQnum') == 64]
print(f"\n2013年题号64的题目: {len(q64_list)} 道")
for i, q in enumerate(q64_list):
    print(f"  题目{i+1}: {q.get('question', '')[:80]}...")

# 如果有两道64题，说明原来的63题被我改成了64，需要改回63
# 或者原来的64题需要改成65
if len(q64_list) == 2:
    # 找到我之前修改的那道题（实心圆和空心圆的题目）
    for q in q64_list:
        if '实心圆' in q.get('question', '') or '空心圆' in q.get('question', ''):
            q['yearQnum'] = 63
            print(f"  已将实心圆/空心圆题目改回题号63")
            break

# 重新排序和分配id
public = [q for q in questions if q['bigSubject'] == '公共基础']
pro = [q for q in questions if q['bigSubject'] == '专业基础']

public.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))
pro.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))

for i, q in enumerate(public):
    q['id'] = i + 1

pro_start = len(public) + 1
for i, q in enumerate(pro):
    q['id'] = pro_start + i

final = public + pro

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print("\n题库已更新")
