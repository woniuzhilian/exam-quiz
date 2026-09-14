import json, re, pymupdf, os

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_题目.pdf'
img_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'
doc = pymupdf.open(pdf_path)

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 9道真的需要配图的题目
need_figure_keys = {
    '2013-90': 214,  # PDF第214页
    '2017-455': None,  # 需要查找页码
    '2018-562': None,
    '2018-563': None,
    '2018-569': None,
    '2018-600': None,
    '2019-690': None,
    '2019-691': None,
    '2020-812': None,
}

# 先从题库中获取这些题目的PDF页码
for q in data:
    key = f'{q["year"]}-{q["id"]}'
    if key in need_figure_keys:
        text = q.get('question', '')
        m = re.search(r'PDF第(\d+)页', text)
        if m:
            need_figure_keys[key] = int(m.group(1))

print("需要配图的题目及PDF页码:")
for k, v in need_figure_keys.items():
    print(f"  {k}: PDF第{v}页")

# 对于每道题，渲染PDF页面并裁剪题目区域
def extract_question_image(year, qnum, page_num):
    """渲染PDF页面，找到题目位置，裁剪出题目区域（包括配图）"""
    page_idx = page_num - 1
    if page_idx >= len(doc):
        return None

    page = doc[page_idx]

    # 找到题目在页面上的位置
    blocks = page.get_text("blocks")
    q_y0 = None
    q_y1 = None
    next_q_y0 = None

    for b in blocks:
        x0, y0, x1, y1, text, block_no, block_type = b
        if f'【{year}-{qnum}】' in text:
            q_y0 = y0
        elif q_y0 is not None and next_q_y0 is None and re.search(r'【\d{4}-\d+】', text):
            next_q_y0 = y0
            break

    if q_y0 is None:
        print(f"  未找到题目 {year}-{qnum} 在第{page_num}页")
        return None

    # 确定裁剪区域：从题目开始到下一题开始（或页面底部）
    crop_y0 = max(0, q_y0 - 10)
    crop_y1 = next_q_y0 if next_q_y0 else page.rect.height
    crop_rect = pymupdf.Rect(0, crop_y0, page.rect.width, crop_y1)

    # 渲染裁剪区域
    mat = pymupdf.Matrix(2, 2)  # 2倍缩放
    pix = page.get_pixmap(matrix=mat, clip=crop_rect)

    # 保存图片
    fname = f'pdf_render_{year}_{qnum}.png'
    fpath = os.path.join(img_dir, fname)
    pix.save(fpath)
    print(f"  已提取: {fname} (区域 y={crop_y0:.0f}-{crop_y1:.0f})")
    return fname

# 提取9道题的图片
extracted = {}
for key, page_num in need_figure_keys.items():
    if page_num:
        year, qnum = key.split('-')
        fname = extract_question_image(int(year), int(qnum), page_num)
        if fname:
            extracted[key] = fname

doc.close()

# 更新题库：删除误标记，为9道题添加图片
removed = 0
updated = 0
for q in data:
    text = q.get('question', '')
    if '本题配图' in text and 'PDF第' in text:
        key = f'{q["year"]}-{q["id"]}'
        if key in extracted:
            # 添加图片标签，删除标记
            img_tag = f'<img src="/images/{extracted[key]}" style="max-width:100%;">'
            q['question'] = re.sub(r'【本题配图[，,]PDF第\d+页】', img_tag, text)
            updated += 1
        else:
            # 删除误标记
            q['question'] = re.sub(r'【本题配图[，,]PDF第\d+页】', '', text)
            removed += 1

print(f'\n删除误标记: {removed}道')
print(f'添加渲染图片: {updated}道')

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'已保存: {len(data)}题')
