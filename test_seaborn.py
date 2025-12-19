import matplotlib.pyplot as plt

import seaborn as sns


# 設定 Seaborn 的主題風格及支援中文顯示
# 主題風格: whitegrid, darkgrid, white, dark, ticks
sns.set_theme(style="whitegrid", font="Microsoft JhengHei")

# 設定調色板為柔和色系
sns.set_palette("pastel")

# 加載內建資料集
penguins  = sns.load_dataset("penguins")
sns.scatterplot(x='bill_length_mm', y ='flipper_length_mm',data=penguins, hue='species', style='island')
plt.title("企鵝")
plt.xlabel("物種")
plt.ylabel("翅膀長度")

# 顯示圖表
plt.show()