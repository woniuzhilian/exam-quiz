from PIL import Image
import os

output_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images\pro'
os.makedirs(output_dir, exist_ok=True)

# 配图裁剪配置：(年份, 题号, PDF页码, 裁剪坐标)
crop_configs = [
    # pro_q_054.png
    ('2023', 24, 54, (350, 100, 650, 280)),
    ('2024', 23, 54, (350, 380, 650, 600)),
    
    # pro_q_059.png
    ('2019', 24, 59, (350, 200, 650, 350)),
    ('2020', 24, 59, (300, 450, 700, 600)),
    
    # pro_q_060.png
    ('2016', 23, 60, (350, 180, 650, 330)),
    ('2022', 26, 60, (380, 600, 620, 780)),
    ('2023', 26, 60, (400, 950, 600, 1150)),
    ('2024', 26, 60, (350, 1300, 650, 1500)),  # 结构动力反应分析题
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

print('\n第三批配图裁剪完成')
