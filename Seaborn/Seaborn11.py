# Seaborn11.py
import matplotlib.pyplot as plt

import seaborn as sns

# 設定 Seaborn 的主題風格及支援中文顯示
# 主題風格: whitegrid, darkgrid, white, dark, ticks
sns.set(style="whitegrid", font="Microsoft JhengHei")

# 設定調色板為柔和色系
sns.set_palette("pastel")

# 加載內建資料集  fmri (功能性磁振造影資料)
fmri = sns.load_dataset("fmri")

# 折線圖範例程式
sns.lineplot(x="timepoint", y="signal", hue="event", style="region", data=fmri)
# region 的每個分類值都會被映射到不同的線條樣式（例如虛線、點線、實線或不同 marker）。
plt.title("折線圖範例程式")
plt.xlabel("時間點")
plt.ylabel("信號")

# 顯示圖表
plt.show()
