import json, re, os

img_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'
existing_files = set(os.listdir(img_dir))

# 建立 id_year -> 图片文件列表 的映射
id_year_map = {}
for fname in existing_files:
    # 匹配 id{id}_{year}_*.png
    m = re.match(r'id(\d+)_([^_]+)_', fname)
    if m:
        qid = int(m.group(1))
        year = m.group(2)
        key = (qid, year)
        if key not in id_year_map:
            id_year_map[key] = []
        id_year_map[key].append(fname)

print(f'图片文件总数: {len(existing_files)}')
print(f'id_year映射数: {len(id_year_map)}')

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def convert_images(text, q):
    if not text:
        return text
    """
    转换各种图片标记为 <img> 标签
    1. 【见本题选项配图：xxx.png】
    2. 【配图：xxx.png】
    3. 【本题配图，PDF第XX页】
    """
    # 1. 【见本题选项配图：xxx.png】 -> <img>
    text = re.sub(
        r'【见本题选项配图[：:]([^】]+)】',
        lambda m: f'<img src="/images/{m.group(1).strip()}" style="max-width:100%;">',
        text
    )
    # 2. 【配图：xxx.png】 -> <img>
    text = re.sub(
        r'【配图[：:]([^】]+)】',
        lambda m: f'<img src="/images/{m.group(1).strip()}" style="max-width:100%;">',
        text
    )
    # 3. 【本题配图，PDF第XX页】 -> 根据id和年份查找图片
    def replace_pdf_page(match):
        key = (q['id'], q['year'])
        if key in id_year_map:
            imgs = id_year_map[key]
            return ''.join(f'<img src="/images/{f}" style="max-width:100%;">' for f in sorted(imgs))
        return match.group(0)  # 找不到就保留原标记

    text = re.sub(r'【本题配图[，,]PDF第\d+页】', replace_pdf_page, text)

    return text

# 统计
count_option_img = 0
count_peitu_img = 0
count_pdf_page = 0
missing_imgs = []

for q in data:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        original = q.get(field, '')
        if not original:
            continue
        if '【见本题选项配图' in original:
            count_option_img += 1
        if '【配图：' in original or '【配图:' in original:
            count_peitu_img += 1
        if '本题配图' in original and 'PDF第' in original:
            count_pdf_page += 1
        q[field] = convert_images(original, q)

# 检查转换后是否还有未转换的【】配图标记
remaining = 0
for q in data:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if '【' in text and '配图' in text:
            remaining += 1
            if remaining <= 10:
                print(f'  剩余标记: {q["bigSubject"]} {q["year"]}-{q["id"]} {field}: {text[:100]}')

# 检查<img>引用的图片是否存在
img_ref_missing = 0
for q in data:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        imgs = re.findall(r'<img[^>]+src="/images/([^"]+)"', text)
        for img in imgs:
            if img not in existing_files:
                img_ref_missing += 1
                if img_ref_missing <= 10:
                    print(f'  缺失图片: {q["bigSubject"]} {q["year"]}-{q["id"]}: {img}')

print(f'\n转换统计:')
print(f'  选项配图标记: {count_option_img}')
print(f'  题干配图标记: {count_peitu_img}')
print(f'  PDF页码标记: {count_pdf_page}')
print(f'  剩余未转换标记: {remaining}')
print(f'  引用缺失图片: {img_ref_missing}')

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'\n已保存更新后的题库: {len(data)}题')
