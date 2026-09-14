from PIL import Image
import os

output_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images\pro'
os.makedirs(output_dir, exist_ok=True)

# 从pro_q_055.png裁剪配图
img = Image.open(r'D:\应用程序开发\刷题\exam-quiz\question_images\pro\pro_q_055.png')

# 2016-22题配图：刚架结构图
crop_2016_22 = img.crop((380, 230, 620, 400))
crop_2016_22.save(os.path.join(output_dir, '2016_22.png'))
print('已保存 2016_22.png')

# 2017-24题配图：梁的图
crop_2017_24 = img.crop((380, 550, 620, 720))
crop_2017_24.save(os.path.join(output_dir, '2017_24.png'))
print('已保存 2017_24.png')

# 2018-22题配图：刚架结构图
crop_2018_22 = img.crop((380, 850, 620, 1020))
crop_2018_22.save(os.path.join(output_dir, '2018_22.png'))
print('已保存 2018_22.png')

# 2022-24题配图：刚架结构图
crop_2022_24 = img.crop((380, 1200, 620, 1400))
crop_2022_24.save(os.path.join(output_dir, '2022_24.png'))
print('已保存 2022_24.png')

print('\n配图裁剪完成')
