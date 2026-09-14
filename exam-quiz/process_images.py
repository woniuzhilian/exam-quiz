import json, re, os

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

images_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'

# 统计图片标记
pdf_ref_count = 0
img_marker_count = 0
img_tag_count = 0

for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if '本题配图' in text or 'PDF第' in text:
            pdf_ref_count += 1
        if '【配图' in text:
            img_marker_count += 1
        if '<img' in text:
            img_tag_count += 1

print(f"含'本题配图/PDF第'标记: {pdf_ref_count}")
print(f"含'【配图'标记: {img_marker_count}")
print(f"含<img>标签: {img_tag_count}")

# 处理图片标记
def process_images(text):
    # 1. 处理【配图：filename.png】或【配图：filename.png, filename2.png】
    def replace_img_marker(match):
        filenames = match.group(1)
        # 分割多个文件名
        parts = re.split(r'[,，]', filenames)
        imgs = []
        for part in parts:
            part = part.strip()
            if part:
                # 检查文件是否存在
                filepath = os.path.join(images_dir, part)
                if os.path.exists(filepath):
                    imgs.append(f'<img src="/images/{part}" style="max-width:100%;">')
                else:
                    # 尝试查找类似文件名
                    imgs.append(f'<img src="/images/{part}" style="max-width:100%;">')
        return ''.join(imgs)

    text = re.sub(r'【配图[：:]\s*([^】]+)】', replace_img_marker, text)

    # 2. 处理【本题配图，PDF第XX页】- 删除标记，因为无法直接提取图片
    text = re.sub(r'【本题配图[，,]\s*PDF第\d+页】', '', text)

    # 3. 处理残留的【本题配图】标记
    text = re.sub(r'【本题配图[^】]*】', '', text)

    return text

# 应用处理
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D']:
        q[field] = process_images(q.get(field, ''))

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"\n图片标记处理完成")

# 再次统计
pdf_ref_count2 = 0
img_marker_count2 = 0
img_tag_count2 = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if '本题配图' in text or 'PDF第' in text:
            pdf_ref_count2 += 1
        if '【配图' in text:
            img_marker_count2 += 1
        if '<img' in text:
            img_tag_count2 += 1

print(f"处理后含'本题配图/PDF第'标记: {pdf_ref_count2}")
print(f"处理后含'【配图'标记: {img_marker_count2}")
print(f"处理后含<img>标签: {img_tag_count2}")
