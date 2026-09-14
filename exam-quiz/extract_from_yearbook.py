import fitz
import re
import json

def extract_questions_from_pdf(pdf_path, start_page, end_page, year):
    """从PDF中提取指定年份的题目"""
    doc = fitz.open(pdf_path)
    all_text = ""
    
    # PDF文件页码 = PDF内页码 + 4
    for i in range(start_page + 3, end_page + 4):
        if i < len(doc):
            text = doc[i].get_text()
            # 移除页眉页脚
            lines = text.split('\n')
            cleaned_lines = []
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if '微信公众号' in line or '基础学习交流' in line or '小注教育' in line:
                    continue
                # 移除纯数字页码
                if re.match(r'^\d+$', line) and len(line) <= 3:
                    continue
                cleaned_lines.append(line)
            all_text += '\n'.join(cleaned_lines) + '\n'
    
    doc.close()
    
    # 解析题目
    questions = []
    # 匹配题号模式：数字、
    pattern = r'(\d+)[、.](.*?)(?=\d+[、.]|$)'
    matches = re.findall(pattern, all_text, re.DOTALL)
    
    for match in matches:
        qnum = int(match[0])
        content = match[1].strip()
        
        # 分离题干和选项
        # 匹配（A）（B）（C）（D）
        option_pattern = r'[（(][A-D][）)](.*?)(?=[（(][A-D][）)]|$)'
        option_matches = re.findall(option_pattern, content, re.DOTALL)
        
        if len(option_matches) >= 4:
            # 题干是选项之前的部分
            first_option_pos = content.find('（A')
            if first_option_pos == -1:
                first_option_pos = content.find('(A')
            question_text = content[:first_option_pos].strip()
            
            # 清理题干中的换行和多余空格
            question_text = re.sub(r'\s+', ' ', question_text).strip()
            
            options = []
            for opt in option_matches[:4]:
                opt = re.sub(r'\s+', ' ', opt).strip()
                options.append(opt)
            
            questions.append({
                'yearQnum': qnum,
                'question': question_text,
                'A': options[0] if len(options) > 0 else '',
                'B': options[1] if len(options) > 1 else '',
                'C': options[2] if len(options) > 2 else '',
                'D': options[3] if len(options) > 3 else ''
            })
    
    return questions

# 各年份的页码范围（PDF内页码）
year_pages = {
    '2016': (10, 18),
    '2017': (19, 27),
    '2018': (28, 36),
    '2019': (37, 45),
    '2020': (46, 54),
    '2021': (55, 63),
    '2022': (64, 71),
    '2022补': (72, 81),
    '2023': (82, 94),
}

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\岩土专业基础历年真题试题册（2024版）.pdf'

# 提取所有年份的题目
all_questions = {}
for year, (start, end) in year_pages.items():
    questions = extract_questions_from_pdf(pdf_path, start, end, year)
    all_questions[year] = questions
    print(f"{year}: 提取到{len(questions)}道题")
    # 打印题号
    qnums = [q['yearQnum'] for q in questions]
    print(f"  题号: {qnums}")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_from_yearbook.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print("\n已保存到 pro_questions_from_yearbook.json")
