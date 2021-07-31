import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

url =  "https://www.daum.net/"
browser.get(url)

#검색창에 검색어 입력
browser.find_element_by_id("q").send_keys("송파 엠스테이트")
browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]").click()

#스크롤 내리기
browser.execute_script("window.scrollTo(0, 100)")


#beatifulsoup으로 정보 가져오기
soup = BeautifulSoup(browser.page_source, "lxml")       #browser.page_source는 res.text와 비슷한 역할 

h_rows = soup.find("table", attrs={"class" : "tbl"}).find("tbody").find_all("tr")   #table을 찾고 첫 번째 tbody를 찾은 다음에 그 밑에 있는 모든 tr을 찾음

index = 1
for row in h_rows:      #for index, row in enumerate(h_rows) - 인덱스와 행 둘 다 가져오기

    type = row.find("td", attrs={"class" : "col1"}).get_text()
    size = row.find("td", attrs={"class" : "col2"}).get_text().strip()
    price = row.find("td", attrs={"class" : "col3"}).get_text().strip()
    location = row.find("td", attrs={"class" : "col4"}).get_text()
    height = row.find("td", attrs={"class" : "col5"}).get_text()

    print("\n")
    print("="*11, "매물", index, "="*11)
    print(f"거래 : {type}")
    print(f"면적 : {size} (공급)")
    print(f"가격 : {price} (만원)")
    print(f"동 : {location}")
    print(f"층 : {height}")

    index += 1

browser.quit()


