import json
import re
import pymupdf

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 需要修复的题目列表
issues = [
    ('2014', 13), ('2014', 23), ('2014', 25), ('2014', 38),
    ('2016', 19), ('2016', 23), ('2017', 8), ('2017', 21),
    ('2018', 12), ('2018', 20), ('2018', 24), ('2018', 27),
    ('2019', 22), ('2019', 23), ('2019', 39), ('2019', 92),
    ('2020', 44), ('2020', 92), ('2021', 21), ('2021', 38),
    ('2022', 35), ('2022', 39), ('2022补', 2), ('2023', 82),
    ('2024', 51), ('2024', 52), ('2024', 57),
]

# 打开PDF
doc = pymupdf.open(r'D:\证件相关\一级岩土工程师\公共基础分类版真题详解（13~24）_题目.pdf')

# 找到每道题在PDF中的位置并渲染
for year, qnum in issues:
    # 在PDF中搜索题目
    found = False
    for i, page in enumerate(doc):
        text = page.get_text()
        marker = f'【{year}-{qnum}】'
        if marker in text:
            # 渲染这一页
            pix = page.get_pixmap(dpi=200)
            filename = f'D:\\应用程序开发\\刷题\\exam-quiz\\unmatched_images\\{year}-{qnum}_question.png'
            pix.save(filename)
            print(f'已保存 {year}-{qnum} 到第 {i+1} 页')
            found = True
            break

    if not found:
        print(f'未找到 {year}-{qnum}')

doc.close()
print('完成')
