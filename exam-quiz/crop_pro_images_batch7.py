from PIL import Image
import os

output_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images\pro'
os.makedirs(output_dir, exist_ok=True)

# 配图裁剪配置：(年份, 题号, PDF页码, 裁剪坐标)
crop_configs = [
    # pro_q_058.png
    ('2023', 25, 58, (380, 100, 620, 280)),
    
    # pro_q_068.png
    ('2024', 40, 68, (350, 100, 650, 350)),
    
    # pro_q_075.png
    ('2020', 27, 75, (250, 1050, 750, 1180)),
    
    # pro_q_080.png
    ('2016', 30, 80, (280, 380, 720, 620)),
    
    # pro_q_081.png
    ('2018', 29, 81, (300, 120, 700, 500)),
    
    # pro_q_082.png
    ('2021', 30, 82, (350, 380, 650, 520)),
    
    # pro_q_083.png
    ('2022补', 32, 83, (350, 120, 650, 320)),
    
    # pro_q_076.png
    ('2021', 27, 76, (380, 600, 620, 750)),
    
    # pro_q_077.png
    ('2022补', 28, 77, (300, 700, 700, 950)),
    
    # pro_q_041.png
    ('2021', 53, 41, (380, 580, 620, 720)),
]

for year, qnum, page_num, coords in crop_configs:
    img_path = rf'D:\应用程序开发\刷题\exam-quiz\question_images\pro\pro_q_{page_num:03d}.png'
    if os.path.exists(img_path):
        img = Image.open(img_path)
        cropped = img.crop(coords)
        year_str = year.replace('补', 'bu')
        output_path = os.path.join(output_dir, f'{year_str}_{qnum}.png')
        cropped.save(output_path)
        print(f'已保存: {year_str}_{qnum}.png (来自第{page_num}页)')
    else:
        print(f'文件不存在: {img_path}')

print('\n第七批配图裁剪完成')
