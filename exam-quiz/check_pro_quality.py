import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 只检查专业基础
pro_questions = [q for q in questions if q['bigSubject'] == '专业基础']

# 检查可能混入公共基础的题目关键词
public_keywords = [
    '电视机', '概率', '数学期望', '矩阵', '微分方程', '积分', '导数',
    '极限', '级数', '向量', '行列式', '特征值', '特征向量',
    '理想气体', '热力学', '波动', '光学', '电路', '变压器',
    '电动机', 'KCL', 'KVL', '真值表', '逻辑函数',
    '化学', '分子', '原子', '电解', '原电池',
    '计算机', '进制', '操作系统', '网络',
    '经济', '投资', '净现值', '内部收益率',
]

print("=== 可能混入公共基础的专业基础题目 ===")
suspicious = []
for q in pro_questions:
    qid = f"{q['year']}-{q.get('yearQnum')}"
    text = q['question'] + q['A'] + q['B'] + q['C'] + q['D'] + q['analysis']
    for keyword in public_keywords:
        if keyword in text:
            suspicious.append((qid, q['smallSubject'], keyword, q['question'][:80]))
            break

for item in suspicious[:50]:
    print(f"{item[0]} ({item[1]}): 关键词={item[2]}")
    print(f"  题干: {item[3]}")

print(f"\n总计: {len(suspicious)}道题可能有问题")
