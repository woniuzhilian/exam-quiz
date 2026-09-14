import json, re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 查找含【配图：xxx.png】的题，分析文件名与题目id/year的关系
print("=== 含具体文件名的配图标记 ===")
count = 0
for q in data:
    text = q.get('question', '')
    m = re.search(r'【配图[：:]([^】]+)】', text)
    if m:
        fname = m.group(1)
        # 解析文件名中的id和year
        fm = re.match(r'id(\d+)_([^_]+)_', fname)
        if fm:
            file_id = int(fm.group(1))
            file_year = fm.group(2)
            print(f'题库: {q["bigSubject"]} {q["year"]}-{q["id"]} | 文件: id={file_id} year={file_year} | {fname}')
            count += 1
            if count >= 15:
                break

print(f"\n=== 含【本题配图，PDF第XX页】的题（前10道）===")
count = 0
for q in data:
    text = q.get('question', '')
    if '本题配图' in text and 'PDF第' in text:
        page = re.search(r'PDF第(\d+)页', text)
        page_num = page.group(1) if page else '?'
        print(f'{q["bigSubject"]} {q["year"]}-{q["id"]} | PDF第{page_num}页 | {text[:60]}')
        count += 1
        if count >= 10:
            break
