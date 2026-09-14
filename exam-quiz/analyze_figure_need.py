import json, re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 检查剩余【本题配图，PDF第XX页】标记的题目，看题干是否提到"图"
remaining = []
for q in data:
    text = q.get('question', '')
    if '本题配图' in text and 'PDF第' in text:
        # 去掉标记后的题干
        clean_text = re.sub(r'【本题配图[，,]PDF第\d+页】', '', text).strip()
        has_figure_keyword = bool(re.search(r'[图如图所示下图上图中图]', clean_text))
        is_short = len(clean_text) < 10
        remaining.append({
            'year': q['year'],
            'id': q['id'],
            'smallSubject': q.get('smallSubject', ''),
            'has_figure': has_figure_keyword,
            'is_short': is_short,
            'question': clean_text[:60]
        })

print(f'总剩余标记: {len(remaining)}')
print(f'题干含"图"关键词: {sum(1 for r in remaining if r["has_figure"])}')
print(f'题干过短(<10字): {sum(1 for r in remaining if r["is_short"])}')
print(f'既不含图也不短(可能误标记): {sum(1 for r in remaining if not r["has_figure"] and not r["is_short"])}')

print(f'\n=== 题干含"图"的题目（前20道）===')
for r in remaining:
    if r['has_figure']:
        print(f'  {r["year"]}-{r["id"]} [{r["smallSubject"]}]: {r["question"]}')

print(f'\n=== 题干过短的题目（前20道）===')
for r in remaining:
    if r['is_short']:
        print(f'  {r["year"]}-{r["id"]} [{r["smallSubject"]}]: {r["question"]}')

print(f'\n=== 可能误标记的题目（前20道）===')
count = 0
for r in remaining:
    if not r['has_figure'] and not r['is_short']:
        print(f'  {r["year"]}-{r["id"]} [{r["smallSubject"]}]: {r["question"]}')
        count += 1
        if count >= 20:
            break
