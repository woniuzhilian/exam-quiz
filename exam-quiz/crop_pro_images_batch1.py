from PIL import Image
import os

output_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images\pro'
os.makedirs(output_dir, exist_ok=True)

# 配图裁剪配置：(年份, 题号, PDF页码, 裁剪坐标)
# 坐标格式：(left, top, right, bottom)
crop_configs = [
    # pro_q_051.png
    ('2017', 22, 51, (350, 220, 650, 420)),
    ('2017', 23, 51, (350, 520, 650, 780)),
    ('2019', 22, 51, (350, 950, 650, 1200)),
    
    # pro_q_052.png
    ('2019', 23, 52, (350, 150, 650, 350)),
    ('2020', 23, 52, (350, 450, 650, 750)),
    ('2021', 22, 52, (350, 900, 650, 1200)),
]

for year, qnum, page_num, coords in crop_configs:
    img_path = rf'D:\应用程序开发\刷题\exam-quiz\question_images\pro\pro_q_{page_num:03d}.png'
    if os.path.exists(img_path):
        img = Image.open(img_path)
        cropped = img.crop(coords)
        output_path = os.path.join(output_dir, f'{year}_{qnum}.png')
        cropped.save(output_path)
        print(f'已保存: {year}_{qnum}.png (来自第{page_num}页)')
    else:
        print(f'文件不存在: {img_path}')

print('\n第一批配图裁剪完成')
