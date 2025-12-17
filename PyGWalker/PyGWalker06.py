# PyGWalker06.py
import os

import pandas as pd

import pygwalker as pyg

# 取得腳本所在目錄
script_dir = os.path.dirname(__file__)
# 相對於腳本的上層目錄
db_path = os.path.join(script_dir, "kaggle_income.csv")

df = pd.read_csv(db_path, encoding="utf-8")

walker = pyg.walk(df)
