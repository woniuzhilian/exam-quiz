import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离公共基础和专业基础
public = [q for q in questions if q['bigSubject'] == '公共基础']
pro = [q for q in questions if q['bigSubject'] == '专业基础']

# 缺失的题目
missing_questions = [
    {
        'bigSubject': '公共基础',
        'smallSubject': '法律法规',
        'year': '2017',
        'yearQnum': 119,
        'question': '根据《建设工程质量管理条例》规定，下列有关建设工程质量保修的说法中，正确的是（　　）。',
        'A': '建设工程的保修期，自工程移交之日起计算',
        'B': '供冷系统在正常使用条件下，最低保修期限为2年',
        'C': '供热系统在正常使用条件下，最低保修期限为2年采暖期',
        'D': '建设工程承包单位向建设单位提交竣工结算资料时，应当出具质量保修书',
        'answer': 'C',
        'analysis': '基础设施工程、房屋建筑的地基基础工程和主体结构工程，为设计文件规定的该工程的合理使用年限。屋面防水工程、有防水要求的卫生间、房间和外墙面的防渗漏，为5年。供热与供冷系统，为两个采暖期、供冷期。电气管线、给排水管道、设备安装和装修工程，为2年。答案选C。'
    },
    {
        'bigSubject': '公共基础',
        'smallSubject': '法律法规',
        'year': '2017',
        'yearQnum': 120,
        'question': '根据《建设工程安全生产管理条例》规定，建设单位确定建设工程安全作业环境及安全施工措施所需费用的时间是（　　）。',
        'A': '编制工程概算时',
        'B': '编制设计预算时',
        'C': '编制施工预算时',
        'D': '编制投资估算时',
        'answer': 'A',
        'analysis': '建设单位在编制工程概算时，应当确定建设工程安全作业环境及安全施工措施所需费用。答案选A。'
    },
    {
        'bigSubject': '公共基础',
        'smallSubject': '法律法规',
        'year': '2018',
        'yearQnum': 119,
        'question': '某城市计划对本地城市建设进行全面规划，根据《环境保护法》的规定，下列城乡建设行为不符合《环境保护法》规定的是（　　）。',
        'A': '加强在自然景观中修建人文景观',
        'B': '有效保护植被、水域',
        'C': '加强城市园林、绿地园林',
        'D': '加强风景名胜区的建设',
        'answer': 'A',
        'analysis': '城乡建设应当结合当地自然环境的特点，保护植被、水域和自然景观，加强城市园林、绿地和风景名胜区的建设。答案选A。'
    },
    {
        'bigSubject': '公共基础',
        'smallSubject': '法律法规',
        'year': '2018',
        'yearQnum': 120,
        'question': '根据《建设工程安全生产管理条例》规定，施工单位主要负责人应当承担的责任是（　　）。',
        'A': '落实安全生产责任制度、安全生产规章制度和操作规程',
        'B': '保证本单位安全生产条件所需资金的投入',
        'C': '确保安全生产费用的有效使用',
        'D': '根据工程的特点组织特定安全施工措施',
        'answer': 'B',
        'analysis': '施工单位主要负责人依法对本单位的安全生产工作全面负责。施工单位应当建立健全安全生产责任制度和安全生产教育培训制度，制定安全生产规章制度和操作规程，保证本单位安全生产条件所需资金的投入，对所承担的建设工程进行定期和专项安全检查，并做好安全检查记录。答案选B。'
    },
    {
        'bigSubject': '公共基础',
        'smallSubject': '法律法规',
        'year': '2021',
        'yearQnum': 120,
        'question': '某工程施工单位完成了楼板钢筋绑扎工序，在浇筑混凝土前需要进行隐蔽质量验收，根据《建设工程质量管理条例》规定，施工单位在隐蔽前应当通知的单位是（　　）。',
        'A': '建设单位和监理单位',
        'B': '建设单位和建设工程质量监督机构',
        'C': '监理单位和设计单位',
        'D': '设计单位和建设工程质量监督机构',
        'answer': 'B',
        'analysis': '施工单位必须建立、健全施工质量的检验制度，严格工序管理，作好隐蔽工程的质量检查和记录。隐蔽工程在隐蔽前，施工单位应当通知建设单位和建设工程质量监督机构。答案选B。'
    },
    {
        'bigSubject': '公共基础',
        'smallSubject': '法律法规',
        'year': '2023',
        'yearQnum': 120,
        'question': '某建设工程项目需要拆除，建设单位应当向工程所在地的县级以上地方人民政府建设行政主管部门或者其他有关部门办理有关资料的备案，其需要报送的资料不包括（　　）。',
        'A': '施工单位资质等级证明',
        'B': '拆除施工组织方案',
        'C': '堆放、清除废弃物的措施',
        'D': '需要拆除的理由',
        'answer': 'D',
        'analysis': '根据《建设工程安全生产管理条例》第十一条规定，建设单位应当将拆除工程发包给具有相应资质等级的施工单位。建设单位应当在拆除工程施工15日前，将下列资料报送建设工程所在地的县级以上地方人民政府建设行政主管部门或者其他有关部门备案：①施工单位资质等级证明；②拟拆除建筑物、构筑物及可能危及毗邻建筑的说明；③拆除施工组织方案；④堆放、清除废弃物的措施。答案选D。'
    }
]

# 添加缺失的题目
public.extend(missing_questions)

# 重新排序公共基础
public.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))

# 重新分配id
for i, q in enumerate(public):
    q['id'] = i + 1

# 专业基础id从公共基础数量+1开始
pro_start = len(public) + 1
for i, q in enumerate(pro):
    q['id'] = pro_start + i

# 合并
final = public + pro

# 验证
print(f"公共基础题数: {len(public)}")
print(f"专业基础题数: {len(pro)}")
print(f"总题数: {len(final)}")

# 检查各年份题数
years = {}
for q in public:
    year = q['year']
    years[year] = years.get(year, 0) + 1

print("\n各年份题数:")
for year in sorted(years.keys()):
    print(f"  {year}: {years[year]}题")

# 检查缺失题目是否已添加
for q in missing_questions:
    found = any(x['year'] == q['year'] and x.get('yearQnum') == q['yearQnum'] for x in public)
    print(f"  {q['year']}-{q['yearQnum']}: {'已添加' if found else '未添加'}")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print("\n题库已更新")
