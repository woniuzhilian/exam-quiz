import pymupdf
import re

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\岩土专业基础分类真题解析（16~24）_题目.pdf'
doc = pymupdf.open(pdf_path)

# 检查第6-15页
for page_idx in range(5, min(15, len(doc))):
    page = doc[page_idx]
    text = page.get_text()
    if text.strip():
        print(f"\n第{page_idx+1}页:")
        print(f"  内容: {text[:300].replace(chr(10), ' ')}")
        qnums = re.findall(r'【(\d{4})-(\d+)】', text)
        print(f"  【YYYY-NN】标记: {qnums[:10]}")
        qnums2 = re.findall(r'(?:^|\n)\s*(\d+)[、.．]\s', text)
        print(f"  数字题号: {qnums2[:10]}")
    else:
        images = page.get_images()
        print(f"\n第{page_idx+1}页: 无文本, {len(images)}张图片")

doc.close()
