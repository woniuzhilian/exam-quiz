import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

# 加载图片映射
with open(r'D:\应用程序开发\刷题\question_images\image_mapping.json', 'r', encoding='utf-8') as f:
    img_mapping = json.load(f)

# 加载JSON
with open(r'D:\应用程序开发\刷题\all_questions_final.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 建立id到题号映射
with open(r'D:\应用程序开发\刷题\questions_raw.txt', 'r', encoding='utf-8') as f:
    raw_text = f.read()
pattern = re.compile(r'【\s*(\d{4}\s*补?)\s*-\s*(\d+)\s*】')
matches = list(pattern.finditer(raw_text))
dup_positions = []
for i, m in enumerate(matches):
    year = m.group(1).replace(' ', '')
    qnum = m.group(2)
    if year == '2016' and qnum == '66':
        dup_positions.append(i+1)
skip_pos = dup_positions[1] if len(dup_positions) > 1 else 819
id_to_qnum = {}
for qid in range(1, 1439):
    if qid < skip_pos:
        match_idx = qid - 1
    else:
        match_idx = qid
    m = matches[match_idx]
    year = m.group(1).replace(' ', '')
    qnum = m.group(2)
    id_to_qnum[qid] = f"{year}-{qnum}"

# 找出未匹配的需配图题目
img_keywords = ['如图', '图所示', '图中', '下图', '上图', '图示', '见图', '图为', '图是']
unmatched = []
for q in data:
    if any(kw in q['question'] for kw in img_keywords):
        qid = str(q['id'])
        if qid not in img_mapping:
            m = re.search(r'PDF第(\d+)页', q['question'])
            page = m.group(1) if m else ''
            qclean = re.sub(r'【本题配图，PDF第\d+页】', '', q['question']).strip()
            unmatched.append({
                'id': q['id'],
                '题号': id_to_qnum.get(q['id'], ''),
                '小科目': q['smallSubject'],
                '年份': q['year'],
                'PDF页码': page,
                '题干摘要': qclean[:50]
            })

print(f"未匹配图片的题目共 {len(unmatched)} 道\n")
# 按小科目统计
from collections import Counter
subject_counts = Counter(u['小科目'] for u in unmatched)
print("按小科目分布:")
for subj, count in subject_counts.most_common():
    print(f"  {subj}: {count}道")

print("\n详细清单:")
print(f"{'id':<6}{'题号':<12}{'年份':<8}{'PDF页':<7}{'小科目':<20}题干摘要")
print("-" * 90)
for u in unmatched:
    print(f"{u['id']:<6}{u['题号']:<12}{u['年份']:<8}{u['PDF页码']:<7}{u['小科目']:<20}{u['题干摘要']}")
