import json, re

# 从原始题库读取
with open(r'D:\应用程序开发\刷题\all_questions_merged.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 检查包含逗号的配图标记
print("=== 包含多个文件名的配图标记 ===")
count = 0
for q in data:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        # 匹配【配图：...】或【见本题选项配图：...】
        for m in re.finditer(r'【(?:配图|见本题选项配图)[：:]([^】]+)】', text):
            filenames = m.group(1)
            if ',' in filenames or '，' in filenames:
                count += 1
                if count <= 10:
                    print(f'  {q["bigSubject"]} {q["year"]}-{q["id"]} {field}: [{filenames}]')

print(f'\n总计: {count} 处包含多个文件名')
