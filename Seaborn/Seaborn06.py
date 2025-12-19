# Seaborn06.py
import matplotlib.pyplot as plt

import seaborn as sns

# 設定 Seaborn 的主題風格及支援中文顯示
# 主題風格: whitegrid, darkgrid, white, dark, ticks
sns.set(style="whitegrid", font="Microsoft JhengHei")

# 設定調色板為柔和色系
sns.set_palette("pastel")

# 加載內建資料集
tips = sns.load_dataset("tips")

# 箱型圖範例程式,進階：增加分組顏色
sns.boxplot(x="day", y="total_bill", hue="sex", data=tips)
plt.title("按星期幾及性別分類的帳單合計箱型圖")
plt.xlabel("星期幾")
plt.ylabel("帳單合計")

# 顯示圖表
plt.show()
