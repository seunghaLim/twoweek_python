import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

for page in range (1, 2):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class" : "type_2"}).find("tbody").find_all("tr")
    #태그가 table이고 class가 type_2인데 그 밑에 tbody 안에서 그 밑에 tr을 찾음

    for row in data_rows:
        columns = row.find_all("td")    #tr(row) 안에 있는 td가 뭍은 태그를 찾음
        data = [column.get_text() for column in columns]    #td 하나씩 가져와서 텍스트만 출력
        print(data)