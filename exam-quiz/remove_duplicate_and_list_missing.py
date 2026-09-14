import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 删除2013-63重复题目（格式不规范的那道）
# 保留2013-64（格式规范的那道）
public = [q for q in questions if q['bigSubject'] == '公共基础']
pro = [q for q in questions if q['bigSubject'] == '专业基础']

# 找到2013-63题（格式不规范的那道）
to_remove = None
for q in public:
    if q['year'] == '2013' and q.get('yearQnum') == 63:
        if '如图两根圆轴' in q.get('question', '') and '横截面面积相同' in q.get('question', ''):
            to_remove = q
            break

if to_remove:
    public.remove(to_remove)
    print(f"已删除重复题目: 2013-63")
    print(f"  题干: {to_remove.get('question', '')[:80]}...")

# 重新排序和分配id
public.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))
pro.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))

for i, q in enumerate(public):
    q['id'] = i + 1

pro_start = len(public) + 1
for i, q in enumerate(pro):
    q['id'] = pro_start + i

final = public + pro

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print(f"\n题库已更新，当前共 {len(final)} 道题")
print(f"  公共基础: {len(public)} 道")
print(f"  专业基础: {len(pro)} 道")

# 列出选项内容缺失的题目
print("\n\n选项内容缺失的题目清单（需要配图）:")
missing_options = []
for q in final:
    for field in ['A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if text in ['选项A', '选项B', '选项C', '选项D', 'A', 'B', 'C', 'D', '']:
            if q.get('A') and '<img' in q.get('A', ''):
                continue
            missing_options.append(q)
            break

for q in missing_options:
    print(f"  {q['year']}-{q.get('yearQnum', q['id'])} ({q['bigSubject']}): {q.get('question', '')[:60]}...")

print(f"\n共 {len(missing_options)} 道题需要补充选项配图")
