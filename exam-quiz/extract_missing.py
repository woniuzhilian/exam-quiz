import pymupdf
import json, re

# 提取缺失的公共基础题目
missing_questions = [
    ('2017', 40, r'D:\证件相关\一级岩土工程师\真题空白卷\公共基础真题+2017.pdf'),
    ('2017', 56, r'D:\证件相关\一级岩土工程师\真题空白卷\公共基础真题+2017.pdf'),
    ('2018', 19, r'D:\证件相关\一级岩土工程师\真题空白卷\公共基础真题+2018.pdf'),
    ('2018', 64, r'D:\证件相关\一级岩土工程师\真题空白卷\公共基础真题+2018.pdf'),
    ('2021', 14, r'D:\证件相关\一级岩土工程师\真题空白卷\公共基础真题+2021.pdf'),
    ('2021', 58, r'D:\证件相关\一级岩土工程师\真题空白卷\公共基础真题+2021.pdf'),
    ('2023', 34, r'D:\证件相关\一级岩土工程师\真题空白卷\2023年公共基础+真题.pdf'),
]

results = []

for year, qnum, pdf_path in missing_questions:
    print(f"\n=== 查找 {year}-{qnum} ===")
    doc = pymupdf.open(pdf_path)
    found = False
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        
        # 查找题号
        pattern = rf'(?:^|\n)\s*{qnum}[\.、\s]'
        if re.search(pattern, text):
            print(f"  在第{page_num+1}页找到")
            # 提取该题及后续内容
            lines = text.split('\n')
            question_lines = []
            capture = False
            for line in lines:
                if re.match(rf'^\s*{qnum}[\.、\s]', line):
                    capture = True
                elif capture and re.match(r'^\s*\d+[\.、\s]', line) and not re.match(rf'^\s*{qnum}[\.、\s]', line):
                    break
                if capture:
                    question_lines.append(line)
            
            question_text = '\n'.join(question_lines)
            print(f"  内容: {question_text[:200]}")
            results.append({
                'year': year,
                'qnum': qnum,
                'page': page_num + 1,
                'text': question_text,
                'pdf': pdf_path
            })
            found = True
            break
    
    if not found:
        print(f"  未找到")
    doc.close()

# 保存结果
with open(r'D:\应用程序开发\刷题\exam-quiz\missing_questions.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n共找到 {len(results)}/7 道缺失题目")
