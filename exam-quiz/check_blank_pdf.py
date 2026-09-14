import pymupdf
import re

# 检查空白卷PDF
pdf_paths = [
    r'D:\证件相关\一级岩土工程师\真题空白卷\公共基础真题+2017.pdf',
    r'D:\证件相关\一级岩土工程师\真题空白卷\公共基础真题+2018.pdf',
]

for pdf_path in pdf_paths:
    print(f"\n=== {pdf_path.split(chr(92))[-1]} ===")
    try:
        doc = pymupdf.open(pdf_path)
        print(f"共{len(doc)}页")

        # 检查前3页的题号格式
        for page_idx in range(min(3, len(doc))):
            page = doc[page_idx]
            text = page.get_text()
            # 查找题号
            qnums = re.findall(r'(?:^|\n)\s*(\d+)\s*[.、]', text[:500])
            print(f"  第{page_idx+1}页前500字符中的题号: {qnums[:10]}")
            print(f"  内容预览: {text[:200].replace(chr(10), ' ')}")

        doc.close()
    except Exception as e:
        print(f"  错误: {e}")
