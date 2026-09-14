from PIL import Image
import os

output_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images\pro'
os.makedirs(output_dir, exist_ok=True)

# 配图裁剪配置：(年份, 题号, PDF页码, 裁剪坐标)
crop_configs = [
    # pro_q_056.png
    ('2022补', 24, 56, (380, 150, 620, 280)),
    ('2024', 24, 56, (300, 380, 700, 620)),
    
    # pro_q_058.png - 需要查看确认
    # ('2023', 25, 58, (350, 400, 650, 600)),
    
    # pro_q_050.png - 需要查看确认
    # ('2024', 21, 50, (350, 400, 650, 600)),
    
    # pro_q_054.png - 2024-19和2024-23
    # ('2024', 19, 54, (350, 380, 650, 600)),  # 与2024-23同页
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

print('\n第五批配图裁剪完成')
