import pymupdf
import json, re

# 从分类版真题PDF中查找68道匹配失败题目的页码
question_pdf = r'D:\证件相关\一级岩土工程师\公共基础分类版真题详解（13~24）_题目.pdf'
answer_pdf = r'D:\证件相关\一级岩土工程师\公共基础分类版真题详解（13~24）_答案解析.pdf'

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 找出匹配失败的题目
unmatched = [q for q in questions if not q.get('smallSubject') and q['bigSubject'] == '公共基础']
print(f"公共基础匹配失败题目: {len(unmatched)} 道")

# 打开题目PDF
doc_q = pymupdf.open(question_pdf)
doc_a = pymupdf.open(answer_pdf)

results = []
for q in unmatched:
    year = q['year']
    qnum = q.get('yearQnum', q['id'])
    year_qnum = f"{year}-{qnum}"
    
    # 在题目PDF中查找
    q_page = None
    for page_num in range(len(doc_q)):
        text = doc_q[page_num].get_text()
        if f'【{year}-{qnum:02d}】' in text or f'【{year}-{qnum}】' in text:
            q_page = page_num + 1
            break
    
    # 在答案PDF中查找
    a_page = None
    for page_num in range(len(doc_a)):
        text = doc_a[page_num].get_text()
        if f'【{year}-{qnum:02d}】' in text or f'【{year}-{qnum}】' in text:
            a_page = page_num + 1
            break
    
    results.append({
        'year_qnum': year_qnum,
        'question_page': q_page,
        'answer_page': a_page,
        'question': q['question'][:60],
    })
    print(f"{year_qnum}: 题目PDF第{q_page}页, 答案PDF第{a_page}页")

doc_q.close()
doc_a.close()

# 保存结果
with open(r'D:\应用程序开发\刷题\exam-quiz\unmatched_pages.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n共标注 {len(results)} 道题的页码")
