# Seaborn13.py
import matplotlib.pyplot as plt

import seaborn as sns

# 設定 Seaborn 的主題風格及支援中文顯示
# 主題風格: whitegrid, darkgrid, white, dark, ticks
sns.set(style="whitegrid", font="Microsoft JhengHei")

# 使用內建 muted 調色板
sns.set_palette("muted")

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
