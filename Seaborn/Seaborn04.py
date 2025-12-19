# Seaborn04.py
import matplotlib.pyplot as plt

import seaborn as sns

# 設定 Seaborn 的主題風格及支援中文顯示
# 主題風格: whitegrid, darkgrid, white, dark, ticks
sns.set(style="whitegrid", font="Microsoft JhengHei")

# 設定調色板為柔和色系
sns.set_palette("pastel")

# 加載內建資料集
tips = sns.load_dataset("tips")

# 直方圖範例程式
sns.histplot(tips["total_bill"], bins=20, kde=True)
# bins: 設置直方圖的區間數。
# kde: 是否繪製核密度估計曲線。
plt.title("帳單合計的分佈")
plt.xlabel("帳單合計")
plt.ylabel("頻率")

# 顯示圖表
plt.show()
