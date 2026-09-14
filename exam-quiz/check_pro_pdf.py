import pymupdf

# 专业基础PDF路径
question_pdf = r'D:\证件相关\一级岩土工程师\岩土专业基础分类真题解析（16~24）_题目.pdf'
analysis_pdf = r'D:\证件相关\一级岩土工程师\岩土专业基础分类真题解析（16~24）_答案解析.pdf'

# 查看页数
doc_q = pymupdf.open(question_pdf)
print(f"专业基础题目PDF页数: {len(doc_q)}")
doc_q.close()

doc_a = pymupdf.open(analysis_pdf)
print(f"专业基础答案解析PDF页数: {len(doc_a)}")
doc_a.close()
