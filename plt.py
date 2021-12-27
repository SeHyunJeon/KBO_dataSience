import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#전처리 완료한 데이터 불러오기
df = pd.read_excel('경기 및 asos.xlsx')
df.drop(df.columns[0], axis=1, inplace=True)

#특정팀의 승리경기 추출
kia_home_matchs = df[df['홈팀'] == 'KIA']
kia_home_wins = kia_home_matchs[kia_home_matchs['홈팀 점수'] > kia_home_matchs['원정팀 점수']]
kia_home_loses = kia_home_matchs[kia_home_matchs['홈팀 점수'] < kia_home_matchs['원정팀 점수']]
kia_home_draws = kia_home_matchs[kia_home_matchs['홈팀 점수'] == kia_home_matchs['원정팀 점수']]

kia_away_matchs = df[df['원정팀'] == 'KIA']
kia_away_wins = kia_away_matchs[kia_away_matchs['원정팀 점수'] > kia_away_matchs['홈팀 점수']]
kia_away_loses = kia_away_matchs[kia_away_matchs['원정팀 점수'] < kia_away_matchs['홈팀 점수']]
kia_away_draws = kia_away_matchs[kia_away_matchs['원정팀 점수'] == kia_away_matchs['홈팀 점수']]

kia_wins = pd.concat([kia_home_wins, kia_away_wins])
kia_wins['result'] = 1
kia_loses = pd.concat([kia_home_loses, kia_away_loses])
kia_loses['result'] = 0
kia_draws = pd.concat([kia_home_draws, kia_away_draws])
kia_draws['result'] = -1

kia_matchs = pd.concat([kia_wins, kia_loses, kia_draws])

kia_matchs.rename(columns={'날짜':'date'}, inplace = True)
kia_matchs.rename(columns={'구장':'place'}, inplace = True)
kia_matchs.rename(columns={'원정팀':'away_team'}, inplace = True)
kia_matchs.rename(columns={'원정팀 점수':'away_team_score'}, inplace = True)
kia_matchs.rename(columns={'홈팀':'home_team'}, inplace = True)
kia_matchs.rename(columns={'홈팀 구장':'home_team_score'}, inplace = True)
kia_matchs.rename(columns={'기온':'temp'}, inplace = True)
kia_matchs.rename(columns={'풍속':'wind_speed'}, inplace = True)
kia_matchs.rename(columns={'습도':'huminity'}, inplace = True)
kia_matchs.rename(columns={'불쾌지수':'discomfort_index.'}, inplace = True)
kia_matchs.rename(columns={'체감온도':'sensory_temperature'}, inplace = True)

#plt를 활용한 그림 그리기
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)

#_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
#ax1.scatter(kia_wins['날짜'], kia_wins['불쾌지수'])
#ax1.scatter(kia_loses['날짜'], kia_loses['불쾌지수'])
ax1.plot(kia_wins['asos'])
ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(kia_loses['asos'])

import seaborn as sns
sns.pairplot(kia_matchs, hue='result') # hue 에 'Type'을 지정하면, Type에는 두 종류 데이터가 있어서 두 개의 색으로 표출

