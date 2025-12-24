from collections import Counter

import jieba
import matplotlib.pyplot as plt
import nltk
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from PIL import Image
import numpy as np
import os
from wordcloud import WordCloud
from collections import Counter

# 下載 nltk 停用詞 (若需要)
nltk.download('stopwords')
font_path = 'C:\\Windows\\Fonts\\msjh.ttc'
# 設定 matplotlib 使用下載的字體
# 修正：直接使用 font_manager.fontManager.addfont

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei', 'Arial Unicode MS']  # 繁體中文字型
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題


# plt.rcParams['font.family'] = 'Noto Sans CJK TC'
# plt.rcParams['axes.unicode_minus'] = False

# 失敗但覺得很怪應該不會錯所以還是保留了這個版本

import re
from PIL import Image

script_dir = os.path.dirname(__file__)
# 相對於腳本的上層目錄
file_name = "test_wordcloud02.txt"
file_path = os.path.join(script_dir, file_name)

# 讀取文本檔案
# with open(file_path, 'r', encoding='utf-8') as f:
#     text = f.read()

# 1. 讀取文本檔案
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        all_text = f.read()
except FileNotFoundError:
    print(f"錯誤：找不到檔案 {file_path}，請確認檔案已上傳至左側資料夾。")
    all_text = ""

if all_text:
    # 2. 文本處理 - 使用 jieba 分詞
    words = jieba.cut(all_text)

    # 3. 取得停用詞 (自定義或 NLTK)
    # 注意：NLTK 的 chinese 停用詞通常較少，建議可自行增加
    stop_words = set(stopwords.words('chinese'))
    # 額外手動加入一些常見符號或無意義詞
    extra_stops = {'的', '了', '在', '是', '我', '你', '他', '她', '它', '與', '和', '就', 'Casey','Lee', '涵薇', '貼圖','emoji','圖片','http', 'https','si'}

    # 將所有數字加入停用詞
    numbers = set(re.findall(r'\b\d+\.?\d*\b', all_text))
    extra_stops.update(numbers)

    stop_words.update(extra_stops)

    # 4. 過濾停用詞並統計詞頻
    # 條件：長度大於1 且 不在停用詞清單內
    filtered_words = [word.strip() for word in words
                      if word.strip() and word not in stop_words and len(word.strip()) > 1]

    word_counts = Counter(filtered_words)

    # 載入遮罩圖片
    mask = np.array(Image.open('cloud.jpg'))
    print(mask)
    # 5. 製作詞雲
    if not word_counts:
        print("錯誤: 沒有找到任何詞彙，請檢查檔案抓取是否成功或分詞結果。")
    else:
        # 產生詞雲 (指定剛才下載的 font_path)
        wordcloud = WordCloud(
            width=1000,
            height=600,
            background_color='white',
            # background_color='black',
            colormap='Set2',
            random_state=42,
            margin=2,
            font_path=font_path,  # 這裡一定要指向 font.ttf
            mask=mask # 使用遮罩
        ).generate_from_frequencies(word_counts)

        # 6. 繪圖
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('皮皮聊天室文字雲')
        plt.show()