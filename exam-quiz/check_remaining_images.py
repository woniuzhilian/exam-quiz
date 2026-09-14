import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

pro = [q for q in questions if q['bigSubject'] == '专业基础']

# 检查还有哪些题目包含"本题配有示意图"或"本题配图"
remaining = []
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text and ('本题配有示意图' in text or '本题配图' in text):
            remaining.append((q['year'], q.get('yearQnum'), field, text[:50]))
            break

print(f'还剩 {len(remaining)} 道题需要处理配图:')
for year, qnum, field, text in remaining:
    print(f'  {year}-{qnum} ({field}): {text}...')

# 检查2024年的题号
year_2024 = [q for q in pro if q['year'] == '2024']
year_2024_sorted = sorted(year_2024, key=lambda x: x.get('yearQnum', 0))
qnums = [q.get('yearQnum') for q in year_2024_sorted]
print(f'\n2024年题号范围: {min(qnums)} - {max(qnums)}')
print(f'2024年题数: {len(year_2024)}')
print(f'缺少的题号: {[n for n in range(1, 61) if n not in qnums]}')

# 检查2024年各题的内容
print('\n2024年题目列表:')
for q in year_2024_sorted:
    print(f"  {q['year']}-{q.get('yearQnum')}: {q.get('question', '')[:60]}...")
