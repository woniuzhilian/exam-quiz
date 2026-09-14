import json, re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 分析剩余【本题配图，PDF第XX页】标记的题目
need_figure = []  # 真的需要配图
maybe_mislabel = []  # 可能误标记

for q in data:
    text = q.get('question', '')
    if '本题配图' in text and 'PDF第' in text:
        clean_text = re.sub(r'【本题配图[，,]PDF第\d+页】', '', text).strip()
        # 判断是否真的需要配图
        # 明确需要配图的关键词：如图所示、下图、上图、中图、如图、波形如图、电路如图、图示
        has_clear_figure = bool(re.search(r'(如图所示|下图|上图|中图|如图|波形如图|电路如图|图示|见图|参考图)', clean_text))
        is_very_short = len(clean_text) < 10

        if has_clear_figure or is_very_short:
            need_figure.append({
                'year': q['year'], 'id': q['id'],
                'smallSubject': q.get('smallSubject', ''),
                'question': clean_text[:60],
                'reason': '短题干' if is_very_short else '含配图关键词'
            })
        else:
            maybe_mislabel.append({
                'year': q['year'], 'id': q['id'],
                'smallSubject': q.get('smallSubject', ''),
                'question': clean_text[:60]
            })

print(f'真的需要配图: {len(need_figure)}道')
print(f'可能误标记: {len(maybe_mislabel)}道')

print(f'\n=== 真的需要配图的题目 ===')
for q in need_figure:
    print(f'  {q["year"]}-{q["id"]} [{q["smallSubject"]}] ({q["reason"]}): {q["question"]}')

print(f'\n=== 可能误标记的题目（前20道）===')
for q in maybe_mislabel[:20]:
    print(f'  {q["year"]}-{q["id"]} [{q["smallSubject"]}]: {q["question"]}')
