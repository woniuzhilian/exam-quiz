import json, re, os

img_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'
existing_files = set(os.listdir(img_dir))

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 检查所有<img>引用
all_refs = set()
missing = []
for q in data:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        imgs = re.findall(r'<img[^>]+src="/images/([^"]+)"', text)
        for img in imgs:
            all_refs.add(img)
            if img not in existing_files:
                missing.append((q['bigSubject'], q['year'], q['id'], field, img))

print(f'题库中引用的不同图片数: {len(all_refs)}')
print(f'public/images中图片数: {len(existing_files)}')
print(f'缺失图片引用数: {len(missing)}')

if missing:
    print(f'\n缺失详情（去重后）:')
    seen = set()
    for item in missing:
        if item[4] not in seen:
            seen.add(item[4])
            print(f'  {item[4]} (首次出现在 {item[0]} {item[1]}-{item[2]} {item[3]})')
        if len(seen) >= 20:
            break

# 检查剩余的【】配图标记
remaining_markers = []
for q in data:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if '【' in text and '配图' in text:
            remaining_markers.append((q['bigSubject'], q['year'], q['id'], field, text[:100]))

print(f'\n剩余【】配图标记数: {len(remaining_markers)}')
if remaining_markers:
    print(f'示例（前10个）:')
    for r in remaining_markers[:10]:
        print(f'  {r[0]} {r[1]}-{r[2]} {r[3]}: {r[4]}')
