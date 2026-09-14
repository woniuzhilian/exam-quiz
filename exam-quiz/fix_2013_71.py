import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2013-71题
for q in questions:
    if q['year'] == '2013' and q.get('yearQnum') == 71:
        q['question'] = r'半径为R的圆管中，横截面上流速分布为$u=2\left(1-\frac{r^2}{R^2}\right)$，其中r表示到圆管轴线的距离，则在$r_1=0.2R$处的粘性切应力与$r_2=R$处的粘性切应力大小之比为：（　　）。'
        print('已修复2013-71')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")
