# Streamlit22.py
import os
import sqlite3

# 取得腳本所在目錄
script_dir = os.path.dirname(__file__)
# 相對於腳本的上層目錄
db_path = os.path.join(script_dir, "Demo.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    UserName TEXT,
    Gender TEXT
)
""")
conn.commit()

cursor.execute("INSERT INTO Users (UserName, Gender) VALUES (?, ?)", ("王小明", "男"))
cursor.execute("INSERT INTO Users (UserName, Gender) VALUES (?, ?)", ("李小華", "女"))

conn.commit()
conn.close()

