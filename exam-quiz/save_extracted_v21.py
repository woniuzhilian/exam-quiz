import json

# 读取已提取的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

# 新增题目（第88-89页）
new_questions = [
    # 岩石的基本物理、力学性质及试验方法 续
    {"year": "2024", "yearQnum": 34, "smallSubject": "岩石的基本物理、力学性质及试验方法", "question": "下列关于影响岩石单轴抗压强度的主要因素中，错误的是（　　）。", "A": "结构面", "B": "试件的形状和尺寸", "C": "加载速度", "D": "承压板端部的摩擦力及其刚度"},
    
    # 第二章 岩体工程分类
    {"year": "2019", "yearQnum": 40, "smallSubject": "岩体工程分类", "question": "某层状结构的岩体，结构面结合良好，实测岩石单轴饱和抗压强度$R_C = 80MP$单位岩体体积的节理数小$Jv = 6$条$/m^3$，按国标工程岩体分级标准（GB50218 - 94）确定该岩体的基本质量等级为（　　）。", "A": "I 级", "B": "II级", "C": "III级", "D": "IV 级"},
    {"year": "2020", "yearQnum": 40, "smallSubject": "岩体工程分类", "question": "我国现行工程岩体分级标准中岩石的坚硬程度确定是按照（　　）。", "A": "岩石的软化系数", "B": "岩石的弹性模量", "C": "岩石的单轴饱和抗拉强度", "D": "岩石的单轴饱和抗压强度"},
    {"year": "2021", "yearQnum": 40, "smallSubject": "岩体工程分类", "question": "测得岩体的纵波波速为 4000m/s，岩块的纵波波速为 5000m/s，问岩体的完整性属于（　　）。", "A": "完整", "B": "较完整", "C": "完整性差", "D": "较破碎"},
    {"year": "2022补", "yearQnum": 35, "smallSubject": "岩体工程分类", "question": "我国工程岩体分级标准中是根据哪些因素对岩石基本质量进行修正？（　　）。①地应力大小 ②地下水 ③结构面方位 ④结构面粗糙度", "A": "①④", "B": "①②", "C": "③", "D": "①②③"},
    {"year": "2023", "yearQnum": 34, "smallSubject": "岩体工程分类", "question": "工程岩体分类的目的是：（　　）。", "A": "用简单易测的指标把地质条件和岩体力学性质参数联系起来，反映岩体质量好坏，为设计和施工提供参数和依据", "B": "找出影响岩体工程稳定性的主要控制因素，为设计和施工提供参数和依据", "C": "进行岩体工程的定量化研究，建立岩体力学严格的理论体系，指导工程实践", "D": "建立适用于各类工程的通用岩体质量评价体系，为设计和施工提供参数和依据"},
    {"year": "2024", "yearQnum": 35, "smallSubject": "岩体工程分类", "question": "工程岩体分类是对岩体进行归类的一种工作方法，其目的不包括（　　）。", "A": "分析评价工程岩体稳定性的需要", "B": "为岩石工程建设的勘察，设计施工和编制定额和概预算提供必要的基本依据", "C": "便于设计施工方法的总结、交流、推广", "D": "以单一指标为分级依据，取代反映复杂岩体各种属性的多因素、综合特性值分类法"},
]

# 合并
all_questions = extracted + new_questions

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(all_questions)} 道题")
