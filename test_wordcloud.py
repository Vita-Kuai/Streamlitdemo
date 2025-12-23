
import os
from collections import Counter

import matplotlib.pyplot as plt

from wordcloud import STOPWORDS, WordCloud

# 設定 matplotlib 中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei', 'Arial Unicode MS']  # 繁體中文字型
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題

# 目標檔案 CNN 新聞
# 取得腳本所在目錄
script_dir = os.path.dirname(__file__)
# 相對於腳本的上層目錄
file_name = "test_wordcloud.txt"
file_path = os.path.join(script_dir, file_name)

# 1. 讀取文本檔案
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 2. 停用詞 (英文)
english_stopwords = set(STOPWORDS)

# 3. 文本處理 - 將文本轉為小寫並分詞
words = text.lower().split()

# 4. 過濾停用詞並統計詞頻
filtered_words = [word.strip('.,!?":;()[]') for word in words
                  if word.strip('.,!?":;()[]') and word.lower() not in english_stopwords]

word_counts = Counter(filtered_words)

# 5. 製作詞雲 (加入檢查)
if len(word_counts) == 0:
    print("錯誤: 沒有找到任何詞彙，請檢查檔案抓取是否成功")
else:
    # 產生詞雲
    font = 'msjh.ttc'  # 微軟正黑體
    wordcloud = WordCloud(
        width=800, height=400,
        background_color='white',
        font_path=font
    ).generate_from_frequencies(word_counts)

    # 6. 繪圖
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('新聞關鍵字分佈詞雲')
    plt.show()
