import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离公共基础和专业基础
public = [q for q in questions if q['bigSubject'] == '公共基础']
pro = [q for q in questions if q['bigSubject'] == '专业基础']

# 修复空字段题目
fixes = {
    ('2017', 40): {
        'answer': 'C',
        'analysis': '太沙基极限承载力理论假定基底完全粗糙，地基土发生整体剪切破坏时，滑动面由三部分组成：Ⅰ区为基底以下的弹性核（刚性核），Ⅱ区为对数螺旋线过渡区，Ⅲ区为朗肯被动区。临塑荷载和临界荷载的计算没有假定刚性核，普朗德尔-瑞斯纳理论假定基底光滑。答案选C。'
    },
    ('2018', 19): {
        'answer': 'B',
        'analysis': '关键路线是总持续时间最长的线路，关键路线上的工作都是关键工作。关键路线上可以有虚工作，虚工作不消耗时间和资源，但可以表示逻辑关系。总时差为0的工作为关键工作（计划工期等于计算工期时）。因此B选项"关键路线上不能有虚工作"的说法不正确。答案选B。'
    },
    ('2020', 16): {
        'answer': 'B',
        'analysis': '最低投标价法一般适用于具有通用技术、性能标准或者招标人对其技术、性能没有特殊要求的招标项目。综合评估法适用于不宜采用经评审的最低投标价法的招标项目，通常是技术复杂或有特殊要求的项目。因此B选项"综合评估法适合没有特殊要求的招标项目"的说法错误。答案选B。'
    },
}

for (year, qnum), data in fixes.items():
    q = next((x for x in pro if x['year'] == year and x.get('yearQnum') == qnum), None)
    if q:
        print(f'修复 {year}-{qnum}:')
        if 'answer' in data:
            print(f'  answer: "{q.get("answer", "")}" -> "{data["answer"]}"')
            q['answer'] = data['answer']
        if 'analysis' in data:
            print(f'  analysis: 已填写')
            q['analysis'] = data['analysis']
    else:
        print(f'未找到 {year}-{qnum}')

# 对于2024-22题（原2024-26），选项为空，需要提取图片
# 暂时保留，后续处理图片问题

# 重新排序专业基础
pro.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))

# 重新分配id
for i, q in enumerate(public):
    q['id'] = i + 1

pro_start = len(public) + 1
for i, q in enumerate(pro):
    q['id'] = pro_start + i

# 合并
final = public + pro

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print('\n题库已更新')
