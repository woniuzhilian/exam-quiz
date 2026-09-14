import json, re, os

# 从原始合并题库中查找
with open(r'D:\应用程序开发\刷题\all_questions_merged.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 查找含【配图：idXXX_year_page_seq.png】的题
print("=== 含具体文件名的配图标记（原始题库）===")
for q in data:
    text = q.get('question', '')
    m = re.search(r'【配图[：:](id\d+_[^_]+_\d+_\d+\.\w+)】', text)
    if m:
        fname = m.group(1)
        fm = re.match(r'id(\d+)_([^_]+)_(\d+)_(\d+)', fname)
        if fm:
            file_id = int(fm.group(1))
            file_year = fm.group(2)
            file_page = fm.group(3)
            print(f'题库: {q["bigSubject"]} {q["year"]}-{q["id"]} | 文件: id={file_id} year={file_year} page={file_page} | {fname}')

# 统计图片文件名中的年份分布
img_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'
files = os.listdir(img_dir)
year_count = {}
for f in files:
    m = re.match(r'id\d+_([^_]+)_', f)
    if m:
        y = m.group(1)
        year_count[y] = year_count.get(y, 0) + 1
print(f"\n=== 图片文件年份分布 ===")
for y, c in sorted(year_count.items()):
    print(f"  {y}: {c}张")
