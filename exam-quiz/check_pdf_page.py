import fitz  # PyMuPDF

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_题目.pdf'
doc = fitz.open(pdf_path)
print(f'PDF总页数: {len(doc)}')

# 检查第51页（index 50）的文本内容
page = doc[50]
text = page.get_text()
print(f'\n第51页文本（前500字）:')
print(text[:500])

# 检查页面中的图片
images = page.get_images(full=True)
print(f'\n第51页图片数量: {len(images)}')
for i, img in enumerate(images):
    print(f'  图片{i}: xref={img[0]}, width={img[2]}, height={img[3]}')

doc.close()
