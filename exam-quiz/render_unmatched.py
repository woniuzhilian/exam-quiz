import pymupdf
import json, os

question_pdf = r'D:\证件相关\一级岩土工程师\公共基础分类版真题详解（13~24）_题目.pdf'
answer_pdf = r'D:\证件相关\一级岩土工程师\公共基础分类版真题详解（13~24）_答案解析.pdf'
output_dir = r'D:\应用程序开发\刷题\exam-quiz\unmatched_images'
os.makedirs(output_dir, exist_ok=True)

with open(r'D:\应用程序开发\刷题\exam-quiz\unmatched_pages.json', 'r', encoding='utf-8') as f:
    unmatched = json.load(f)

doc_q = pymupdf.open(question_pdf)
doc_a = pymupdf.open(answer_pdf)

for item in unmatched:
    year_qnum = item['year_qnum']
    q_page = item['question_page']
    a_page = item['answer_page']
    
    # 渲染题目页
    if q_page:
        page = doc_q[q_page - 1]
        pix = page.get_pixmap(dpi=200)
        img_path = os.path.join(output_dir, f'{year_qnum}_question.png')
        pix.save(img_path)
        print(f"已渲染题目: {year_qnum} -> 第{q_page}页")
    
    # 渲染答案页
    if a_page and a_page != 'None':
        page = doc_a[a_page - 1]
        pix = page.get_pixmap(dpi=200)
        img_path = os.path.join(output_dir, f'{year_qnum}_answer.png')
        pix.save(img_path)
        print(f"已渲染答案: {year_qnum} -> 第{a_page}页")

doc_q.close()
doc_a.close()
print(f"\n共渲染 {len(unmatched)} 道题的页面")
