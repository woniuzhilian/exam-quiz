import pymupdf
import re, os

pdf_paths = [
    r'D:\证件相关\一级岩土工程师\真题空白卷\岩土专业基础历年真题解析册（2024版）.pdf',
    r'D:\证件相关\一级岩土工程师\真题空白卷\岩土专业基础历年真题试题册（2024版）.pdf',
]

for pdf_path in pdf_paths:
    print(f"\n=== {os.path.basename(pdf_path)} ===")
    try:
        doc = pymupdf.open(pdf_path)
        print(f"共{len(doc)}页")

        # 检查前3页
        for page_idx in range(min(3, len(doc))):
            page = doc[page_idx]
            text = page.get_text()
            if text.strip():
                qnums = re.findall(r'(?:^|\n)\s*(\d+)\s*[.、]', text[:500])
                print(f"  第{page_idx+1}页题号: {qnums[:10]}")
                print(f"  内容: {text[:200].replace(chr(10), ' ')}")
            else:
                # 检查是否有图片
                images = page.get_images()
                print(f"  第{page_idx+1}页: 无文本, {len(images)}张图片（可能是扫描件）")

        doc.close()
    except Exception as e:
        print(f"  错误: {e}")
