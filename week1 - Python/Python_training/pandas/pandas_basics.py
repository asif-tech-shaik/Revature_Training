import pandas as pd

data=[1,2,3,4,5]
print(type(data))
series=pd.Series(data)
print(series)
print(type(series))

data={
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['New York','San Fransco','Los Angeles']
}
df=pd.DataFrame(data)
print(df)

print('head \n',df.head())
print('tail -2 \n',df.tail(2))

print(df.info())
print('desc \n',df.describe())

print(df['Name'])
print(df[['Name','City']])

print(df[df['Age']>30])
