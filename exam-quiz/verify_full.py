import json, os, re

# 验证题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'题库总题数: {len(data)}')
pub = [q for q in data if q['bigSubject'] == '公共基础']
prof = [q for q in data if q['bigSubject'] == '专业基础']
print(f'公共基础: {len(pub)}题, 专业基础: {len(prof)}题')

# 验证字段完整性和answer
errors = []
for q in data:
    for field in ['id','bigSubject','smallSubject','year','question','A','B','C','D','answer','analysis']:
        if field not in q:
            errors.append(f'{q["bigSubject"]} id={q.get("id")} 缺少字段: {field}')
    if q['answer'] not in ['A','B','C','D']:
        errors.append(f'{q["bigSubject"]} id={q["id"]} answer非法: {q["answer"]}')

if errors:
    print(f'\n字段错误: {len(errors)}个')
    for e in errors[:10]:
        print(f'  {e}')
else:
    print('字段完整性和answer校验: 通过')

# 统计引用图片的题目
img_questions = []
for q in data:
    imgs = re.findall(r'<img[^>]+src="([^"]+)"', q.get('question',''))
    for opt in ['A','B','C','D']:
        imgs += re.findall(r'<img[^>]+src="([^"]+)"', q.get(opt,''))
    if imgs:
        img_questions.append((q['bigSubject'], q['year'], q['id'], imgs))

print(f'\n引用图片的题目: {len(img_questions)}道')

# 检查图片文件是否存在
img_dir = r'D:\应用程序开发\刷题\exam-quiz\public\images'
existing = set(os.listdir(img_dir))
missing = []
for subj, year, qid, imgs in img_questions:
    for img in imgs:
        fname = os.path.basename(img)
        if fname not in existing:
            missing.append(f'{subj} {year}-{qid}: {fname}')

print(f'public/images目录文件数: {len(existing)}')
if missing:
    print(f'缺失图片: {len(missing)}个')
    for m in missing[:20]:
        print(f'  {m}')
else:
    print('所有引用图片均存在')
