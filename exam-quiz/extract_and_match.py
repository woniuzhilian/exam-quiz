import pymupdf
import re, os, json

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_题目.pdf'
img_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'
os.makedirs(img_dir, exist_ok=True)

doc = pymupdf.open(pdf_path)
print(f'PDF总页数: {len(doc)}')

# 存储每道题匹配到的图片: key=(year, qnum), value=[image_filename,...]
question_images = {}

# 遍历每一页
for page_idx in range(len(doc)):
    page = doc[page_idx]
    page_num = page_idx + 1  # PDF页码从1开始

    # 1. 获取页面上所有题目编号及其y坐标
    blocks = page.get_text("blocks")
    questions_on_page = []  # [(year, qnum, y0), ...]
    for b in blocks:
        x0, y0, x1, y1, text, block_no, block_type = b
        # 匹配【YYYY-NN】格式
        matches = re.findall(r'【(\d{4})-(\d+)】', text)
        for year, qnum in matches:
            questions_on_page.append((int(year), int(qnum), y0))

    if not questions_on_page:
        continue

    # 2. 获取页面上所有图片及其位置
    images = page.get_images(full=True)
    for img in images:
        xref = img[0]
        rects = page.get_image_rects(xref)
        if not rects:
            continue
        img_y0 = rects[0].y0

        # 3. 将图片匹配到位于其上方的最近一道题
        # 找到所有y0 < img_y0的题目，取y0最大的那个
        candidates = [q for q in questions_on_page if q[2] < img_y0]
        if not candidates:
            # 图片在页面顶部，可能属于上一页最后一题，跳过
            continue
        # 按y坐标排序，取最大的（最接近图片上方的）
        candidates.sort(key=lambda x: x[2], reverse=True)
        year, qnum, _ = candidates[0]

        key = (year, qnum)
        if key not in question_images:
            question_images[key] = []

        # 提取图片
        try:
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            # 文件名格式: pdf_page{页码}_{xref}.{ext}
            fname = f'pdf_p{page_num}_{xref}.{image_ext}'
            fpath = os.path.join(img_dir, fname)
            if not os.path.exists(fpath):
                with open(fpath, 'wb') as f:
                    f.write(image_bytes)
            question_images[key].append(fname)
        except Exception as e:
            print(f'  提取图片失败: page={page_num}, xref={xref}, error={e}')

doc.close()

print(f'\n匹配到图片的题目数: {len(question_images)}')
total_imgs = sum(len(v) for v in question_images.values())
print(f'提取图片总数: {total_imgs}')

# 显示一些匹配结果
print(f'\n匹配结果示例（前20个）:')
for i, (key, imgs) in enumerate(sorted(question_images.items())[:20]):
    print(f'  {key[0]}-{key[1]}: {imgs}')

# 保存匹配结果
with open(r'D:\应用程序开发\刷题\exam-quiz\pdf_image_mapping.json', 'w', encoding='utf-8') as f:
    json.dump({f'{k[0]}-{k[1]}': v for k, v in question_images.items()}, f, ensure_ascii=False, indent=2)

print(f'\n匹配结果已保存到 pdf_image_mapping.json')
