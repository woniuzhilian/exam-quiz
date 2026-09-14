import json

# 读取已提取的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

# 新增题目（第53-56页）
new_questions = [
    # 结构受力分析 续
    {"year": "2021", "yearQnum": 23, "smallSubject": "结构受力分析", "question": "图示桁架 a 杆轴力为（　　）【本题配图，PDF第53页】", "A": "-15KN", "B": "-20KN", "C": "-25KN", "D": "-30KN"},
    {"year": "2022", "yearQnum": 23, "smallSubject": "结构受力分析", "question": "图示桁架 C 杆的内力是（　　）【本题配图，PDF第53页】", "A": "P", "B": "-P/2", "C": "P/2", "D": "0"},
    {"year": "2022补", "yearQnum": 23, "smallSubject": "结构受力分析", "question": "图示结构 B 点杆端弯矩（设内侧受拉为正）为：（　　）【本题配图，PDF第53页】", "A": "$M_{BA} = Pa$，$M_{BC} = -Pa$", "B": "$M_{BA} = M_{BC} = 2Pa$", "C": "$M_{BA} = M_{BC} = Pa$", "D": "$M_{BA} = M_{BC} = 0$"},
    {"year": "2023", "yearQnum": 24, "smallSubject": "结构受力分析", "question": "求截面 K 的剪力（　　）【本题配图，PDF第54页】", "A": "-1kN", "B": "1kN", "C": "-0.5kN", "D": "0.5kN"},
    {"year": "2024", "yearQnum": 23, "smallSubject": "结构受力分析", "question": "图示简支钢梁斜梁跨中截面 E 的剪力为（　　）【本题配图，PDF第54页】", "A": "-10kN", "B": "-15kN", "C": "-20kN", "D": "-25kN"},
    {"year": "2024", "yearQnum": 27, "smallSubject": "结构受力分析", "question": "图示多跨梁的弯矩图大致形状正确的是（　　）【本题配图，PDF第54页】", "A": "选项A", "B": "选项B", "C": "选项C", "D": "选项D"},
    
    # 第三章 位移计算
    {"year": "2016", "yearQnum": 22, "smallSubject": "位移计算", "question": "图示对称结构 C 点的水平位移$\\Delta$ CH =$\\Delta$（右），若 AC 杆 EI 增大一倍，BC 杆 EI 不变，则$\\Delta$ CH变为（　　）【本题配图，PDF第55页】", "A": "2 $\\Delta$", "B": "1.5 $\\Delta$", "C": "0.5 $\\Delta$", "D": "0.75 $\\Delta$"},
    {"year": "2017", "yearQnum": 24, "smallSubject": "位移计算", "question": "图示梁的抗弯刚度为EI，长度为l，欲使梁中点 C 弯矩为零，则弹性支座刚度k的取值应为（　　）【本题配图，PDF第55页】", "A": "$3EI/l^3$", "B": "$6EI/l^3$", "C": "$9EI/l^3$", "D": "$12EI/l^3$"},
    {"year": "2018", "yearQnum": 22, "smallSubject": "位移计算", "question": "图内结构中的反力$F_H$（　　）【本题配图，PDF第55页】", "A": "M / L", "B": "−M / L", "C": "2M / L", "D": "−2M / L"},
    {"year": "2022", "yearQnum": 24, "smallSubject": "位移计算", "question": "图示结构，求 A、B 两点相对线位移时，虚力状态应在两点分别施加的单位力为（　　）【本题配图，PDF第55页】", "A": "竖向反向力", "B": "水平反向力", "C": "连线方向反向力", "D": "反向力偶"},
    {"year": "2022补", "yearQnum": 24, "smallSubject": "位移计算", "question": "图示结构 A 截面转角（设顺时针为正）为：（　　）【本题配图，PDF第56页】", "A": "$2Pa^2/EI$", "B": "$-Pa^2/EI$", "C": "$5Pa^2/(4EI)$", "D": "$-5Pa^2/(4EI)$"},
    {"year": "2024", "yearQnum": 24, "smallSubject": "位移计算", "question": "图示三铰拱右支座发生水平支座位移$\\Delta$，则拱顶 C 竖向位移的值（　　）【本题配图，PDF第56页】", "A": "$\\frac{L}{8f}\\Delta$", "B": "$\\frac{L}{4f}\\Delta$", "C": "$\\frac{L}{2f}\\Delta$", "D": "$\\frac{L}{f}\\Delta$"},
]

# 合并
all_questions = extracted + new_questions

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(all_questions)} 道题")
