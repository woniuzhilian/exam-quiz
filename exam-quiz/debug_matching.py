import json
import os
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 查找2013-93题
for q in questions:
    if q['year'] == '2013' and q.get('yearQnum') == 93:
        print('找到2013-93题')
        print('  选项A:', q.get('A', ''))
        print('  选项B:', q.get('B', ''))
        print('  选项C:', q.get('C', ''))
        print('  选项D:', q.get('D', ''))
        break

# 检查图片文件名匹配
image_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'
image_map = {}
for filename in os.listdir(image_dir):
    if '2013_93' in filename:
        match = re.match(r'id\d+_(\d+)_(\d+)_(\d+)\.(png|jpg|jpeg)', filename)
        if match:
            print(f'匹配到: {filename} -> year={match.group(1)}, qnum={match.group(2)}, index={match.group(3)}')
            year = match.group(1)
            qnum = int(match.group(2))
            index = int(match.group(3))
            key = (year, qnum)
            if key not in image_map:
                image_map[key] = {}
            image_map[key][index] = f'/images/{filename}'
        else:
            print(f'未匹配: {filename}')

print('\nimage_map中的键:', list(image_map.keys()))
print('2013-93的配图:', image_map.get(('2013', 93), '未找到'))
