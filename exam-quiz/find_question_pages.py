import json

# 读取题目截图映射
with open(r'D:\应用程序开发\刷题\exam-quiz\question_images\question_image_mapping.json', 'r', encoding='utf-8') as f:
    mapping = json.load(f)

# 查找需要的题目
target_questions = [
    ('2021', 21), ('2021', 22), ('2022', 58), ('2022', 60)
]

for year, qnum in target_questions:
    key = f"{year}-{qnum}"
    if key in mapping:
        info = mapping[key]
        print(f"{key}:")
        print(f"  题目页: {info.get('question_page', 'N/A')}")
        print(f"  解析页: {info.get('answer_page', 'N/A')}")
    else:
        print(f"{key}: 未找到映射")
