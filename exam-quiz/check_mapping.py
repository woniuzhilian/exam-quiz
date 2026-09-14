import json

with open(r'D:\应用程序开发\刷题\exam-quiz\question_images\question_image_mapping.json', 'r', encoding='utf-8') as f:
    mapping = json.load(f)

# 查看几道题的映射
for key in ['2013-71', '2014-85', '2016-81', '2017-19', '2018-62', '2018-65', '2019-69', '2020-62']:
    if key in mapping:
        qp = mapping[key]['question_page']
        ap = mapping[key]['analysis_page']
        print(f'{key}: question_page={qp}, analysis_page={ap}')
