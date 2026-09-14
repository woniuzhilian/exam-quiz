import pymupdf
import json
import os

# 路径
question_pdf = r'D:\证件相关\一级岩土工程师\公共基础分类版真题详解（13~24）_题目.pdf'
analysis_pdf = r'D:\证件相关\一级岩土工程师\公共基础分类版真题详解（13~24）_答案解析.pdf'
output_dir = r'D:\应用程序开发\刷题\exam-quiz\question_images'

# 读取映射
with open(os.path.join(output_dir, 'page_mapping.json'), 'r', encoding='utf-8') as f:
    mapping = json.load(f)

question_page_map = mapping['question']
analysis_page_map = mapping['analysis']

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 只处理公共基础题目
public_questions = [q for q in questions if q['bigSubject'] == '公共基础']

# 收集需要渲染的页面（去重）
question_pages = set()
analysis_pages = set()
question_keys = []

for q in public_questions:
    key = f"{q['year']}-{q.get('yearQnum')}"
    if key in question_page_map:
        question_pages.add(question_page_map[key])
        question_keys.append((key, question_page_map[key], 'question'))
    if key in analysis_page_map:
        analysis_pages.add(analysis_page_map[key])
        question_keys.append((key, analysis_page_map[key], 'analysis'))

print(f"需要渲染的题目页面数: {len(question_pages)}")
print(f"需要渲染的解析页面数: {len(analysis_pages)}")
print(f"总题目数: {len(public_questions)}")

# 批量渲染题目页面
print("\n开始渲染题目页面...")
doc_q = pymupdf.open(question_pdf)
count = 0
for page_num in sorted(question_pages):
    page = doc_q[page_num - 1]  # 页码从0开始
    pix = page.get_pixmap(dpi=150)
    output_path = os.path.join(output_dir, f'page_q_{page_num:03d}.png')
    pix.save(output_path)
    count += 1
    if count % 50 == 0:
        print(f"  已渲染 {count}/{len(question_pages)} 个题目页面")
doc_q.close()
print(f"题目页面渲染完成，共 {count} 个")

# 批量渲染解析页面
print("\n开始渲染解析页面...")
doc_a = pymupdf.open(analysis_pdf)
count = 0
for page_num in sorted(analysis_pages):
    page = doc_a[page_num - 1]
    pix = page.get_pixmap(dpi=150)
    output_path = os.path.join(output_dir, f'page_a_{page_num:03d}.png')
    pix.save(output_path)
    count += 1
    if count % 50 == 0:
        print(f"  已渲染 {count}/{len(analysis_pages)} 个解析页面")
doc_a.close()
print(f"解析页面渲染完成，共 {count} 个")

# 建立题号到图片文件的映射
print("\n建立题号到图片文件的映射...")
question_image_map = {}
for q in public_questions:
    key = f"{q['year']}-{q.get('yearQnum')}"
    question_image_map[key] = {
        'question_page': question_page_map.get(key),
        'analysis_page': analysis_page_map.get(key),
        'question_image': f'page_q_{question_page_map[key]:03d}.png' if key in question_page_map else None,
        'analysis_image': f'page_a_{analysis_page_map[key]:03d}.png' if key in analysis_page_map else None,
    }

with open(os.path.join(output_dir, 'question_image_mapping.json'), 'w', encoding='utf-8') as f:
    json.dump(question_image_map, f, ensure_ascii=False, indent=2)

print("题号到图片文件的映射已保存")
print("\n全部完成！")
