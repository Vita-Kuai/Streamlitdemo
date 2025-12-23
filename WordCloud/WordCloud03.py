# WordCloud03.py
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

# 載入使用者字典
userdict_path = os.path.join(script_dir, "WordCloud03.txt")
jieba.load_userdict(userdict_path)

#程式內新增、刪除分詞
#如果臨時想增加分詞或刪除分詞，可以透過jieba的add_word()方法和del_word()方法來做到。

# 新增分詞
jieba.add_word('蚵仔煎')

# 刪除分詞
jieba.del_word('不過')

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

# 6. 繪圖
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Python 關鍵字分佈詞雲')
plt.show()
