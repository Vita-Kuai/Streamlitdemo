# WordCloud04.py
import os
from collections import Counter

import jieba
import matplotlib.pyplot as plt

from wordcloud import WordCloud

# 設定 matplotlib 中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei', 'Arial Unicode MS']  # 繁體中文字型
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題

# 取得腳本所在目錄
script_dir = os.path.dirname(__file__)
# 相對於腳本的上層目錄
file_name = "WordCloud02.txt"
file_path = os.path.join(script_dir, "WordCloud02.txt")

# 讀取文本檔案
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 2. 分詞 (中文)
words = jieba.cut(text)

# 3. 去除停用詞 (簡化版，實際應有完整停用詞表)
stopwords = {'是', '一種', '廣泛', '使用'}
filtered_words = [word for word in words if word not in stopwords and len(word) > 1]

# 4. 統計詞頻
word_counts = Counter(filtered_words)

# 5. 製作詞雲
font = 'msjh.ttc'  # 微軟正黑體
wordcloud = WordCloud(
    width=800, height=400,
    background_color='white',
    font_path=font
).generate_from_frequencies(word_counts)

# 6. 繪製長條圖
top_n = 10
most_common_words = word_counts.most_common(top_n)
words_list, counts_list = zip(*most_common_words)

plt.figure(figsize=(10, 5))
plt.bar(words_list, counts_list)
plt.title(f'Top {top_n} 關鍵字頻率')
plt.xlabel('關鍵字')
plt.ylabel('頻率')
plt.xticks(rotation=45)
plt.show()
