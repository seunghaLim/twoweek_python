#headless / 브라우저가 안 뜨고 데이터를 처리할 수 있음
# 동적 페이지에서 selenium 이용해서 데이터 가져오기. 
import time
from selenium import webdriver

#headless로 크롬 접근하는 법
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
#주의 - headless 크롬으로 접근할 때 유저 에이전트에 HeadlessChrome 이라고 뜸. 그럴땐 아래처럼 해줘야 함
#options.add_argument("user-agent=유저 에이전트 주소")


browser = webdriver.Chrome(options = options)
browser.maximize_window()

url =  "https://play.google.com/store/movies/top"
browser.get(url)

#로딩 시간 2초 지정
interval = 2 

# 현재 문서 높이를 가져와서 prev_h에 저장
prev_h = browser.execute_script("return document.body.scrollHeight")

#반복 수행
while True:
    # 페이지 제일 끝까지 스크롤 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    #2초 로딩
    time.sleep(interval)    

    #현재 문서 높이를 가져와서 저장
    curr_h = browser.execute_script("return document.body.scrollHeight")
    if prev_h == curr_h:
        break

    #prev_h 갱신
    prev_h = curr_h

import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"

soup = BeautifulSoup(browser.page_source, "lxml")       #browser.page_source는 res.text와 비슷한 역할 

movies = soup.find_all("div", attrs={"class" :  "Vpfmgd"})        #리스트 안에 있는 클래스를 모두 가져옴


#할인 이벤트 진행하는 영화 이름 가져오기 
for movie in movies:
    title = movie.find("div", attrs={"class" : "WsMG1c nnK0zc"}).get_text()

    #할인 전 금액 
    original_price = movie.find("span", attrs={"class" : "SUZt4c djCuy"})
    if not original_price:
        #print("{}은 할인 이벤트를 진행하지 않습니다".format(title))
        continue
    original_price = original_price.get_text()

    #할인된 가격
    sale_price = movie.find("span", attrs={"class" : "VfPpfd ZdBevf i5DZme"}).get_text()

    #링크
    link = movie.find("a", attrs = {"class" : "JC71ub"})["href"]
    link = "https://play.google.com" + link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인된 가격: {sale_price}")
    print(f"링크 : {link}")
    print("-"*100)
    


