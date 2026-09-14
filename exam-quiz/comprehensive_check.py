import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print("=" * 80)
print("全面题库质量检查")
print("=" * 80)

# 1. 检查乱码字符
print("\n1. 乱码字符检查:")
garbage_chars = ['�', '□', '■', '●', '○', '◇', '◆', '★', '☆', '※', '→', '←', '↑', '↓', '⇒', '⇐', '⇑', '⇓']
garbage_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text:
            for char in garbage_chars:
                if char in text:
                    print(f"  {q['year']}-{q.get('yearQnum', q['id'])} ({field}): 包含字符 '{char}'")
                    garbage_count += 1
                    break
print(f"  共发现 {garbage_count} 个乱码问题")

# 2. 检查未转换的特殊符号（应该用LaTeX但用了Unicode）
print("\n2. 未转换特殊符号检查:")
special_unicode = ['²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹', '⁰', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉', '₀',
                   '√', '∛', '∜', '∞', '∑', '∏', '∫', '∮', '∂', '∇', 'Δ', 'δ', 'ε', 'ζ', 'η', 'θ', 'λ', 'μ', 'ν',
                   'ξ', 'π', 'ρ', 'σ', 'τ', 'φ', 'χ', 'ψ', 'ω', 'Γ', 'Θ', 'Λ', 'Ξ', 'Π', 'Σ', 'Φ', 'Ψ', 'Ω',
                   '≤', '≥', '≠', '≈', '≡', '±', '×', '÷', '∠', '⊥', '∥', '∵', '∴']
special_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text:
            found = [char for char in special_unicode if char in text]
            if found:
                # 排除已经在$...$中的LaTeX
                # 简单检查：如果文本中有$，可能已经是LaTeX
                if '$' not in text:
                    print(f"  {q['year']}-{q.get('yearQnum', q['id'])} ({field}): {found}")
                    special_count += 1
print(f"  共发现 {special_count} 个未转换特殊符号")

# 3. 检查上标下标问题（如m2, m3, cm2等应该是m^2）
print("\n3. 上标下标格式检查:")
superscript_patterns = [
    (r'm(\d)(?!\d)', 'm^{\\1}'),  # m2, m3
    (r'cm(\d)(?!\d)', 'cm^{\\1}'),  # cm2, cm3
    (r'mm(\d)(?!\d)', 'mm^{\\1}'),  # mm2, mm3
    (r'kN/m(\d)(?!\d)', 'kN/m^{\\1}'),  # kN/m2, kN/m3
    (r'N/mm(\d)(?!\d)', 'N/mm^{\\1}'),  # N/mm2
]
superscript_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text and '$' not in text:
            for pattern, replacement in superscript_patterns:
                matches = re.findall(pattern, text)
                if matches:
                    print(f"  {q['year']}-{q.get('yearQnum', q['id'])} ({field}): {matches}")
                    superscript_count += 1
                    break
print(f"  共发现 {superscript_count} 个上标格式问题")

# 4. 检查配图位置问题（img标签在文字中间）
print("\n4. 配图位置检查:")
img_position_count = 0
for q in questions:
    text = q.get('question', '')
    if text and '<img' in text:
        # 检查img标签是否在文字中间（前后都有非空白字符）
        parts = text.split('<img')
        if len(parts) > 1:
            before = parts[0].strip()
            after = parts[1].split('>')[-1].strip() if '>' in parts[1] else ''
            if before and after and len(before) > 10:
                print(f"  {q['year']}-{q.get('yearQnum', q['id'])}: 配图可能在文字中间")
                print(f"    前文: {before[:50]}...")
                img_position_count += 1
print(f"  共发现 {img_position_count} 个配图位置问题")

# 5. 检查题号连续性
print("\n5. 题号连续性检查:")
for big_subject in ['公共基础', '专业基础']:
    subject_questions = [q for q in questions if q['bigSubject'] == big_subject]
    years = sorted(set(q['year'] for q in subject_questions))
    for year in years:
        year_questions = [q for q in subject_questions if q['year'] == year]
        qnums = sorted([q.get('yearQnum', 0) for q in year_questions])
        expected_max = 120 if big_subject == '公共基础' else 60
        missing = [n for n in range(1, expected_max + 1) if n not in qnums]
        if missing:
            print(f"  {big_subject} {year}: 缺失题号 {missing}")

# 6. 检查空字段
print("\n6. 空字段检查:")
empty_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'answer', 'analysis']:
        if not q.get(field):
            # 排除选项配图合并的情况
            if field in ['B', 'C', 'D'] and q.get('A') and '<img' in q.get('A', ''):
                continue
            print(f"  {q['year']}-{q.get('yearQnum', q['id'])} ({q['bigSubject']}): {field} 为空")
            empty_count += 1
print(f"  共发现 {empty_count} 个空字段")

# 7. 检查上划线问题（如AB上划线）
print("\n7. 上划线检查:")
overline_patterns = [r'[A-Z]̅', r'[A-Z]̄', r'[A-Z]‾']
overline_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text:
            for pattern in overline_patterns:
                if re.search(pattern, text):
                    print(f"  {q['year']}-{q.get('yearQnum', q['id'])} ({field}): 包含上划线字符")
                    overline_count += 1
                    break
print(f"  共发现 {overline_count} 个上划线问题")

# 8. 检查公式格式问题（$...$不配对）
print("\n8. 公式格式检查:")
formula_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text:
            dollar_count = text.count('$')
            if dollar_count % 2 != 0:
                print(f"  {q['year']}-{q.get('yearQnum', q['id'])} ({field}): $符号不配对 ({dollar_count}个)")
                formula_count += 1
print(f"  共发现 {formula_count} 个公式格式问题")

print("\n" + "=" * 80)
print("检查完成")
print("=" * 80)
