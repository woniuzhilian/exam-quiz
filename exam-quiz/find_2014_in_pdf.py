import pymupdf
import re

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_题目.pdf'
doc = pymupdf.open(pdf_path)

# 查找2014年的题目在PDF中的位置
print("=== 查找2014年题目在PDF中的位置 ===")
for page_idx in range(len(doc)):
    page = doc[page_idx]
    text = page.get_text()
    # 查找2014年的题目编号
    matches = re.findall(r'【2014-(\d+)】', text)
    if matches:
        print(f"PDF第{page_idx+1}页: 2014-{', '.join(matches[:5])}{'...' if len(matches)>5 else ''}")

doc.close()
