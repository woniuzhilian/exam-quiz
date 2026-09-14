import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

pro = [q for q in questions if q['bigSubject'] == '专业基础']
public = [q for q in questions if q['bigSubject'] == '公共基础']

print("=" * 60)
print("专业基础题库全面复查")
print("=" * 60)

# 1. 检查题数
print(f"\n1. 题数统计:")
print(f"   公共基础: {len(public)} 题")
print(f"   专业基础: {len(pro)} 题")
print(f"   总计: {len(questions)} 题")

# 2. 检查各年份题数
print(f"\n2. 专业基础各年份题数:")
years = sorted(set(q['year'] for q in pro))
for year in years:
    year_questions = [q for q in pro if q['year'] == year]
    qnums = sorted([q.get('yearQnum', 0) for q in year_questions])
    missing = [n for n in range(1, 61) if n not in qnums]
    print(f"   {year}: {len(year_questions)} 题, 题号范围 {min(qnums)}-{max(qnums)}, 缺失: {missing if missing else '无'}")

# 3. 检查空字段
print(f"\n3. 空字段检查:")
empty_fields = []
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'answer', 'analysis']:
        if not q.get(field):
            empty_fields.append((q['year'], q.get('yearQnum'), field))
if empty_fields:
    print(f"   发现 {len(empty_fields)} 个空字段:")
    for year, qnum, field in empty_fields:
        print(f"     {year}-{qnum}: {field}")
else:
    print("   无空字段")

# 4. 检查answer字段
print(f"\n4. answer字段检查:")
invalid_answers = []
for q in pro:
    answer = q.get('answer', '')
    if answer not in ['A', 'B', 'C', 'D']:
        invalid_answers.append((q['year'], q.get('yearQnum'), answer))
if invalid_answers:
    print(f"   发现 {len(invalid_answers)} 个无效answer:")
    for year, qnum, answer in invalid_answers:
        print(f"     {year}-{qnum}: {answer}")
else:
    print("   所有answer字段均为A/B/C/D")

# 5. 检查配图标记
print(f"\n5. 配图标记检查:")
image_markers = []
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text and ('本题配有示意图' in text or '本题配图' in text):
            image_markers.append((q['year'], q.get('yearQnum'), field))
            break
if image_markers:
    print(f"   发现 {len(image_markers)} 个配图标记:")
    for year, qnum, field in image_markers:
        print(f"     {year}-{qnum}: {field}")
else:
    print("   无未处理的配图标记")

# 6. 检查img标签
print(f"\n6. img标签检查:")
img_count = 0
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text and '<img' in text:
            img_count += 1
print(f"   共 {img_count} 个字段包含img标签")

# 7. 检查LaTeX公式
print(f"\n7. LaTeX公式检查:")
latex_count = 0
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text and '$' in text:
            latex_count += 1
print(f"   共 {latex_count} 个字段包含LaTeX公式")

# 8. 检查特殊符号
print(f"\n8. 特殊符号检查:")
special_chars = ['α', 'β', 'γ', 'δ', 'π', 'Δ', 'Σ', '≤', '≥', '±', '×', '÷', '≠', '≈', '∞', '∫', '∂', '∇', '√', '∠', '⊥', '∥', '∵', '∴']
special_count = 0
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text:
            for char in special_chars:
                if char in text:
                    special_count += 1
                    break
print(f"   共 {special_count} 个字段包含特殊符号（可能需要转LaTeX）")

# 9. 检查HTML表格
print(f"\n9. HTML表格检查:")
table_count = 0
for q in pro:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text and '<table' in text:
            table_count += 1
print(f"   共 {table_count} 个字段包含HTML表格")

print("\n" + "=" * 60)
print("复查完成")
print("=" * 60)
