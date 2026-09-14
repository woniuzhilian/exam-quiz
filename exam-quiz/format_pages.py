import json

with open(r'D:\应用程序开发\刷题\exam-quiz\unmatched_pages.json', 'r', encoding='utf-8') as f:
    results = json.load(f)

# 补充2022补考的页码
bu_pages = {
    '2022补-20': (34, None),
    '2022补-33': (55, None),
    '2022补-42': (70, None),
    '2022补-46': (82, None),
    '2022补-48': (97, None),
    '2022补-69': (159, None),
    '2022补-96': (227, None),
}

for r in results:
    if r['year_qnum'] in bu_pages:
        r['question_page'] = bu_pages[r['year_qnum']][0]

# 按年份排序
def sort_key(r):
    yq = r['year_qnum']
    if '补' in yq:
        year = int(yq.split('补')[0])
        qnum = int(yq.split('-')[1])
        return (year, 1, qnum)  # 补考排后面
    else:
        year = int(yq.split('-')[0])
        qnum = int(yq.split('-')[1])
        return (year, 0, qnum)

results.sort(key=sort_key)

# 输出表格
print("| 题号 | 题目PDF页码 | 答案PDF页码 | 题干摘要 |")
print("|------|------------|------------|----------|")
for r in results:
    q = r['question'].replace('|', '').replace('\n', ' ')[:40]
    print(f"| {r['year_qnum']} | 第{r['question_page']}页 | 第{r['answer_page']}页 | {q} |")

# 保存更新后的结果
with open(r'D:\应用程序开发\刷题\exam-quiz\unmatched_pages.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
