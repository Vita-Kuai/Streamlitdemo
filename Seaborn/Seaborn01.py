#Seaborn01.py
# 匯入必要的套件
import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns

# 建立範例 DataFrame
data = {
    "產品": ["A", "B", "C", "D"],
    "銷售量": [100, 150, 80, 200],
    "區域": ["北部", "中部", "南部", "東部"],
}
df = pd.DataFrame(data)
print(df)
"""
  產品  銷售量  區域
0  A  100  北部
1  B  150  中部
2  C   80  南部
3  D  200  東部
"""

# 設定 Seaborn 的主題風格及支援中文顯示
# 主題風格: whitegrid, darkgrid, white, dark, ticks
sns.set_theme(style="whitegrid", font="Microsoft JhengHei")

# 建立長條圖
plt.figure(figsize=(8, 5))

# 依照銷售量排序產品名稱
order = df.sort_values("銷售量", ascending=False)["產品"]

# hue="產品" → 讓圖表依照「產品」區分顏色。
# palette="Set2" → 選擇柔和配色。
sns.barplot(data=df, x="產品", y="銷售量", hue="產品", order=order, palette="Set2")

# X 軸文字旋轉 , 0=不旋轉
plt.xticks(rotation=0)

# 顯示數值標籤
for container in plt.gca().containers:
    plt.bar_label(container, fmt="%.0f", label_type="edge", fontsize=10, padding=3)

# 標題與標籤
plt.title("各產品銷售量比較", fontsize=16)
plt.xlabel("產品名稱", fontsize=12)
plt.ylabel("銷售量", fontsize=12)

# 避免文字重疊。
plt.tight_layout()

# 顯示圖表
plt.show()
