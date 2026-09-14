import pymupdf
import re

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\岩土专业基础分类真题解析（16~24）_题目.pdf'
doc = pymupdf.open(pdf_path)

print(f"共{len(doc)}页")

# 检查前5页
for page_idx in range(min(5, len(doc))):
    page = doc[page_idx]
    text = page.get_text()
    print(f"\n第{page_idx+1}页:")
    print(f"  内容: {text[:300].replace(chr(10), ' ')}")
    # 查找题号格式
    qnums = re.findall(r'(?:^|\n)\s*(\d+)[、.．]\s', text)
    print(f"  题号: {qnums[:10]}")

doc.close()
