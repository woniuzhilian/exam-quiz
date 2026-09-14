import json, re, os

img_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'
existing_files = set(os.listdir(img_dir))

# 建立 (year, page) -> 图片文件列表 的映射
year_page_map = {}
for fname in existing_files:
    m = re.match(r'id\d+_([^_]+)_(\d+)_', fname)
    if m:
        year = m.group(1)
        page = int(m.group(2))
        key = (year, page)
        if key not in year_page_map:
            year_page_map[key] = []
        year_page_map[key].append(fname)

print(f'图片文件总数: {len(existing_files)}')
print(f'年份+页码映射数: {len(year_page_map)}')

# 从原始题库重新读取（因为之前的转换已经改了questions.json）
with open(r'D:\应用程序开发\刷题\all_questions_merged.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def convert_images(text, q):
    if not text:
        return text
    """
    转换各种图片标记为 <img> 标签
    1. 【见本题选项配图：xxx.png】
    2. 【配图：xxx.png】
    3. 【本题配图，PDF第XX页】 -> 根据年份+PDF页码匹配
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
    # 3. 【本题配图，PDF第XX页】 -> 根据年份+PDF页码查找图片
    def replace_pdf_page(match):
        page_num = int(match.group(1))
        key = (q['year'], page_num)
        if key in year_page_map:
            imgs = sorted(year_page_map[key])
            return ''.join(f'<img src="/images/{f}" style="max-width:100%;">' for f in imgs)
        return match.group(0)  # 找不到就保留原标记

    text = re.sub(r'【本题配图[，,]PDF第(\d+)页】', replace_pdf_page, text)

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
            page_m = re.search(r'PDF第(\d+)页', original)
            if page_m:
                key = (q['year'], int(page_m.group(1)))
                if key in year_page_map:
                    pdf_page_matched += 1
                else:
                    pdf_page_unmatched += 1
        q[field] = convert_images(original, q)

# 检查转换后是否还有未转换的【】配图标记
remaining = []
for q in data:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if '【' in text and '配图' in text:
            remaining.append((q['bigSubject'], q['year'], q['id'], field, text[:80]))

# 检查<img>引用的图片是否存在
img_ref_missing = []
for q in data:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        imgs = re.findall(r'<img[^>]+src="/images/([^"]+)"', text)
        for img in imgs:
            if img not in existing_files:
                img_ref_missing.append((q['bigSubject'], q['year'], q['id'], img))

print(f'\n转换统计:')
print(f'  选项配图标记: {count_option_img}')
print(f'  题干配图标记(有文件名): {count_peitu_img}')
print(f'  PDF页码标记: {count_pdf_page} (匹配成功: {pdf_page_matched}, 未匹配: {pdf_page_unmatched})')
print(f'  剩余未转换标记: {len(remaining)}')
print(f'  引用缺失图片: {len(img_ref_missing)}')

if remaining:
    print(f'\n未转换标记示例（前10个）:')
    for r in remaining[:10]:
        print(f'  {r[0]} {r[1]}-{r[2]} {r[3]}: {r[4]}')

if img_ref_missing:
    print(f'\n缺失图片示例（前10个）:')
    seen = set()
    for r in img_ref_missing:
        if r[3] not in seen:
            seen.add(r[3])
            print(f'  {r[0]} {r[1]}-{r[2]}: {r[3]}')
        if len(seen) >= 10:
            break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'\n已保存更新后的题库: {len(data)}题')
