import fitz
import re
import json

def get_year_text(pdf_path, year_start_page, year_end_page):
    """获取某年份的全部文本"""
    doc = fitz.open(pdf_path)
    all_text = ""
    
    # PDF文件页码 = PDF内页码 + 5
    for i in range(year_start_page + 4, year_end_page + 5):
        if i < len(doc):
            text = doc[i].get_text()
            all_text += text + "\n"
    
    doc.close()
    return all_text

def extract_specific_answer(text, qnum):
    """从文本中提取指定题号的答案和解析"""
    # 匹配题号模式：题号、小注教育答案：【X】
    pattern = rf'(?:^|\n){qnum}[、.].*?答案[：:]\s*[【\[]([A-D])[】\]](.*?)(?=\n\d+[、.]|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    
    if not match:
        # 尝试另一种格式
        pattern2 = rf'(?:^|\n){qnum}[、.].*?([A-D])[】\]]\s*解题分析[：:](.*?)(?=\n\d+[、.]|\Z)'
        match = re.search(pattern2, text, re.DOTALL)
        if not match:
            return None
        answer = match.group(1)
        analysis = match.group(2).strip()
    else:
        answer = match.group(1)
        analysis = match.group(2).strip()
        # 移除"解题分析："前缀
        analysis = re.sub(r'^解题分析[：:]\s*', '', analysis)
    
    # 清理解析文本
    analysis = re.sub(r'\s+', ' ', analysis).strip()
    
    return {
        'answer': answer,
        'analysis': analysis
    }

pdf_path = r'D:\应用程序开发\刷题\题目和答案pdf\岩土专业基础历年真题解析册（2024版）.pdf'

# 各年份的页码范围（PDF内页码）
year_pages = {
    '2016': (19, 33),
    '2017': (34, 47),
    '2018': (48, 62),
    '2019': (63, 82),
    '2020': (83, 98),
    '2021': (99, 113),
    '2022': (114, 127),
    '2022补': (128, 142),
    '2023': (143, 161),
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

extracted_answers = {}

for year, qnums in missing_questions.items():
    start, end = year_pages[year]
    text = get_year_text(pdf_path, start, end)
    
    year_answers = {}
    for qnum in qnums:
        ans = extract_specific_answer(text, qnum)
        if ans:
            year_answers[str(qnum)] = ans
            print(f"{year}-{qnum}: 答案={ans['answer']}, 解析={ans['analysis'][:40]}...")
        else:
            print(f"{year}-{qnum}: 提取失败")
    
    extracted_answers[year] = year_answers

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_missing_answers.json', 'w', encoding='utf-8') as f:
    json.dump(extracted_answers, f, ensure_ascii=False, indent=2)

total = sum(len(v) for v in extracted_answers.values())
print(f"\n共提取到 {total} 道题的答案解析")
