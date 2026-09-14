import json, os, re
from collections import Counter

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

images_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'

# 找出所有选项包含配图标记的题目
img_options = []
for q in questions:
    for field in ['A', 'B', 'C', 'D']:
        text = q.get(field, '')
        match = re.search(r'【见本题选项配图[:：]([^】]+)】', text)
        if match:
            img_file = match.group(1)
            img_path = os.path.join(images_dir, img_file)
            file_size = os.path.getsize(img_path) if os.path.exists(img_path) else 0
            img_options.append({
                'year': q['year'],
                'qnum': q.get('yearQnum', q['id']),
                'id': q['id'],
                'field': field,
                'img_file': img_file,
                'file_size': file_size,
                'smallSubject': q.get('smallSubject', ''),
                'question': q['question'][:100],
                'other_options': {k: q.get(k, '')[:50] for k in ['A','B','C','D'] if k != field}
            })

print(f"选项配图题目总数: {len(img_options)}")
print(f"\n按小科目分布:")
subject_counts = Counter(item['smallSubject'] for item in img_options)
for subj, count in subject_counts.most_common():
    print(f"  {subj or '(空)'}: {count}题")

print(f"\n按图片文件大小分布:")
size_ranges = {'<10KB': 0, '10-50KB': 0, '50-100KB': 0, '>100KB': 0, '不存在': 0}
for item in img_options:
    if item['file_size'] == 0:
        size_ranges['不存在'] += 1
    elif item['file_size'] < 10240:
        size_ranges['<10KB'] += 1
    elif item['file_size'] < 51200:
        size_ranges['10-50KB'] += 1
    elif item['file_size'] < 102400:
        size_ranges['50-100KB'] += 1
    else:
        size_ranges['>100KB'] += 1
for k, v in size_ranges.items():
    print(f"  {k}: {v}题")

# 输出前20道题的详细信息
print(f"\n=== 前20道选项配图题目详情 ===")
for item in img_options[:20]:
    print(f"\n{item['year']}-{item['qnum']} ({item['smallSubject']})")
    print(f"  题干: {item['question'][:80]}")
    print(f"  {item['field']}: 配图={item['img_file']} ({item['file_size']//1024}KB)")
    for k, v in item['other_options'].items():
        print(f"  {k}: {v}")
