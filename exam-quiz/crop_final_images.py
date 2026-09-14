from PIL import Image
import os
import shutil

output_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images\pro'
os.makedirs(output_dir, exist_ok=True)

# 2024-27题的选项配图在pro_q_054.png中
img_path = r'D:\应用程序开发\刷题\exam-quiz\question_images\pro\pro_q_054.png'
img = Image.open(img_path)

# 裁剪四个选项的配图（弯矩图）
# 选项A: 大约在坐标(200, 800, 750, 900)
# 选项B: 大约在坐标(200, 920, 750, 1020)
# 选项C: 大约在坐标(200, 1040, 750, 1140)
# 选项D: 大约在坐标(200, 1160, 750, 1260)

# 实际上，2024-27题的配图是四个选项连在一起的，我直接裁剪整个选项区域
cropped = img.crop((180, 780, 770, 1280))
output_path = os.path.join(output_dir, '2024_27_options.png')
cropped.save(output_path)
print(f'已保存: 2024_27_options.png')

# 2024-44题的配图已经裁剪为2024_40.png，复制为2024_44.png
src = os.path.join(output_dir, '2024_40.png')
dst = os.path.join(output_dir, '2024_44.png')
if os.path.exists(src):
    shutil.copy(src, dst)
    print(f'已复制: 2024_40.png -> 2024_44.png')
else:
    print(f'文件不存在: {src}')

print('\n配图裁剪完成')
