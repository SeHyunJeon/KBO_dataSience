import pandas as pd
import matplotlib.pyplot as plt


#데이터 불러오기
data = pd.read_excel('2018~2021 KBO 경기 결과.xlsx')

#읽어드린 엑셀 데이터의 1열 및 1행이 nan 값임. 따라서 삭제
data.drop(data.columns[0], axis=1, inplace=True)
data = data.dropna()

#스코어 열의 형변환
data = data.astype({'원정팀 점수': 'int'})
data = data.astype({'홈팀 점수': 'int'})

#ASOS 데이터프레임 생성
data_asos = {'구장':['마산', '창원', '대구', '잠실', '고척', '광주', '문학', '수원', '사직', '대전', '울산', '포항', '청주'], 
             'asos':['155', '155', '143', '108', '108', '156', '112', '119', '159', '133', '152', '138', '131']}

asos = pd.DataFrame(data_asos)

#구장을 기준으로 join
data = pd.merge(data, asos, left_on='구장', right_on='구장', how='left')

#날짜 형식 변환
data['날짜'] = pd.to_datetime(data['날짜'])

#날짜를 기준으로 정렬
data = data.sort_values('날짜')

#취소된 경기들 삭제(점수가 -1점인 경기)
drop_index = data[data['원정팀 점수'] == -1].index
data.drop(drop_index, inplace=True)

drop_index = data[data['홈팀'] == "드림"].index
data.drop(drop_index, inplace=True)

drop_index = data[data['홈팀'] == "나눔"].index
data.drop(drop_index, inplace=True)

#기온 데이터 불러오기 
data_asos = pd.read_csv('asos_data.csv')
data_asos['날짜'] = pd.to_datetime(data_asos['날짜'])

#날짜를 기준으로 정렬
data_asos = data_asos.sort_values('날짜')

#data_asos asos를 object로 변환
data_asos = data_asos.astype({'asos':'str'})

#asos, 날짜를 기준으로 join
data = pd.merge(left=data, right=data_asos, how='left',
                on=['asos', '날짜'], sort=True)

data.drop(data.columns[7], axis=1, inplace=True)

data.to_excel ("경기 및 asos.xlsx")

#특정팀의 승리경기 추출
kia_home_match = data[data['홈팀'] == 'KIA']
kia_home_wins = kia_home_match[kia_home_match['홈팀 점수'] > kia_home_match['원정팀 점수']]

kia_away_match = data[data['원정팀'] == 'KIA']
kia_away_wins = kia_away_match[kia_away_match['원정팀 점수'] > kia_away_match['홈팀 점수']]

kia_wins = pd.concat([kia_home_wins, kia_away_wins])


print(data.dtypes)
print(data_asos.dtypes)



