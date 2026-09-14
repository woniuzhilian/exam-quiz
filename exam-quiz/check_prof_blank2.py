import pymupdf
import re

pdf_path = r'D:\证件相关\一级岩土工程师\真题空白卷\岩土专业基础历年真题试题册（2024版）.pdf'
doc = pymupdf.open(pdf_path)

# 检查第5-10页
for page_idx in range(4, min(10, len(doc))):
    page = doc[page_idx]
    text = page.get_text()
    print(f"\n第{page_idx+1}页:")
    print(f"  内容: {text[:300].replace(chr(10), ' ')}")
    # 查找题号
    qnums = re.findall(r'(?:^|\n)\s*(\d+)\s*[.、]', text)
    print(f"  题号: {qnums[:10]}")

doc.close()
