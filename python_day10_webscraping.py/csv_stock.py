import csv
import requests
from bs4 import BeautifulSoup

#시가총액 상위 20위 기업 정보

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

#csv 파일 만들기
filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")       #newline="" 엔터로 들어가는 new line을 공백으로 만들어줌
writer = csv.writer(f)

#맨 위에 필드 넣기. split("\t")으로 탭으로 구분한 애들이 리스트로 들어가도록 함 
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
print(type(title))      #<class 'list'>
writer.writerow(title)

for page in range (1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class" : "type_2"}).find("tbody").find_all("tr")
    #태그가 table이고 class가 type_2인데 그 밑에 tbody 안에서 그 밑에 tr을 찾음

    for row in data_rows:
        columns = row.find_all("td")    #tr(row) 안에 있는 td가 뭍은 태그를 찾음
        if len(columns) <= 1:       #불필요한 columns 데이터 제거
            continue
        data = [column.get_text().strip() for column in columns]    #td 하나씩 가져와서 텍스트만 출력. strip함수 - 불필요한 탭키나 개행문자 제거
        #print(data)
        writer.writerow(data)   #리스트 형태를 넣어줘야 됨. 