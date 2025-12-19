# Seaborn09.py
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

# 熱力圖範例程式
# 只選擇數值型列計算相關係數矩陣
numeric_cols = tips.select_dtypes(include=["float64", "int64"])  # 選擇數值型列
corr = numeric_cols.corr()  # 計算相關係數矩陣

# 配對圖範例程式
sns.pairplot(tips, hue="性別", diag_kind="kde")
plt.suptitle("按性別分類的配對圖", y=1.02)

# 顯示圖表
plt.show()
