import json, re, os

img_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'
existing_files = set(os.listdir(img_dir))

# 建立无扩展名的文件名映射
name_no_ext = {}
for f in existing_files:
    name = os.path.splitext(f)[0]
    name_no_ext[name] = f

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 检查所有<img>引用的图片
missing = []
extension_mismatch = []
for q in data:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        imgs = re.findall(r'<img[^>]+src="/images/([^"]+)"', text)
        for img in imgs:
            if img not in existing_files:
                name = os.path.splitext(img)[0]
                if name in name_no_ext:
                    extension_mismatch.append((img, name_no_ext[name]))
                else:
                    missing.append((q['bigSubject'], q['year'], q['id'], img))

print(f'扩展名不匹配（可修复）: {len(extension_mismatch)}')
for old, new in extension_mismatch[:10]:
    print(f'  {old} -> {new}')

print(f'\n完全缺失（无法修复）: {len(missing)}')
seen = set()
for item in missing:
    if item[3] not in seen:
        seen.add(item[3])
        print(f'  {item[0]} {item[1]}-{item[2]}: {item[3]}')
    if len(seen) >= 15:
        break
