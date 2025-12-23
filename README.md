# Streamlit & Dash 資料視覺化範例集

## 專案概要
- 集合多個以 Streamlit、Dash/Plotly 為主的互動式資料視覺化範例，涵蓋儀表板、表格、圖表及資料探索。
- 包含 Seaborn/Matplotlib 的靜態圖表示例，以及 PyGWalker 的低程式碼資料探索腳本。
- 主要展示資料處理、圖表繪製、互動控制、資料庫/檔案載入等常見情境。

## 專案結構
- `app.py`：Streamlit 健康數據儀表板（步數、睡眠、心率、卡路里）。
- `Dash/`：多個 Dash 應用（含 Plotly 圖表、控制面板、資料表），如 `Dash21.py` 的銷售分析儀表板。
- `Streamlit/`：系列 Streamlit 範例（表單、圖表、Altair、SQLite 資料載入、檔案讀取等）。
- `PyGWalker/`：PyGWalker 互動式資料探索腳本與 CSV 範例。
- `Seaborn/`：Seaborn + Matplotlib 圖表範例。
- `test_dataframe.py`, `test_seaborn.py`：基本測試與圖表輸出示例。

## 主要套件與用途
- `streamlit`：快速打造互動式網頁應用與儀表板（側邊欄、表格、圖表）。
- `dash`, `plotly`：建構多頁控制面板、互動圖表（線圖、圓餅圖、散點圖）；`dash-ag-grid`、`dash-mantine-components` 擴充表格與 UI 元件。
- `pandas`, `numpy`：資料清理、統計計算、隨機數據生成。
- `seaborn`, `matplotlib`：靜態資料視覺化（長條圖、散點圖、盒鬚圖等）。
- `altair`：宣告式圖表繪製（Streamlit 內嵌）。
- `pygwalker`：以類似 Tableau 的介面快速探索資料。
- 其他：`sympy`（數學運算示例）、`sqlite3`/`os`/`json`（檔案與資料庫存取）、`datetime`/`time`（時間處理）。

## 環境設定
1) 建議使用 Python 虛擬環境（如 `python -m venv .venv` 並啟用後）。
2) 安裝主要套件：
```pip install streamlit dash plotly pandas numpy seaborn matplotlib altair pygwalker dash-ag-grid dash-mantine-components sympy "dash[cloud]" ```
