import json
import re

# 读取提取的题目和答案
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_missing_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

with open(r'D:\应用程序开发\刷题\exam-quiz\pro_missing_answers.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 清理文本函数
def clean_text(text):
    # 移除页眉页脚
    text = re.sub(r'微信公众号[：:]小注基础', '', text)
    text = re.sub(r'基础学习交流QQ\s*群[：:]\s*\d+', '', text)
    text = re.sub(r'小注教育', '', text)
    # 移除纯数字页码
    text = re.sub(r'\n\d+\n', '\n', text)
    # 清理多余空格
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# 确定小科目（这些题目主要是施工管理、法律法规相关）
def get_small_subject(year, qnum):
    # 13-16题通常是施工管理/法律法规
    if qnum in [13, 14, 15, 16]:
        return '施工管理'
    # 其他题目根据内容判断
    if year == '2016' and qnum == 45:
        return '地质作用及地质年代'  # 冰川谷
    if year == '2019' and qnum in [51, 52, 53]:
        return '地基处理'  # 水泥土桩、冻胀、沉降
    if year == '2022' and qnum == 44:
        return '地质作用及地质年代'  # 断层
    return '施工管理'

# 合并题目和答案
merged = []
for year, qs in questions.items():
    for q in qs:
        qnum = q['yearQnum']
        ans = answers.get(year, {}).get(str(qnum), {})
        
        # 清理文本
        question_text = clean_text(q['question'])
        # 移除题干末尾的"（ ）"或"()"
        question_text = re.sub(r'[（(]\s*[）)]\s*$', '', question_text).strip()
        
        merged.append({
            'bigSubject': '专业基础',
            'smallSubject': get_small_subject(year, qnum),
            'year': year,
            'yearQnum': qnum,
            'question': question_text,
            'A': clean_text(q['A']),
            'B': clean_text(q['B']),
            'C': clean_text(q['C']),
            'D': clean_text(q['D']),
            'answer': ans.get('answer', ''),
            'analysis': clean_text(ans.get('analysis', ''))
        })

print(f"合并了 {len(merged)} 道题")

# 按年份和题号排序
merged.sort(key=lambda x: (x['year'], x['yearQnum']))

# 打印前几道题检查
for q in merged[:5]:
    print(f"\n{q['year']}-{q['yearQnum']} ({q['smallSubject']})")
    print(f"  题干: {q['question'][:60]}...")
    print(f"  答案: {q['answer']}")
    print(f"  解析: {q['analysis'][:60]}...")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_missing_merged.json', 'w', encoding='utf-8') as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print("\n已保存到 pro_missing_merged.json")
