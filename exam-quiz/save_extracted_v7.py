import json

# 读取已提取的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

# 新增题目（第48-52页）
new_questions = [
    # 地基处理 续
    {"year": "2023", "yearQnum": 60, "smallSubject": "地基处理", "question": "土面为 1m 素填土，容重 16.5kN/m³，下面软土层厚 7.5m，容重 18.6kN/m³，软土$f_{ak}$=70kpa；地下水位 1.0m，基础顶面荷载 180kN/m，基础宽 1.2m，埋深 1.0m，用砂垫层进行地基处理，厚度 2.0m，扩散角为 30 度，求砂垫层的最小宽度（　　）。", "A": "2.5m", "B": "3.0m", "C": "3.5m", "D": "4.5m"},
    {"year": "2024", "yearQnum": 60, "smallSubject": "地基处理", "question": "竖向承载旋喷桩复合地基宜在基础和桩顶之间设置褥垫层，下列哪种材料不宜适用（　　）。", "A": "块石", "B": "中砂", "C": "粗砂", "D": "级配砂石"},
    
    # 第五部分 结构力学 - 第一章 平面几何体系组成
    {"year": "2020", "yearQnum": 22, "smallSubject": "平面几何体系组成", "question": "几何可变体系的计算自由度（　　）。", "A": ">0", "B": "<0", "C": "=0", "D": "不确定"},
    {"year": "2022", "yearQnum": 22, "smallSubject": "平面几何体系组成", "question": "图示平面的几何组成性质是（　　）【本题配图，PDF第49页】", "A": "几何不变无多余约束", "B": "几何不变有多余约束", "C": "几何可变", "D": "瞬变"},
    {"year": "2022补", "yearQnum": 22, "smallSubject": "平面几何体系组成", "question": "图示体系为：（　　）【本题配图，PDF第49页】", "A": "几何不变无多余约束", "B": "几何不变有多余约束", "C": "几何可变", "D": "几何瞬变"},
    {"year": "2023", "yearQnum": 22, "smallSubject": "平面几何体系组成", "question": "该体系的计算自由度：（　　）【本题配图，PDF第49页】", "A": "0", "B": "1", "C": "-1", "D": "2"},
    {"year": "2023", "yearQnum": 23, "smallSubject": "平面几何体系组成", "question": "静定结构支座移动的时候会产生（　　）。", "A": "内力", "B": "应力", "C": "刚体位移", "D": "变形"},
    {"year": "2024", "yearQnum": 22, "smallSubject": "平面几何体系组成", "question": "图示体系的几个组合性质为（　　）【本题配图，PDF第49页】", "A": "几何可变体系", "B": "无多余约束的结几何不变体系", "C": "有 1 个多余约束的结束何不变体系", "D": "有 2 个多余约束的结几何不变体系"},
    {"year": "2024", "yearQnum": 25, "smallSubject": "平面几何体系组成", "question": "图示结构的超静定次数为（　　）【本题配图，PDF第50页】", "A": "3", "B": "4", "C": "5", "D": "6"},
    
    # 第二章 结构受力分析
    {"year": "2017", "yearQnum": 22, "smallSubject": "结构受力分析", "question": "图示对称结构$M_{AD} = ql^2/36$（左拉），$F_{NAD} = -5ql/12$（压），则$M_{BC}$为（以下侧受拉为正）（　　）【本题配图，PDF第51页】", "A": "$-ql^2/6$", "B": "$ql^2/6$", "C": "$-ql^2/9$", "D": "$ql^2/9$"},
    {"year": "2017", "yearQnum": 23, "smallSubject": "结构受力分析", "question": "图示结构EI = 常数，在给定荷载作用下，水平反力$H_A$为（　　）【本题配图，PDF第51页】", "A": "P", "B": "2P", "C": "3P", "D": "4P"},
    {"year": "2019", "yearQnum": 22, "smallSubject": "结构受力分析", "question": "图示结构BC杆轴力为（　　）【本题配图，PDF第51页】", "A": "$-2F_P$", "B": "$-2\\sqrt{2}F_P$", "C": "$-\\sqrt{2}F_P$", "D": "$-4F_P$"},
    {"year": "2019", "yearQnum": 23, "smallSubject": "结构受力分析", "question": "图示三铰拱，若高跨比f/L = 1/2，则水平推力$F_H$为（　　）【本题配图，PDF第52页】", "A": "$\\frac{1}{4}F_P$", "B": "$\\frac{1}{2}F_P$", "C": "$\\frac{3}{4}F_P$", "D": "$\\frac{3}{8}F_P$"},
    {"year": "2020", "yearQnum": 23, "smallSubject": "结构受力分析", "question": "图示刚架$M_{DC}$为（下侧受拉为正）（　　）【本题配图，PDF第52页】", "A": "20kN·m", "B": "40kN·m", "C": "60kN·m", "D": "80kN·m"},
    {"year": "2021", "yearQnum": 22, "smallSubject": "结构受力分析", "question": "如图示结构，$M_{DC}$大小为（　　）【本题配图，PDF第52页】", "A": "20kN·m", "B": "40kN·m", "C": "60kN·m", "D": "80kN·m"},
]

# 合并
all_questions = extracted + new_questions

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(all_questions)} 道题")
