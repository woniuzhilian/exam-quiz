import json
import re

# 读取合并的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_missing_merged.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 深度清理文本
def deep_clean(text):
    # 移除页眉页脚
    text = re.sub(r'微信公众号[：:]?\s*小注基础', '', text)
    text = re.sub(r'基础学习交流\s*QQ\s*群[：:]?\s*\d+', '', text)
    text = re.sub(r'小注教育', '', text)
    # 移除开头的数字页码（如"30 解题分析："）
    text = re.sub(r'^\d+\s*解题分析[：:]?', '', text)
    # 移除中间的孤立数字（如"22 建设工程"）
    text = re.sub(r'\s+\d{1,2}\s+(?=[\u4e00-\u9fff])', ' ', text)
    # 移除题干末尾的"（ ）"和后面的数字
    text = re.sub(r'[（(]\s*[）)]\s*\d+\s*$', '', text)
    text = re.sub(r'[（(]\s*[）)]\s*$', '', text)
    # 清理多余空格
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# 清理所有题目
for q in questions:
    q['question'] = deep_clean(q['question'])
    q['A'] = deep_clean(q['A'])
    q['B'] = deep_clean(q['B'])
    q['C'] = deep_clean(q['C'])
    q['D'] = deep_clean(q['D'])
    q['analysis'] = deep_clean(q['analysis'])

# 读取原题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    original = json.load(f)

# 分离公共基础和专业基础
public = [q for q in original if q['bigSubject'] == '公共基础']
pro = [q for q in original if q['bigSubject'] == '专业基础']

print(f"原专业基础题数: {len(pro)}")

# 检查是否有重复
existing_keys = set()
for q in pro:
    key = f"{q['year']}-{q.get('yearQnum', '')}"
    existing_keys.add(key)

# 添加新题目
added = 0
for q in questions:
    key = f"{q['year']}-{q['yearQnum']}"
    if key not in existing_keys:
        pro.append(q)
        added += 1
    else:
        print(f"跳过重复: {key}")

print(f"添加了 {added} 道题")
print(f"新专业基础题数: {len(pro)}")

# 按年份和题号排序
pro.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))

# 重新分配id
for i, q in enumerate(pro):
    q['id'] = 1434 + i

# 合并
final = public + pro
print(f"最终题库题数: {len(final)}")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print("题库已更新")

# 统计各年份
from collections import Counter
year_counts = Counter(q['year'] for q in pro)
print("\n各年份题数:")
for year in sorted(year_counts.keys()):
    print(f"  {year}: {year_counts[year]}")
