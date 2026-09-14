from PIL import Image
import os

output_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images\pro'
os.makedirs(output_dir, exist_ok=True)

# 配图裁剪配置：(年份, 题号, PDF页码, 裁剪坐标)
crop_configs = [
    # pro_q_049.png
    ('2022', 22, 49, (250, 280, 750, 350)),
    ('2022补', 22, 49, (350, 420, 650, 580)),
    ('2023', 22, 49, (380, 700, 620, 900)),
    ('2024', 22, 49, (250, 1050, 750, 1150)),
    
    # pro_q_051.png
    ('2017', 22, 51, (350, 220, 650, 420)),
    ('2017', 23, 51, (350, 520, 650, 780)),
    ('2019', 22, 51, (350, 950, 650, 1200)),
    
    # pro_q_052.png
    ('2019', 23, 52, (350, 150, 650, 350)),
    ('2020', 23, 52, (350, 450, 650, 750)),
    ('2021', 22, 52, (350, 900, 650, 1200)),
    
    # pro_q_053.png
    ('2021', 23, 53, (350, 180, 650, 380)),
    ('2022', 23, 53, (350, 450, 650, 700)),
    ('2022补', 23, 53, (350, 800, 650, 1000)),
    
    # pro_q_055.png (已处理)
    # ('2016', 22, 55, (380, 230, 620, 400)),  # 已处理
    # ('2017', 24, 55, (380, 550, 620, 720)),  # 已处理
    # ('2018', 22, 55, (380, 850, 620, 1020)),  # 已处理
    # ('2022', 24, 55, (380, 1200, 620, 1400)),  # 已处理
    
    # pro_q_057.png
    ('2016', 24, 57, (380, 180, 620, 350)),
    ('2018', 24, 57, (250, 450, 700, 620)),
    ('2021', 24, 57, (350, 750, 650, 920)),
    ('2022补', 25, 57, (250, 1000, 700, 1180)),
]

for year, qnum, page_num, coords in crop_configs:
    img_path = rf'D:\应用程序开发\刷题\exam-quiz\question_images\pro\pro_q_{page_num:03d}.png'
    if os.path.exists(img_path):
        img = Image.open(img_path)
        cropped = img.crop(coords)
        # 处理年份中的"补"字
        year_str = year.replace('补', 'bu')
        output_path = os.path.join(output_dir, f'{year_str}_{qnum}.png')
        cropped.save(output_path)
        print(f'已保存: {year_str}_{qnum}.png (来自第{page_num}页)')
    else:
        print(f'文件不存在: {img_path}')

print('\n第二批配图裁剪完成')
