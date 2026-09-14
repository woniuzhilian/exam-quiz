import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离公共基础和专业基础
public = [q for q in questions if q['bigSubject'] == '公共基础']
pro = [q for q in questions if q['bigSubject'] == '专业基础']

# 检查2021年的题目
year_2021 = [q for q in public if q['year'] == '2021']
year_2021_sorted = sorted(year_2021, key=lambda x: x.get('yearQnum', 0))

print("修复前2021年第18-22题:")
for q in year_2021_sorted[17:22]:
    print(f"  {q['year']}-{q.get('yearQnum')}: {q['question'][:60]}...")

# 找到需要添加的2021-19题
# 从PDF截图来看，2021-19题是：若矩阵A = [[1,0,0],[0,-1,-1],[0,0,1]], I = [[1,0,0],[0,1,0],[0,0,1]], 则矩阵(A - 2I)⁻¹(A² - 4I)为
# 选项A: [[3,0,0],[0,1,-1],[0,0,3]]
# 选项B: [[3,0,0],[0,1,0],[0,0,3]]
# 选项C: [[3,0,0],[0,1,1],[0,0,3]]
# 选项D: [[2,0,0],[0,-2,-2],[0,-2,2]]

new_question_19 = {
    'id': 0,  # 后面重新分配
    'bigSubject': '公共基础',
    'smallSubject': '线性代数',
    'year': '2021',
    'yearQnum': 19,
    'question': '若矩阵$A=\\begin{pmatrix} 1 & 0 & 0 \\\\ 0 & -1 & -1 \\\\ 0 & 0 & 1 \\end{pmatrix}$，$I=\\begin{pmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$，则矩阵$(A-2I)^{-1}(A^2-4I)$为：（　　）。',
    'A': '$\\begin{pmatrix} 3 & 0 & 0 \\\\ 0 & 1 & -1 \\\\ 0 & 0 & 3 \\end{pmatrix}$',
    'B': '$\\begin{pmatrix} 3 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 3 \\end{pmatrix}$',
    'C': '$\\begin{pmatrix} 3 & 0 & 0 \\\\ 0 & 1 & 1 \\\\ 0 & 0 & 3 \\end{pmatrix}$',
    'D': '$\\begin{pmatrix} 2 & 0 & 0 \\\\ 0 & -2 & -2 \\\\ 0 & -2 & 2 \\end{pmatrix}$',
    'answer': 'A',
    'analysis': '矩阵运算。$(A-2I)^{-1}(A^2-4I) = (A-2I)^{-1}(A-2I)(A+2I) = A+2I = \\begin{pmatrix} 3 & 0 & 0 \\\\ 0 & 1 & -1 \\\\ 0 & 0 & 3 \\end{pmatrix}$，选A。'
}

# 将2021年第19题及以后的题号加1
for q in year_2021_sorted:
    if q.get('yearQnum', 0) >= 19:
        q['yearQnum'] = q['yearQnum'] + 1

# 添加新的2021-19题
public.append(new_question_19)

# 重新排序公共基础
public.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))

# 重新分配id
for i, q in enumerate(public):
    q['id'] = i + 1

# 专业基础id从1434开始
for i, q in enumerate(pro):
    q['id'] = 1434 + i

# 合并
final = public + pro

# 验证
year_2021_new = [q for q in public if q['year'] == '2021']
year_2021_new_sorted = sorted(year_2021_new, key=lambda x: x.get('yearQnum', 0))

print("\n修复后2021年第18-23题:")
for q in year_2021_new_sorted[17:23]:
    print(f"  {q['year']}-{q.get('yearQnum')}: {q['question'][:60]}...")

print(f"\n2021年题数: {len(year_2021_new)}")
qnums = [q.get('yearQnum') for q in year_2021_new_sorted]
print(f"题号范围: {min(qnums)} - {max(qnums)}")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print("\n题库已更新")
