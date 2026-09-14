import pymupdf
import re

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\公共基础分类版真题详解（13~24）_题目.pdf'
doc = pymupdf.open(pdf_path)

# 收集所有题目编号格式
all_qnums = set()
for page_idx in range(len(doc)):
    page = doc[page_idx]
    text = page.get_text()
    matches = re.findall(r'【([^】]+)】', text)
    for m in matches:
        if re.search(r'\d{4}', m):
            all_qnums.add(m)

# 按年份分组
from collections import defaultdict
by_year = defaultdict(list)
for q in all_qnums:
    m = re.match(r'(\d{4})(.*?)-(\d+)', q)
    if m:
        year = m.group(1)
        suffix = m.group(2)
        by_year[year + suffix].append(int(m.group(3)))

print("题目编号格式:")
for year, nums in sorted(by_year.items()):
    print(f"  {year}: {len(nums)}题, 范围{min(nums)}-{max(nums)}")

doc.close()
