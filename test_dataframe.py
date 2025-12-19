import pandas as pd
df = pd.DataFrame({
    'name': ['Tom', 'Amy', 'John'],
    'age': [20, 25, 30]
})
print(df)
# print(df.shape) # (3, 2)
# print(df.head())
# print(df.head(2))
# print(df.info())
age = df['age']
list = df[['name', 'age']]
age1 = df[['age']]
# print(age) # 沒有欄位age
# print(age1) #有欄位age
# print(list)
iloc1 = df.iloc[0]
print(iloc1) #沒有index
iloc2 = df.iloc[[0]]
print(iloc2) #有index
print(df.iloc[1]['age']) # 25
print(df.loc[1, 'age']) # 25