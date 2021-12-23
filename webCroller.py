import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
from urllib.request import urlopen
from html_table_parser import parser_functions as parser
import pandas as pd
import re

#드라이버 불러오기        
driver = webdriver.Chrome()
driver.get("https://www.koreabaseball.com/Schedule/Schedule.aspx?seriesId=0,9")
assert "경기일정/결과 | 일정/결과 | KBO" in driver.title

#2018년 선택
select_menu=Select(driver.find_element_by_id("ddlYear"))
select_menu.select_by_index(3)

#01월 선택
select_menu=Select(driver.find_element_by_id("ddlMonth")) 
select_menu.select_by_index(0)

#페이지 소스 가져오기
page_source = driver.page_source 
soup = BeautifulSoup(page_source, "html.parser")

#소스 중에서 table 가져오기
temp = soup.find("table", {"class":"tbl"})

#리스트 자료형으로 변환
result = parser.make2d(temp)

#2018년 02월부터 2020년 12월까지 데이터를 리스트에 추가
for year in range(4, 0, -1):
    for month in range(0, 12):
        if(year==4 and month==0):
            continue
        
        select_menu=Select(driver.find_element_by_id("ddlYear"))
        select_menu.select_by_index(year-1)
        
        select_menu=Select(driver.find_element_by_id("ddlMonth")) 
        select_menu.select_by_index(month)
        
        page_source = driver.page_source 
        soup = BeautifulSoup(page_source, "html.parser")
        
        temp = soup.find("table", {"class":"tbl"})
        
        table = parser.make2d(temp)
    
        #속성 중복 방지를 위하여 첫번째 행 삭제
        del table[0]
        
        if(table[0][3] == '데이터가 없습니다.'):
            continue
        
        #날짜 앞에 년도 붙이기
        if(year==4):
            for i in range(0, len(table)):
                table[i][0] = '2018.' + table[i][0]
        elif(year==3):
            for i in range(0, len(table)):
                table[i][0] = '2019.' + table[i][0]
        elif(year==2):
            for i in range(0, len(table)):
                table[i][0] = '2020.' + table[i][0]
        elif(year==1):
            for i in range(0, len(table)):
                table[i][0] = '2021.' + table[i][0]
            
        #결과를 도출하기 위한 최종 테이블에 추가
        result.extend(table)

#예외처리, 위 가정을 거칠 경우 1번째 값이 '데이터가 없습니다.' 이기에 수동으로 삭제하였음
del result[1]

#pandas 라이브러리의 dataFrame 자료형으로 변환
df = pd.DataFrame(data=result[1:], columns=[result[0]])

#필요없는 속성값 삭제
df = df.drop(['게임센터', '하이라이트', 'TV', '라디오'], axis=1)



#리스트에서 요소를 삭제할 때마다 앞당겨져서 인덱스 유지 불가

#result 리스트에서 경기 결과 불러와 match 리스트에 추가(append)
match = list()
for index_result in range(1, len(result)):
    match.append(result[index_result][2])

#match 리스트에 들어있는 각 경기들을 vs로 스플릿하여 split 리스트에 추가(append)
split = list()
for index_match in range(0, len(match)):
    split.append(match[index_match].split('vs'))

#split 리스트에 들어있는 값들을 열 기준으로 (0열: 1팀, 1열: 2팀) 각 리스트에 추가(append)
team1 = list()
team2 = list()
for index_split in range(0, len(split)):
    if(split[index_split] == False):
        continue
    team1.append(split[index_split][0])
    team2.append(split[index_split][1])
    
    #team1.append(''.join([i for i in split[index_split][0] if not i.isdigit()]))
    #team2.append(''.join([i for i in split[index_split][1] if not i.isdigit()]))

#team1 리스트와 team2 리스트를 이용하여 dataFrame에 추가
team1_score = list()
team2_score = list()
temp1 = list()
temp2 = list()
for i in range(0, len(team1)):
    string = team1[i]
    if(re.findall(r'\d+', string) == []):
        team1_score.append(int(-1))
        team2_score.append(int(-1))
        continue
    temp1 = re.findall(r'\d+', string)
    team1_score.append(int(temp1[0]))
    
    string = team2[i]
    temp2 = re.findall(r'\d+', string)
    team2_score.append(int(temp2[0]))

team1 = list()
team2 = list()
for index_split in range(0, len(split)):
    if(split[index_split] == False):
        continue
    
    team1.append(''.join([i for i in split[index_split][0] if not i.isdigit()]))
    team2.append(''.join([i for i in split[index_split][1] if not i.isdigit()]))

df.insert(4, 'TEAM1', team1, True)  
df.insert(5, 'TEAM1_SCORE', team1_score, True)
df.insert(6, 'TEAM2', team2, True)
df.insert(7, 'TEAM2_SCORE', team2_score, True) 

#비고 삭제
df = df.drop(['비고', '경기'], axis=1)

print(df)
df.to_excel("2018~2020 KBO 경기 결과.xlsx")

#스코어가 -1인 경기들은 취소된 경기들이므로 제거하여야함 
#팀명에서 점수 제거하여야함 































