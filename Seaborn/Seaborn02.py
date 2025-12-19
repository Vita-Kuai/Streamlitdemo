# Seaborn02.py
import matplotlib.pyplot as plt

import seaborn as sns

# 設定 Seaborn 的主題風格及支援中文顯示
# 主題風格: whitegrid, darkgrid, white, dark, ticks
sns.set_theme(style="whitegrid", font="Microsoft JhengHei")

# 設定調色板為柔和色系
sns.set_palette("pastel")

# 加載內建資料集
tips = sns.load_dataset("tips")

# 繪製散點圖
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("帳單合計 vs 小費")
plt.xlabel("帳單合計")
plt.ylabel("小費")

# 顯示圖表
plt.show()
