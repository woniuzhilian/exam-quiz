import fitz
import os

# 渲染PDF页面为图片
def render_pdf_pages(pdf_path, output_dir, start_page, end_page, prefix):
    doc = fitz.open(pdf_path)
    os.makedirs(output_dir, exist_ok=True)
    
    for i in range(start_page - 1, min(end_page, len(doc))):
        page = doc[i]
        # 提高渲染分辨率
        mat = fitz.Matrix(2, 2)
        pix = page.get_pixmap(matrix=mat)
        output_path = os.path.join(output_dir, f'{prefix}_{i+1:03d}.png')
        pix.save(output_path)
        print(f'已渲染: {output_path}')
    
    doc.close()

# 2017年PDF - 渲染后面的页面
render_pdf_pages(
    r'D:\应用程序开发\刷题\题目和答案pdf\公共基础真题+2017.pdf',
    r'D:\应用程序开发\刷题\exam-quiz\missing_questions',
    30, 42, '2017'
)

# 2018年PDF
render_pdf_pages(
    r'D:\应用程序开发\刷题\题目和答案pdf\公共基础真题+2018.pdf',
    r'D:\应用程序开发\刷题\exam-quiz\missing_questions',
    30, 42, '2018'
)

# 2021年PDF
render_pdf_pages(
    r'D:\应用程序开发\刷题\题目和答案pdf\公共基础真题+2021.pdf',
    r'D:\应用程序开发\刷题\exam-quiz\missing_questions',
    35, 45, '2021'
)

# 2023年PDF
render_pdf_pages(
    r'D:\应用程序开发\刷题\题目和答案pdf\2023年公共基础+真题.pdf',
    r'D:\应用程序开发\刷题\exam-quiz\missing_questions',
    15, 20, '2023'
)
