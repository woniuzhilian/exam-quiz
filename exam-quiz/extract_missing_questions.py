import fitz
import re
import json

def get_year_text(pdf_path, year_start_page, year_end_page):
    """获取某年份的全部文本"""
    doc = fitz.open(pdf_path)
    all_text = ""
    
    for i in range(year_start_page + 3, year_end_page + 4):
        if i < len(doc):
            text = doc[i].get_text()
            all_text += text + "\n"
    
    doc.close()
    return all_text

def extract_specific_question(text, qnum):
    """从文本中提取指定题号的题目"""
    # 匹配题号
    pattern = rf'(?:^|\n){qnum}[、.](.*?)(?=\n\d+[、.]|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    
    if not match:
        return None
    
    content = match.group(1).strip()
    
    # 分离题干和选项
    option_pattern = r'[（(][A-D][）)](.*?)(?=[（(][A-D][）)]|$)'
    option_matches = re.findall(option_pattern, content, re.DOTALL)
    
    if len(option_matches) >= 4:
        first_option_pos = -1
        for marker in ['（A', '(A', '（A）', '(A)']:
            pos = content.find(marker)
            if pos != -1:
                first_option_pos = pos
                break
        
        if first_option_pos == -1:
            return None
            
        question_text = content[:first_option_pos].strip()
        question_text = re.sub(r'\s+', ' ', question_text).strip()
        
        options = []
        for opt in option_matches[:4]:
            opt = re.sub(r'\s+', ' ', opt).strip()
            options.append(opt)
        
        return {
            'yearQnum': qnum,
            'question': question_text,
            'A': options[0],
            'B': options[1],
            'C': options[2],
            'D': options[3]
        }
    
    return None

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\岩土专业基础历年真题试题册（2024版）.pdf'

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

# 需要提取的题目
missing_questions = {
    '2016': [13, 14, 15, 16, 45],
    '2017': [13, 14, 15, 16],
    '2018': [13, 14, 15, 16],
    '2019': [13, 14, 15, 16, 51, 52, 53],
    '2020': [13, 14, 15, 16],
    '2021': [13, 14, 15, 16],
    '2022': [13, 14, 15, 16, 44],
    '2022补': [13, 14, 15, 16],
    '2023': [13, 14, 15, 16],
}

extracted = {}

for year, qnums in missing_questions.items():
    start, end = year_pages[year]
    text = get_year_text(pdf_path, start, end)
    
    year_questions = []
    for qnum in qnums:
        q = extract_specific_question(text, qnum)
        if q:
            year_questions.append(q)
            print(f"{year}-{qnum}: 提取成功 - {q['question'][:40]}...")
        else:
            print(f"{year}-{qnum}: 提取失败")
    
    extracted[year] = year_questions

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_missing_questions.json', 'w', encoding='utf-8') as f:
    json.dump(extracted, f, ensure_ascii=False, indent=2)

print(f"\n共提取到 {sum(len(v) for v in extracted.values())} 道题")
