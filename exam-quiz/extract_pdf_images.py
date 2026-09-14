import pymupdf
import re, os, json

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_题目.pdf'
doc = pymupdf.open(pdf_path)

# 先测试第51页（index 50）的文本块和图片位置
page = doc[50]
print(f'页面尺寸: {page.rect}')

# 获取所有文本块
blocks = page.get_text("blocks")
print(f'\n文本块数量: {len(blocks)}')
for b in blocks[:15]:
    x0, y0, x1, y1, text, block_no, block_type = b
    text_clean = text.strip().replace('\n', ' ')[:60]
    print(f'  y={y0:.0f}-{y1:.0f}: {text_clean}')

# 获取所有图片及其位置
images = page.get_images(full=True)
print(f'\n图片数量: {len(images)}')
for img in images:
    xref = img[0]
    # 获取图片在页面上的位置
    rects = page.get_image_rects(xref)
    for r in rects:
        print(f'  xref={xref}, 位置: y={r.y0:.0f}-{r.y1:.0f}, x={r.x0:.0f}-{r.x1:.0f}')

doc.close()
