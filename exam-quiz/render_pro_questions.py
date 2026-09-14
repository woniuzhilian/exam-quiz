import pymupdf
import os

# 专业基础PDF路径
question_pdf = r'D:\证件相关\一级岩土工程师\岩土专业基础分类真题解析（16~24）_题目.pdf'
analysis_pdf = r'D:\证件相关\一级岩土工程师\岩土专业基础分类真题解析（16~24）_答案解析.pdf'
output_dir = r'D:\应用程序开发\刷题\exam-quiz\question_images'

# 创建专业基础子目录
pro_dir = os.path.join(output_dir, 'pro')
os.makedirs(pro_dir, exist_ok=True)

# 渲染题目PDF所有页面
print("开始渲染专业基础题目PDF...")
doc_q = pymupdf.open(question_pdf)
total_q = len(doc_q)
for i in range(total_q):
    page = doc_q[i]
    pix = page.get_pixmap(dpi=150)
    output_path = os.path.join(pro_dir, f'pro_q_{i+1:03d}.png')
    pix.save(output_path)
    if (i+1) % 20 == 0:
        print(f"  已渲染 {i+1}/{total_q} 个题目页面")
doc_q.close()
print(f"题目PDF渲染完成，共 {total_q} 个页面")

# 渲染解析PDF所有页面
print("\n开始渲染专业基础答案解析PDF...")
doc_a = pymupdf.open(analysis_pdf)
total_a = len(doc_a)
for i in range(total_a):
    page = doc_a[i]
    pix = page.get_pixmap(dpi=150)
    output_path = os.path.join(pro_dir, f'pro_a_{i+1:03d}.png')
    pix.save(output_path)
    if (i+1) % 20 == 0:
        print(f"  已渲染 {i+1}/{total_a} 个解析页面")
doc_a.close()
print(f"解析PDF渲染完成，共 {total_a} 个页面")

print("\n全部完成！")
print(f"题目页面: {total_q} 张")
print(f"解析页面: {total_a} 张")
print(f"存储目录: {pro_dir}")
