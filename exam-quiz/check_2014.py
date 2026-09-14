import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 检查2014年公共基础的题目
print("=== 2014年公共基础题目（id范围121-240）===")
count = 0
for q in data:
    if q['bigSubject'] == '公共基础' and q['year'] == '2014':
        count += 1
        if count <= 15 or q['id'] in [122, 129]:
            print(f"  id={q['id']}, smallSubject={q['smallSubject']}, question={q['question'][:60]}")

print(f"\n2014年总题数: {count}")

# 检查id=122的题目详情
print("\n=== id=122 详情 ===")
for q in data:
    if q['id'] == 122 and q['bigSubject'] == '公共基础':
        print(f"year={q['year']}, smallSubject={q['smallSubject']}")
        print(f"question={q['question'][:200]}")
        print(f"A={q['A'][:200]}")
        print(f"B={q['B'][:200]}")
        print(f"answer={q['answer']}")
        break
