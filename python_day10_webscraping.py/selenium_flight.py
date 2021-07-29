from selenium import webdriver
# 네이버 항공권 검색 및 상품 선택

import selenium
#창이 로딩될 때까지 대기했다가 로딩 다 되면 명령 수행하는 방법
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()       #창 최대화


url = "https://flight.naver.com/flights/"
browser.get(url)


#가는날 선택
browser.find_element_by_link_text("가는날 선택").click()
browser.find_element_by_xpath("//*[@id='l_8']/div[1]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/table/tbody/tr[4]/td[6]").click()

#오는날 선택
browser.find_element_by_xpath("//*[@id='l_8']/div[1]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/table/tbody/tr[5]/td[3]").click()

#목적지 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권 버튼 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    #브라우저를 최대 10초동안 대기함 until xpath인 //~ 이 엘리먼트가 나올 때까지
    elem = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    
    #첫번째 결과 출력
    print(elem.text)
    # elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
    # print(elem)

finally:
    browser.quit()

