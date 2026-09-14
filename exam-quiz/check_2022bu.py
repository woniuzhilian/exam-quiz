import pymupdf
import re

question_pdf = r'D:\证件相关\一级岩土工程师\公共基础分类版真题详解（13~24）_题目.pdf'
doc = pymupdf.open(question_pdf)

# 查找2022补考相关的标记
for page_num in range(len(doc)):
    text = doc[page_num].get_text()
    if '2022' in text and ('补' in text or '补考' in text):
        # 找出所有题号标记
        matches = re.findall(r'【\d{4}[^】]*】', text)
        if matches:
            print(f"第{page_num+1}页: {matches[:5]}")

doc.close()
