import json, re, os

img_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'
existing_files = set(os.listdir(img_dir))

# 建立 (year, 题号) -> 图片文件列表 的映射
year_qnum_map = {}
for fname in existing_files:
    m = re.match(r'id\d+_([^_]+)_(\d+)_', fname)
    if m:
        year = m.group(1)
        qnum = int(m.group(2))  # 这个是题号
        key = (year, qnum)
        if key not in year_qnum_map:
            year_qnum_map[key] = []
        year_qnum_map[key].append(fname)

print(f'年份+题号映射数: {len(year_qnum_map)}')

# 从原始题库读取
with open(r'D:\应用程序开发\刷题\all_questions_merged.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 检查【本题配图，PDF第XX页】标记的题目，用年份+题号匹配
matched = 0
unmatched = 0
unmatched_list = []
for q in data:
    text = q.get('question', '')
    if '本题配图' in text and 'PDF第' in text:
        key = (q['year'], q['id'])
        if key in year_qnum_map:
            matched += 1
        else:
            unmatched += 1
            if len(unmatched_list) < 20:
                unmatched_list.append(f'{q["bigSubject"]} {q["year"]}-{q["id"]}')

print(f'用年份+题号匹配: 成功{matched}, 失败{unmatched}')
if unmatched_list:
    print(f'失败示例: {unmatched_list[:10]}')

# 看看这些失败的题目的id在图片中是否以其他形式存在
print(f'\n检查2013年题号31是否有图片:')
for f in sorted(existing_files):
    if '2013_31' in f:
        print(f'  {f}')
print(f'检查2013年题号44是否有图片:')
for f in sorted(existing_files):
    if '2013_44' in f:
        print(f'  {f}')
