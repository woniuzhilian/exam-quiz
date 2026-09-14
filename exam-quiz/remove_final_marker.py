import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

pro = [q for q in questions if q['bigSubject'] == '专业基础']
public = [q for q in questions if q['bigSubject'] == '公共基础']

# 检查2024-27题的题干
for q in pro:
    if q['year'] == '2024' and q.get('yearQnum') == 27:
        print(f'2024-27题干: {q["question"]}')
        # 移除题干中的配图标记
        q['question'] = re.sub(r'【本题配有示意图】|【本题配图，PDF第\d+页】', '', q['question'])
        print(f'更新后: {q["question"]}')

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

# 最终检查
remaining = []
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text and ('本题配有示意图' in text or '本题配图' in text):
            remaining.append((q['year'], q.get('yearQnum'), field))
            break

print(f'\n还剩 {len(remaining)} 道题需要处理配图')
for year, qnum, field in remaining:
    print(f'  {year}-{qnum} ({field})')
