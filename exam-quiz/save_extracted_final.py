import json

# 读取已提取的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

# 新增题目（第94页）
new_questions = [
    # 岩体力学在岩基工程中的应用 续
    {"year": "2024", "yearQnum": 54, "smallSubject": "岩体力学在岩基工程中的应用", "question": "对于脆性地基，若已知岩石单轴抗压强度为$R_c$，则基于格里菲斯理论确定岩基的极限承载$Q_f$为（　　）。", "A": "$3R_c$", "B": "$9R_c$", "C": "$12R_c$", "D": "$24R_c$"},
]

# 合并
all_questions = extracted + new_questions

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"题目提取完成，共 {len(all_questions)} 道题")

# 统计各年份题目数量
from collections import Counter
year_counts = Counter(q['year'] for q in all_questions)
print("\n各年份题目数量：")
for year, count in sorted(year_counts.items()):
    print(f"  {year}: {count}道")
