from docx import Document
import os
from PIL import Image
import io

docx_path = r'D:\证件相关\一级岩土工程师\真题空白卷\截图.docx'
output_dir = r'D:\应用程序开发\刷题\exam-quiz\missing_images'
os.makedirs(output_dir, exist_ok=True)

doc = Document(docx_path)

# 提取所有图片
image_count = 0
for rel in doc.part.rels.values():
    if "image" in rel.target_ref:
        image_count += 1
        image_data = rel.target_part.blob
        image_ext = rel.target_ref.split('.')[-1]
        image_path = os.path.join(output_dir, f'image_{image_count}.{image_ext}')
        with open(image_path, 'wb') as f:
            f.write(image_data)
        print(f"保存图片: {image_path} ({len(image_data)} bytes)")

print(f"\n共提取 {image_count} 张图片")
