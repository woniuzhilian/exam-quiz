import pymupdf
import re

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_题目.pdf'
doc = pymupdf.open(pdf_path)

# 检查2013-90题（PDF第214页，index 213）
page = doc[213]
print(f'=== PDF第214页 ===')
print(f'页面尺寸: {page.rect}')

# 获取文本块
blocks = page.get_text("blocks")
for b in blocks:
    x0, y0, x1, y1, text, block_no, block_type = b
    text_clean = text.strip().replace('\n', ' ')[:80]
    if text_clean:
        print(f'  y={y0:.0f}-{y1:.0f}: {text_clean}')

# 获取图片
images = page.get_images(full=True)
print(f'\n嵌入图片数量: {len(images)}')

# 检查页面上的绘图（矢量图形）
drawings = page.get_drawings()
print(f'矢量图形数量: {len(drawings)}')

doc.close()
