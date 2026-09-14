import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2017-19题
for q in questions:
    if q['year'] == '2017' and q.get('yearQnum') == 19:
        q['question'] = r'矩阵$A=\begin{bmatrix}0 & 0 & -2 \\ 0 & 3 & 0 \\ 1 & 0 & 0\end{bmatrix}$的逆矩阵$A^{-1}=$：（　　）。'
        q['A'] = r'$\begin{bmatrix}-\frac{1}{2} & 0 & 0 \\ 0 & \frac{1}{3} & 0 \\ 0 & 0 & 1\end{bmatrix}$'
        q['B'] = r'$\begin{bmatrix}0 & 0 & -\frac{1}{2} \\ 0 & \frac{1}{3} & 0 \\ 1 & 0 & 0\end{bmatrix}$'
        q['C'] = r'$\begin{bmatrix}0 & 0 & 1 \\ 0 & \frac{1}{3} & 0 \\ -\frac{1}{2} & 0 & 0\end{bmatrix}$'
        q['D'] = r'$\begin{bmatrix}0 & 0 & 6 \\ 0 & 2 & 0 \\ 3 & 0 & 0\end{bmatrix}$'
        print('已修复2017-19')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")
