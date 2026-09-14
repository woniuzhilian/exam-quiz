import pymupdf
import re

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_题目.pdf'
doc = pymupdf.open(pdf_path)

# 查找2023年的题目在哪些页
print("=== 2023年题目在PDF中的位置 ===")
for page_idx in range(len(doc)):
    page = doc[page_idx]
    text = page.get_text()
    matches = re.findall(r'【2023-(\d+)】', text)
    if matches:
        print(f"PDF第{page_idx+1}页: 2023-{', '.join(matches[:8])}{'...' if len(matches)>8 else ''}")

# 查看2023年第1题的内容
print("\n=== 2023年第1题内容 ===")
for page_idx in range(len(doc)):
    page = doc[page_idx]
    text = page.get_text()
    if '【2023-1】' in text:
        # 提取该题附近的文本
        idx = text.find('【2023-1】')
        print(text[idx:idx+500])
        break

doc.close()
