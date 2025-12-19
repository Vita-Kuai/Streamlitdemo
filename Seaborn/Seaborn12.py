# Seaborn12.py
# 使用pyplot的好處在於可以自訂圖表大小
import matplotlib.pyplot as plt

import seaborn as sns

# 設定 Seaborn 的主題風格及支援中文顯示
# 主題風格: whitegrid, darkgrid, white, dark, ticks
sns.set(style="whitegrid", font="Microsoft JhengHei")

# 設定調色板為柔和色系
sns.set_palette("pastel")

# 加載內建資料集
tips = sns.load_dataset("tips")

# 控制圖表大小範例程式
plt.figure(figsize=(10, 6))
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("自訂圖表大小範例程式")
plt.xlabel("星期幾")
plt.ylabel("帳單合計")

# 顯示圖表
plt.show()
