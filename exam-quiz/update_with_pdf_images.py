import json, re, os

# 读取图片匹配结果
with open(r'D:\应用程序开发\刷题\exam-quiz\pdf_image_mapping.json', 'r', encoding='utf-8') as f:
    pdf_mapping = json.load(f)

# 读取当前题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

img_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'
existing_files = set(os.listdir(img_dir))

# 统计
updated = 0
still_missing = 0
already_has_img = 0

for q in data:
    key = f'{q["year"]}-{q["id"]}'
    text = q.get('question', '')

    # 检查是否还有【本题配图，PDF第XX页】标记
    if '本题配图' in text and 'PDF第' in text:
        if key in pdf_mapping:
            # 有匹配的图片，替换标记
            imgs = pdf_mapping[key]
            img_tags = ''.join(f'<img src="/images/{f}" style="max-width:100%;">' for f in imgs)
            q['question'] = re.sub(r'【本题配图[，,]PDF第\d+页】', img_tags, text)
            updated += 1
        else:
            # 没有匹配的图片，保留标记
            still_missing += 1
    elif key in pdf_mapping and '<img' not in text:
        # 题目没有配图标记但在PDF中有图片（可能是之前漏标记的）
        # 检查题干是否提到"图"
        clean_text = re.sub(r'<[^>]+>', '', text)
        if re.search(r'[图如图所示下图上图]', clean_text):
            imgs = pdf_mapping[key]
            img_tags = ''.join(f'<img src="/images/{f}" style="max-width:100%;">' for f in imgs)
            q['question'] = img_tags + text
            updated += 1

# 最终检查
remaining = 0
missing_refs = 0
for q in data:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if '本题配图' in text and 'PDF第' in text:
            remaining += 1
        imgs = re.findall(r'<img[^>]+src="/images/([^"]+)"', text)
        for img in imgs:
            if img not in existing_files:
                missing_refs += 1

print(f'更新题目数: {updated}')
print(f'仍缺失配图（保留文本标记）: {still_missing}')
print(f'剩余【本题配图】标记: {remaining}')
print(f'引用缺失图片: {missing_refs}')

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'\n已保存: {len(data)}题')
