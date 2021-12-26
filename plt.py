import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#전처리 완료한 데이터 불러오기
df = pd.read_excel('경기 및 asos.xlsx')
df.drop(df.columns[0], axis=1, inplace=True)

#특정팀의 승리경기 추출
kia_home_match = df[df['홈팀'] == 'KIA']
kia_home_wins = kia_home_match[kia_home_match['홈팀 점수'] > kia_home_match['원정팀 점수']]
kia_home_loses = kia_home_match[kia_home_match['홈팀 점수'] < kia_home_match['원정팀 점수']]

kia_away_match = df[df['원정팀'] == 'KIA']
kia_away_wins = kia_away_match[kia_away_match['원정팀 점수'] > kia_away_match['홈팀 점수']]
kia_away_loses = kia_away_match[kia_away_match['원정팀 점수'] < kia_away_match['홈팀 점수']]

kia_wins = pd.concat([kia_home_wins, kia_away_wins])
kia_loses = pd.concat([kia_home_loses, kia_away_loses])



#plt를 활용한 그림 그리기
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)


#_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax1.scatter(kia_wins['날짜'], kia_wins['불쾌지수'])
ax1.scatter(kia_loses['날짜'], kia_loses['불쾌지수'])

ax2 = fig.add_subplot(2, 1, 2)