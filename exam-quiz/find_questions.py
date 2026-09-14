import pymupdf
import re

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_题目.pdf'
doc = pymupdf.open(pdf_path)

# 需要查找的题目
targets = ['2017-455', '2018-562', '2018-563', '2018-569', '2018-600', '2019-690', '2019-691', '2020-812']
found = {}

for page_idx in range(len(doc)):
    page = doc[page_idx]
    text = page.get_text()
    for target in targets:
        if target not in found and f'【{target}】' in text:
            found[target] = page_idx + 1  # 页码从1开始
            print(f'  {target} 在PDF第{page_idx + 1}页')

doc.close()

print(f'\n找到: {len(found)}/{len(targets)}')
for t in targets:
    if t not in found:
        print(f'  未找到: {t}')
