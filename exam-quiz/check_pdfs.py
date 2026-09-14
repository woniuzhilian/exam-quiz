import pymupdf

pdfs = [
    r'D:\证件相关\一级岩土工程师\真题空白卷\公共基础真题+2017.pdf',
    r'D:\证件相关\一级岩土工程师\真题空白卷\公共基础真题+2018.pdf',
    r'D:\证件相关\一级岩土工程师\真题空白卷\公共基础真题+2021.pdf',
    r'D:\证件相关\一级岩土工程师\真题空白卷\2023年公共基础+真题.pdf',
    r'D:\证件相关\一级岩土工程师\真题空白卷\2024年注册勘察设计岩土专业基础真题答案.pdf',
]

for pdf_path in pdfs:
    print(f"\n=== {pdf_path.split(chr(92))[-1]} ===")
    try:
        doc = pymupdf.open(pdf_path)
        print(f"  页数: {len(doc)}")
        # 检查前3页是否有文本
        for i in range(min(3, len(doc))):
            text = doc[i].get_text()
            print(f"  第{i+1}页文本长度: {len(text)}")
            if text.strip():
                print(f"  前100字: {text[:100]}")
        doc.close()
    except Exception as e:
        print(f"  错误: {e}")
