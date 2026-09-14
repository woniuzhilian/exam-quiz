import json, re, os

img_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'
existing_files = set(os.listdir(img_dir))

# 建立 (year, 题号) -> 图片文件列表 的映射（用于PDF页码标记匹配）
year_qnum_map = {}
for fname in existing_files:
    m = re.match(r'id\d+_([^_]+)_(\d+)_', fname)
    if m:
        year = m.group(1)
        qnum = int(m.group(2))
        key = (year, qnum)
        if key not in year_qnum_map:
            year_qnum_map[key] = []
        year_qnum_map[key].append(fname)

# 从原始题库读取
with open(r'D:\应用程序开发\刷题\all_questions_merged.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def filenames_to_imgs(filenames_str):
    """将逗号分隔的文件名字符串转换为多个<img>标签"""
    # 分割文件名（支持中英文逗号）
    parts = re.split(r'[，,]\s*', filenames_str.strip())
    imgs = []
    for p in parts:
        p = p.strip()
        if p:
            imgs.append(f'<img src="/images/{p}" style="max-width:100%;">')
    return ''.join(imgs)

def convert_images(text, q):
    if not text:
        return text
    """
    转换各种图片标记为 <img> 标签
    1. 【见本题选项配图：xxx.png, yyy.png】-> 多个<img>
    2. 【配图：xxx.png, yyy.png】-> 多个<img>
    3. 【本题配图，PDF第XX页】-> 根据年份+题号匹配，匹配不到保留文本
    """
    # 1. 【见本题选项配图：...】 -> <img>
    text = re.sub(
        r'【见本题选项配图[：:]([^】]+)】',
        lambda m: filenames_to_imgs(m.group(1)),
        text
    )
    # 2. 【配图：...】 -> <img>
    text = re.sub(
        r'【配图[：:]([^】]+)】',
        lambda m: filenames_to_imgs(m.group(1)),
        text
    )
    # 3. 【本题配图，PDF第XX页】-> 根据年份+题号查找图片
    def replace_pdf_page(match):
        key = (q['year'], q['id'])
        if key in year_qnum_map:
            imgs = sorted(year_qnum_map[key])
            return ''.join(f'<img src="/images/{f}" style="max-width:100%;">' for f in imgs)
        return match.group(0)  # 找不到就保留原标记

    text = re.sub(r'【本题配图[，,]PDF第\d+页】', replace_pdf_page, text)

    return text

# 统计
count_option_img = 0
count_peitu_img = 0
count_pdf_page = 0
pdf_page_matched = 0
pdf_page_unmatched = 0

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
            key = (q['year'], q['id'])
            if key in year_qnum_map:
                pdf_page_matched += 1
            else:
                pdf_page_unmatched += 1
        q[field] = convert_images(original, q)

# 检查转换后状态
remaining = []
img_ref_missing = []
for q in data:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if '【' in text and '配图' in text:
            remaining.append((q['bigSubject'], q['year'], q['id'], field))
        imgs = re.findall(r'<img[^>]+src="/images/([^"]+)"', text)
        for img in imgs:
            if img not in existing_files:
                img_ref_missing.append((q['bigSubject'], q['year'], q['id'], img))

print(f'转换统计:')
print(f'  选项配图标记: {count_option_img}')
print(f'  题干配图标记(有文件名): {count_peitu_img}')
print(f'  PDF页码标记: {count_pdf_page} (匹配: {pdf_page_matched}, 未匹配: {pdf_page_unmatched})')
print(f'  剩余未转换标记: {len(remaining)}')
print(f'  引用缺失图片: {len(img_ref_missing)}')

if img_ref_missing:
    print(f'\n缺失图片（去重）:')
    seen = set()
    for item in img_ref_missing:
        if item[3] not in seen:
            seen.add(item[3])
            print(f'  {item[3]} ({item[0]} {item[1]}-{item[2]})')

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'\n已保存: {len(data)}题')
