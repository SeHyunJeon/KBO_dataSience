import pandas as pd

data = pd.read_excel('2018~2020 KBO 경기 결과.xlsx')
asos = pd.read_excel('야구 경기장 목록.xlsx')

data.drop(data.columns[0], axis=1, inplace=True)
data = data.dropna()

data = data.astype({'TEAM1_SCORE': 'int'})
data = data.astype({'TEAM2_SCORE': 'int'})


print(data.dtypes)

place_list = list()

for i in range(1, len(data)):
   place = data['구장'][i]
   place_list.append(place)
   

