# 文字雲遮罩範例(文字雲)

# WordCloud06.py
import os
from collections import Counter

import jieba
import matplotlib.pyplot as plt
import numpy
import requests
from bs4 import BeautifulSoup
from PIL import Image

from wordcloud import WordCloud

# 設定 matplotlib 中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei', 'Arial Unicode MS']  # 繁體中文字型
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題

# 儲存所有抓取的文字
all_text = ''

# 目標新聞網址 (中央社)
# 美國再宣布對台軍售　含M109A7自走砲標槍飛彈等8案
url = 'https://www.cna.com.tw/news/aipl/202512180038.aspx'

# 模擬瀏覽器請求頭
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 發送 GET 請求
response = requests.get(url, headers=headers)
# 設定正確的編碼,中央社使用 UTF-8 編碼
response.encoding = 'utf-8'

# 檢查請求是否成功
if response.status_code == 200:
    # 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser' )

    # 抽取新聞內容,找出整個網頁內的p標籤，而且該標籤沒有class屬性。
    texts = soup.select('div.centralContent div.paragraph > p:not([class])')

    # 1. 合併所有文字
    for t in texts:
        all_text += t.text.strip()

    if all_text != '':
        # 2. 分詞 (中文)
        words = jieba.cut(all_text)

        # 3. 去除停用詞 (簡化版，實際應有完整停用詞表)
        stopwords = {'是', '一種', '廣泛', '使用', '的', '在', '和', '了', '與', '等', '、', '。', '，'}
        filtered_words = [word.strip() for word in words if word.strip() not in stopwords and len(word.strip()) > 1]

        # 4. 統計詞頻
        word_counts = Counter(filtered_words)

        # 5. 製作詞雲 (加入檢查)
        if len(word_counts) == 0:
            print("錯誤: 沒有找到任何詞彙，請檢查網頁抓取是否成功")
        else:
            # 取得腳本所在目錄
            script_dir = os.path.dirname(__file__)
            # 相對於腳本的上層目錄
            file_name = "WordCloud06.png"
            file_path = os.path.join(script_dir, file_name)


            # 建立遮罩
            mask = numpy.array(Image.open(file_path))


            # 產生詞雲
            font = 'msjh.ttc'  # 微軟正黑體
            wordcloud = WordCloud(
                width=800, height=400,
                background_color='white',
                font_path=font,
                mask=mask
            ).generate_from_frequencies(word_counts)

            # 6. 繪圖
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.title('新聞關鍵字分佈詞雲')
            plt.show()
