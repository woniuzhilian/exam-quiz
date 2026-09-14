import json

with open(r'D:\应用程序开发\刷题\exam-quiz\question_images\question_image_mapping.json', 'r', encoding='utf-8') as f:
    mapping = json.load(f)

# 查看几道题的映射
for key in ['2014-23', '2017-23', '2019-23', '2018-81', '2020-62', '2022补-18', '2023-61', '2024-2']:
    if key in mapping:
        qp = mapping[key]['question_page']
        ap = mapping[key]['analysis_page']
        print(f'{key}: question_page={qp}, analysis_page={ap}')
