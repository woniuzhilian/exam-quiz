import json

# 读取已提取的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

# 新增题目（第57-60页）
new_questions = [
    # 第四章 力法
    {"year": "2016", "yearQnum": 24, "smallSubject": "力法", "question": "图示结构$M_{BA}$的大小为（　　）【本题配图，PDF第57页】", "A": "$\\frac{pl}{2}$", "B": "$\\frac{pl}{3}$", "C": "$\\frac{pl}{4}$", "D": "$\\frac{pl}{5}$"},
    {"year": "2018", "yearQnum": 24, "smallSubject": "力法", "question": "图示两桁架温度均匀降低 t℃，则温度引起的结构内力为（　　）【本题配图，PDF第57页】", "A": "（a）无，（b）有", "B": "（a）有，（b）无", "C": "两者均有", "D": "两者均无"},
    {"year": "2021", "yearQnum": 24, "smallSubject": "力法", "question": "图示结构 B 处弹性支座的弹簧刚度 k=6EI/l³，B 截面转角位移为（　　）【本题配图，PDF第57页】", "A": "$PL^2/12EI$", "B": "$PL^2/6EI$", "C": "$PL^2/4EI$", "D": "$PL^2/3EI$"},
    {"year": "2022补", "yearQnum": 25, "smallSubject": "力法", "question": "图（a）结构，取图（b）为力法基本体系，EI=常数，$\\delta_{11}$为：（　　）【本题配图，PDF第57页】", "A": "2l/3E", "B": "l/2EI", "C": "l/EI", "D": "4l/3EI"},
    {"year": "2023", "yearQnum": 25, "smallSubject": "力法", "question": "取 A 竖向和水平反力为力法方程，未知量 X1（向上）和 X2（向右），主系数为（　　）【本题配图，PDF第58页】", "A": "$\\delta_{11}>0$，$\\delta_{22}<0$", "B": "$\\delta_{11}<0$，$\\delta_{22}>0$", "C": "$\\delta_{11}<0$，$\\delta_{22}<0$", "D": "$\\delta_{11}>0$，$\\delta_{22}>0$"},
    
    # 第五章 位移法、力矩分配法
    {"year": "2019", "yearQnum": 24, "smallSubject": "位移法、力矩分配法", "question": "图示结构EI = 常数，当支座A发生转角θ时，支座B处截面的转角为：（以顺时针为正）（　　）【本题配图，PDF第59页】", "A": "$\\frac{1}{3}\\theta$", "B": "$\\frac{2}{5}\\theta$", "C": "$-\\frac{1}{3}\\theta$", "D": "$-\\frac{2}{5}\\theta$"},
    {"year": "2020", "yearQnum": 24, "smallSubject": "位移法、力矩分配法", "question": "图示结构$M_{BA}$为：（以下侧受拉为正）（　　）【本题配图，PDF第59页】", "A": "$-\\frac{1}{3}M$", "B": "$-\\frac{2}{3}M$", "C": "$\\frac{1}{3}M$", "D": "$\\frac{2}{3}M$"},
    {"year": "2022", "yearQnum": 25, "smallSubject": "位移法、力矩分配法", "question": "位移法典型方程中主系数$\\gamma_{11}$一定（　　）。", "A": "等于零", "B": "大于零", "C": "小于零", "D": "大于等于零"},
    
    # 第六章 结构动力反应分析
    {"year": "2016", "yearQnum": 23, "smallSubject": "结构动力反应分析", "question": "在图示结构中，若要使其自身频率ω增大可以（　　）【本题配图，PDF第60页】", "A": "增大 P", "B": "增大 m", "C": "增大 EI", "D": "增大 l"},
    {"year": "2018", "yearQnum": 23, "smallSubject": "结构动力反应分析", "question": "单自由度体系受简谐荷载作用$m\\ddot{y} + c\\dot{y} + ky = F\\sin\\theta t$，当简谐荷载频率等于结构自振频率，即$\\theta = \\omega = \\sqrt{k/m}$时，与外荷载平衡的力是（　　）。", "A": "惯性力", "B": "阻尼力", "C": "弹性力", "D": "弹性力+惯性力"},
    {"year": "2022", "yearQnum": 26, "smallSubject": "结构动力反应分析", "question": "图示体系在$P(t) = P\\sin\\theta t$作用下，不考虑阻尼，当$\\theta = \\sqrt{0.75EI/(ml^3)}$时，动力系数μ为（　　）【本题配图，PDF第60页】", "A": "0.75", "B": "1.33", "C": "1.50", "D": "1.80"},
    {"year": "2022补", "yearQnum": 26, "smallSubject": "结构动力反应分析", "question": "体系的跨度、约束、质点位置不变，下列哪种情况自振频率最小？（　　）。", "A": "质量小，刚度小", "B": "质量大，刚度大", "C": "质量小，刚度大", "D": "质量大，刚度小"},
    {"year": "2023", "yearQnum": 26, "smallSubject": "结构动力反应分析", "question": "直杆的轴向变形不计，它的动力自由度数是（　　）【本题配图，PDF第60页】。", "A": "2", "B": "3", "C": "4", "D": "1"},
    {"year": "2024", "yearQnum": 26, "smallSubject": "结构动力反应分析", "question": "图示结构中柱的质量不计，阻尼不计。刚性横梁上承受简谐荷载 $Fsin\\theta t$ 的作用，【本题配图，PDF第60页】", "A": "", "B": "", "C": "", "D": ""},
]

# 合并
all_questions = extracted + new_questions

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(all_questions)} 道题")
