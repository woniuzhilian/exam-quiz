import pymupdf
import os

# 检查真题空白卷中的PDF
pdf_dir = r'D:\证件相关\一级岩土工程师\真题空白卷'
pdf_files = [
    '岩土专业基础历年真题解析册（2024版）.pdf',
    '岩土专业基础历年真题试题册（2024版）.pdf',
]

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_dir, pdf_file)
    if os.path.exists(pdf_path):
        doc = pymupdf.open(pdf_path)
        print(f"\n=== {pdf_file} ===")
        print(f"页数: {len(doc)}")
        # 检查前3页是否有文本
        for i in range(min(3, len(doc))):
            page = doc[i]
            text = page.get_text()
            print(f"第{i+1}页文本长度: {len(text)}")
            if text:
                print(f"前100字: {text[:100]}")
        doc.close()
    else:
        print(f"\n{pdf_file} 不存在")
