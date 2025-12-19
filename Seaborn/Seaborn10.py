# Seaborn10.py
# 顯示男性與女性在午餐和晚餐兩個時段時所付的小費分布圖
import matplotlib.pyplot as plt

import seaborn as sns

# 設定 Seaborn 的主題風格及支援中文顯示
# 主題風格: whitegrid, darkgrid, white, dark, ticks
sns.set(style="whitegrid", font="Microsoft JhengHei")

# 設定調色板為柔和色系
sns.set_palette("pastel")

# 加載內建資料集
tips = sns.load_dataset("tips")
# 將英文欄位名稱改為中文
tips = tips.rename(columns={
    'total_bill': '帳單總額',
    'tip': '小費',
    'sex': '性別',
    'smoker': '是否吸煙',
    'day': '星期幾',
    'time': '用餐時間',
    'size': '用餐人數'
})
# 分面圖範例程式
g = sns.FacetGrid(tips, col="sex", row="time", margin_titles=True)
g.map(sns.scatterplot, "total_bill", "tip")
plt.suptitle("按性別和用餐時間分類的分面圖", y=1.02)

# 顯示圖表
plt.show()
