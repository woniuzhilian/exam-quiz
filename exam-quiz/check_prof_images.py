import pymupdf

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\岩土专业基础分类真题解析（16~24）_题目.pdf'
doc = pymupdf.open(pdf_path)

print(f"共{len(doc)}页")

# 检查每一页的图片数量
total_images = 0
for page_idx in range(len(doc)):
    page = doc[page_idx]
    images = page.get_images()
    text = page.get_text()
    if images or text.strip():
        print(f"第{page_idx+1}页: {len(images)}张图片, {len(text)}字符文本")
    total_images += len(images)

print(f"\n总图片数: {total_images}")

# 检查第20页的详细内容
if len(doc) > 20:
    page = doc[20]
    print(f"\n第21页详细:")
    print(f"  文本: {page.get_text()[:200]}")
    print(f"  图片: {len(page.get_images())}")

doc.close()
