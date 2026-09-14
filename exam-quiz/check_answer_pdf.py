import pymupdf
import re

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_答案解析.pdf'
doc = pymupdf.open(pdf_path)

print(f"答案解析PDF共{len(doc)}页")

# 检查前10页的内容，看是否按题号顺序
for page_idx in range(min(10, len(doc))):
    page = doc[page_idx]
    text = page.get_text()
    # 查找题号
    qnums = re.findall(r'(\d{4})\s*年?\s*第?\s*(\d+)\s*题', text)
    if not qnums:
        qnums = re.findall(r'【(\d{4})-(\d+)】', text)
    if not qnums:
        qnums = re.findall(r'(?:^|\n)\s*(\d{4})[年\-](\d+)', text)
    print(f"\n第{page_idx+1}页: 找到{len(qnums)}个题号标记")
    if qnums:
        print(f"  前5个: {qnums[:5]}")
    # 显示前200字符
    print(f"  内容: {text[:200].replace(chr(10), ' ')}")

doc.close()
