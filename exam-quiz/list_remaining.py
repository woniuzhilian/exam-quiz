import json, re
from collections import Counter

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 统计剩余【本题配图，PDF第XX页】标记
remaining = []
for q in data:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if '本题配图' in text and 'PDF第' in text:
            page = re.search(r'PDF第(\d+)页', text)
            remaining.append({
                'bigSubject': q['bigSubject'],
                'year': q['year'],
                'id': q['id'],
                'smallSubject': q.get('smallSubject', ''),
                'page': page.group(1) if page else '?',
                'question': q['question'][:80]
            })

print(f'剩余未匹配配图题目: {len(remaining)}道')
print(f'\n按年份分布:')
year_count = Counter(r['year'] for r in remaining)
for y, c in sorted(year_count.items()):
    print(f'  {y}: {c}道')

print(f'\n按小科目分布:')
subj_count = Counter(r['smallSubject'] for r in remaining)
for s, c in sorted(subj_count.items(), key=lambda x: -x[1]):
    print(f'  {s}: {c}道')

print(f'\n题目列表示例（前20道）:')
for r in remaining[:20]:
    print(f'  {r["bigSubject"]} {r["year"]}-{r["id"]} [{r["smallSubject"]}] PDF第{r["page"]}页: {r["question"][:50]}')
