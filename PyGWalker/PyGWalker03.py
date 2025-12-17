# PyGWalker03.py
import pandas as pd
import pygwalker as pyg

# 建立範例 DataFrame
data = {
    "部門": ["管理部", "人事部", "財務部", "總務部" , "管理部", "人事部", "財務部", "總務部", "總務部", "財務部", "管理部", "人事部", "管理部","總務部" , "人事部" , "財務部"],
    "加班時數": [490, 278, 326, 289, 383, 245, 160, 252, 216, 229, 321, 420 , 212 , 331, 359 , 241],
    "月份": ["2025/01", "2025/02", "2025/03", "2025/04", "2025/05", "2025/06", "2025/01", "2025/02", "2025/03", "2025/05", "2025/05", "2025/06" , "2025/01" , "2025/02" , "2025/03","2025/04"]
}
df = pd.DataFrame(data)

# 先建立計算欄位
df['加班費'] = df['加班時數'] * 150

# 定義 PyGWalker 視覺化配置
vis_spec = {
    "config": [{
        "config": {
            "defaultAggregated": True,
            "geoms": ["table"],
            "coordSystem": "generic",
            "limit": -1 # 沒有限制筆數
        },
        "encodings": {
            "dimensions": [ # 維度
                {"fid": "月份", "name": "月份", "basename": "月份", "semanticType": "nominal", "analyticType": "dimension", "offset": 0},
                {"fid": "部門", "name": "部門", "basename": "部門", "semanticType": "nominal", "analyticType": "dimension", "offset": 0}
            ],
            "measures": [
                {"fid": "加班時數", "name": "加班時數", "basename": "加班時數", "analyticType": "measure", "semanticType": "quantitative", "aggName": "sum", "offset": 0},
                {"fid": "加班費", "name": "加班費", "basename": "加班費", "analyticType": "measure", "semanticType": "quantitative", "aggName": "sum", "offset": 0}
            ],
            "rows": [
                {"fid": "月份", "name": "月份", "basename": "月份", "semanticType": "nominal", "analyticType": "dimension", "offset": 0}
            ],
            "columns": [
                {"fid": "部門", "name": "部門", "basename": "部門", "semanticType": "nominal", "analyticType": "dimension", "offset": 0},
                {"fid": "加班費", "name": "加班費", "basename": "加班費", "analyticType": "measure", "semanticType": "quantitative", "aggName": "sum", "offset": 0}
            ],
            "color": [],
            "opacity": [],
            "size": [],
            "shape": [],
            "radius": [],
            "theta": [],
            "longitude": [],
            "latitude": [],
            "geoId": [],
            "details": [],
            "filters": [],
            "text": [
                {"fid": "加班時數", "name": "加班時數", "basename": "加班時數", "analyticType": "measure", "semanticType": "quantitative", "aggName": "sum", "offset": 0},
                {"fid": "加班費", "name": "加班費", "basename": "加班費", "analyticType": "measure", "semanticType": "quantitative", "aggName": "sum", "offset": 0}
            ]
        },
        "layout": {
            "showActions": False,
            "showTableSummary": False,
            "stack": "stack",
            "interactiveScale": False,
            "zeroScale": True,
            "size": {"mode": "full", "width": 320, "height": 200},
            "format": {},
            "geoKey": "name",
            "resolve": {"x": False, "y": False, "color": False, "opacity": False, "shape": False, "size": False},
            "scaleIncludeUnmatchedChoropleth": False
        },
        "visId": "gw_viz",
        "name": "Chart 1"
    }],
    "chart_map": {},
    "version": "0.4.9.15",
    "workflow_list": [[{"type": "view", "query": [{"op": "aggregate", "groupBy": ["部門", "月份"], "measures": [{"field": "加班費", "agg": "sum", "asFieldKey": "加班費_sum"}]}]}]]
}

# 啟動 PyGWalker 互動視覺化，並套用配置
# 使用核心（kernel）進行計算，而不是在前端瀏覽器中進行計算，減少瀏覽器的負擔。
walker = pyg.walk(df, spec=vis_spec, use_kernel_calc=True)
