# PyGWalker04.py
import pandas as pd
import pygwalker as pyg
import json
import os

# 建立範例 DataFrame
data = {
    "部門": ["管理部", "人事部", "財務部", "總務部" , "管理部", "人事部", "財務部", "總務部", "總務部", "財務部", "管理部", "人事部", "管理部","總務部" , "人事部" , "財務部"],
    "加班時數": [490, 278, 326, 289, 383, 245, 160, 252, 216, 229, 321, 420 , 212 , 331, 359 , 241],
    "月份": ["2025/01", "2025/02", "2025/03", "2025/04", "2025/05", "2025/06", "2025/01", "2025/02", "2025/03", "2025/05", "2025/05", "2025/06" , "2025/01" , "2025/02" , "2025/03","2025/04"]
}
df = pd.DataFrame(data)

# 先建立計算欄位
df['加班費'] = df['加班時數'] * 150

# 取得程式所在目錄
script_dir = os.path.dirname(os.path.abspath(__file__))
# 設定資料庫檔案名稱
spec_filename = "PyGWalker04.json"
# 建立資料庫檔案的完整路徑
spec_path = os.path.join(script_dir, spec_filename)

# 載入 PyGWalker spec 配置檔案
with open(spec_path, 'r', encoding='utf-8') as f:
    vis_spec = json.load(f)

# 啟動 PyGWalker 互動視覺化，並套用配置
# 套用預設配置檔案 PyGWalker04.json
# 使用核心（kernel）進行計算，而不是在前端瀏覽器中進行計算，減少瀏覽器的負擔。
walker = pyg.walk(df, spec=vis_spec, use_kernel_calc=True)
