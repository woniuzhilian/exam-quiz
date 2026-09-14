import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

pro = [q for q in questions if q['bigSubject'] == '专业基础']
public = [q for q in questions if q['bigSubject'] == '公共基础']

# 修复2024-22题的选项
q = next((x for x in pro if x['year'] == '2024' and x.get('yearQnum') == 22), None)
if q:
    print('修复2024-22题选项:')
    q['A'] = '$\\frac{FL^3}{12EI}$'
    q['B'] = '$\\frac{FL^3}{15EI}$'
    q['C'] = '$\\frac{2FL^3}{12EI}$'
    q['D'] = '$\\frac{FL^3}{4EI}$'
    print(f'  A: {q["A"]}')
    print(f'  B: {q["B"]}')
    print(f'  C: {q["C"]}')
    print(f'  D: {q["D"]}')

# 重新排序和分配id
pro.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))
public.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))

for i, q in enumerate(public):
    q['id'] = i + 1

pro_start = len(public) + 1
for i, q in enumerate(pro):
    q['id'] = pro_start + i

final = public + pro

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print('\n题库已更新')
