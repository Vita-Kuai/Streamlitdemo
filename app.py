# 導入必要的函式庫
import streamlit as st  # Streamlit：用於建立網頁應用程式
import pandas as pd  # Pandas：資料處理和分析
import numpy as np  # NumPy：數值計算和隨機數生成
import plotly.express as px  # Plotly：繪製互動式圖表
from datetime import datetime, timedelta  # 日期和時間處理

# --- 1. 數據生成與處理 ---

# 設置 Streamlit 頁面配置（寬版佈局、設定頁面標題）
st.set_page_config(layout="wide", page_title="個人健康追蹤儀表板")

# 使用 @st.cache_data 裝飾器快取資料，避免重複執行函式
@st.cache_data
def generate_fake_health_data(days=90):
    """生成虛假的健康數據 (步數、睡眠、心率)"""
    # 取得今天的日期
    end_date = datetime.now().date()
    # 計算起始日期（往前推 days-1 天）
    start_date = end_date - timedelta(days=days - 1)
    # 使用 pd.date_range 生成日期序列（每日一筆）
    dates = pd.date_range(start_date, end_date, freq='D')

    # 建立字典，儲存各項健康數據
    data = {
        'Date': dates,  # 日期欄位
        'Steps': np.random.randint(4000, 15000, size=days),  # 隨機步數（4000-15000步）
        'Sleep_Hours': np.round(np.random.uniform(5.5, 9.0, size=days), 1),  #最後的 1 是指「小數點位數」。 # 隨機睡眠時數（5.5-9小時）
        'Resting_HR': np.random.randint(55, 75, size=days),  # 隨機靜息心率（55-75 bpm）
        'Calories_Burned': np.random.randint(1800, 3000, size=days)  # 隨機卡路里消耗（1800-3000卡）
    }
    # 將字典轉換成 DataFrame（表格格式）
    df = pd.DataFrame(data)
    # 回傳資料框
    return df

# 呼叫函式生成 90 天的虛假健康數據
health_df = generate_fake_health_data()

# --- 2. Streamlit 側邊欄 (Sidebar) ---

# 在側邊欄中顯示標題
st.sidebar.header("📊 數據篩選與控制")

# 取得資料框中最大日期並轉換為日期格式
max_date = health_df['Date'].max().date()
# 取得資料框中最小日期並轉換為日期格式
min_date = health_df['Date'].min().date()

# 在側邊欄建立日期範圍滑桿
# value：預設值（最近30天的日期範圍）
date_range = st.sidebar.slider(
    "選擇日期範圍",
    value=(max_date - timedelta(days=29), max_date), #預設值是今天往前數29天
    format="YYYY/MM/DD" # 決定滑桿顯示的日期格式
)
# 將選取的日期範圍解析為起始和結束日期
# 預設的起始結束日期
start_date, end_date = date_range # 滑桿回傳一個包含兩個日期的tuple

# 根據選取的日期範圍篩選資料
# 篩選條件：日期在 start_date 和 end_date 之間
filtered_df = health_df[
    (health_df['Date'].dt.date >= start_date) &
    (health_df['Date'].dt.date <= end_date)
]

# --- 3. Streamlit 主標題與關鍵指標 (Metrics) ---

# 顯示頁面主標題
st.title("🏃 個人健康數據追蹤儀表板")
# 顯示分割線
st.markdown("---")

# 建立三個並排的列（用來展示三個指標）
col1, col2, col3 = st.columns(3)

# 計算篩選資料中的平均步數
current_avg_steps = filtered_df['Steps'].mean()
# 取得上個週期的資料（時間跨度相同）
last_period_df = health_df[
    (health_df['Date'].dt.date >= start_date - (end_date - start_date)) &
    (health_df['Date'].dt.date < start_date)
]
# 計算上個週期的平均步數，如果沒有資料則使用目前平均值
last_avg_steps = last_period_df['Steps'].mean() if not last_period_df.empty else current_avg_steps

# 在第一個列中顯示「平均每日步數」指標
step_delta = current_avg_steps - last_avg_steps
col1.metric(
    label="平均每日步數",  # 指標標題
    value=f"{current_avg_steps:,.0f} 步",  # 顯示的數值
    delta=f"{step_delta:,.0f} 步 vs. 上個週期"  # 與上個週期的差異
)

# 在第二個列中顯示「平均睡眠時長」指標
avg_sleep = filtered_df['Sleep_Hours'].mean()
col2.metric(
    label="平均睡眠時長",  # 指標標題
    value=f"{avg_sleep:.1f} 小時",  # 顯示的數值
    delta_color="off"  # 關閉箭頭顏色變化
)

# 在第三個列中顯示「平均靜息心率」指標
avg_hr = filtered_df['Resting_HR'].mean()
col3.metric(
    label="平均靜息心率 (HR)",  # 指標標題
    value=f"{avg_hr:.0f} bpm",  # 顯示的數值
    delta="目標: < 65 bpm"  # 顯示目標值
)

# 顯示分割線
st.markdown("---")

# --- 4. 可視化圖表 ---

# 在側邊欄建立下拉選單，讓使用者選擇要查看的指標
# format_func：將欄位名稱格式化為更易讀的格式（用空格替換底線，並首字大寫）
metric_to_plot = st.selectbox(
    "選擇要查看的趨勢指標",  # 選單標籤
    ['Steps', 'Sleep_Hours', 'Resting_HR', 'Calories_Burned'],  # 可選擇的指標清單
    format_func=lambda x: x.replace('_', ' ').title()  # 格式化顯示名稱
)

# 顯示子標題（使用選取的指標名稱）
st.header(f"📈 {metric_to_plot.replace('_', ' ').title()} 趨勢")

# 使用 Plotly 繪製折線圖
fig = px.line(
    filtered_df,  # 使用篩選後的資料
    x='Date',  # X 軸為日期
    y=metric_to_plot,  # Y 軸為選取的指標
    title=f'{metric_to_plot.replace("_", " ").title()} 隨時間變化',  # 圖表標題
    template="plotly_white",  # 選擇白色主題
    labels={'Date': '日期', metric_to_plot: metric_to_plot.replace('_', ' ').title()}  # 設定軸標籤
)

# 如果選取的指標是「步數」，則添加目標線
if metric_to_plot == 'Steps':
    fig.add_hline(
        y=10000,  # 在 Y 軸 10000 處添加水平線
        line_dash="dot",  # 使用虛線
        annotation_text="目標步數",  # 註解文字
        annotation_position="bottom right"  # 註解位置
    )

# 顯示圖表（use_container_width：讓圖表充滿容器寬度）
st.plotly_chart(fig, use_container_width=True)

# 顯示區段標題
st.header("📄 數據詳細表格")
# 顯示篩選後的資料表格（按日期降序排列）
st.dataframe(filtered_df.sort_values(by='Date', ascending=False), use_container_width=True)


