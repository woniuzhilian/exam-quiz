import fitz
import os
from PIL import Image

# 专业基础题目PDF
pdf_path = r'D:\证件相关\一级岩土工程师\岩土专业基础分类真题解析（16~24）_题目.pdf'
output_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images\pro'
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)

# 需要提取图片的题目列表
# 格式：(年份, 题号, PDF页码, 配图区域坐标)
# 坐标需要根据实际页面调整
questions_to_extract = [
    # 2016年
    ('2016', 22, 55, (300, 200, 500, 380)),  # 刚架结构图
    ('2016', 23, 60, None),  # 需要查看页面确定坐标
    ('2016', 24, 57, None),
    ('2016', 30, 80, None),
]

def render_page(page_num):
    """渲染PDF页面为图片"""
    page = doc[page_num - 1]
    mat = fitz.Matrix(2, 2)
    pix = page.get_pixmap(matrix=mat)
    img_path = os.path.join(output_dir, f'temp_page_{page_num}.png')
    pix.save(img_path)
    return img_path

def crop_image(img_path, coords, output_path):
    """裁剪图片"""
    img = Image.open(img_path)
    cropped = img.crop(coords)
    cropped.save(output_path)
    print(f'已保存: {output_path}')

# 先渲染需要的页面
pages_to_render = set([q[2] for q in questions_to_extract])
for page_num in pages_to_render:
    render_page(page_num)
    print(f'已渲染第{page_num}页')

doc.close()
print('\n页面渲染完成，请查看图片确定配图坐标')
