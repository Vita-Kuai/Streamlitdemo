# PyGWalker01.py
import pandas as pd
import pygwalker as pyg

# 建立範例 DataFrame
data = {
    "產品": ["A", "B", "C", "D"],
    "銷售量": [100, 150, 80, 200],
    "區域": ["北部", "中部", "南部", "東部"],
}
df = pd.DataFrame(data)

# 啟動 PyGWalker 互動視覺化
# 若在 Jupyter Notebook 中使用，則可直接顯示互動視覺化介面
# 若在其他環境中使用，則會啟動本地伺服器並在瀏覽器中打開
pyg.walk(df)
