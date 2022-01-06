
# 프로젝트 개요
본 프로젝트에서는 KBO 각 구단들의 정규시즌 성적과 국내 기후 데이터를 활용하여 상호 상관관계를 분석한다.

![KBO 로고](https://user-images.githubusercontent.com/89785498/147881142-108baad3-a0ad-492e-9269-25e905726bc1.png)



# 개발환경
<img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/></a>
<img src="https://img.shields.io/badge/JSON-83B81A?style=flat-square&logo=JSON&logoColor=white"/></a>


# 설명
* __web_crawler.py__
  * KBO 공식 홈페이지에서 정규시즌 경기결과를 불러온다.    -->    2018~2021 KBO 경기 결과.xlsx
* __merge.py__
  * 경기결과와 국내 기상 관측 기구 ASOS 데이터를 merge한다.    -->    경기 및 asos.xlsx
 * __plot__
   * 위에서 생성된 데이터를 분석하여 그래픽화한다.
* __chromedriver.exe__
  * web_crawler가 동작하기 위하여 필요한 소프트웨어
   



# 진행사항
+ 데이터 수집
  + web crawler 제작
  + KBO 정규시즌 경기결과, 국내 기상관측 기구 ASOS 데이터 확보
  + 두 데이터 연결(merge)

 + 데이터 분석

 + 결론 도출




