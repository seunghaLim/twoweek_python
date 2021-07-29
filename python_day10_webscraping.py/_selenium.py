#크롬 웹 드라이버 객체를 생성하고 넣어준 url로 이동

from selenium import webdriver
browser = webdriver.Chrome()        

#네이버로 이동
browser.get("http://naver.com")

#로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#일회용 번호로 로그인
elem = browser.find_element_by_id("log.otn").click()


#일회용 버튼 입력
browser.find_element_by_id("disposable").send_keys("12345")

#로그인 버튼 누르기
browser.find_element_by_id("otnlog.login").click()

#값 지우는 방식 
# browser.find_element_by_id("disposable").clear()

#html 정보 출력
print(browser.page_source)

#브라우저 종료

#browser.close() #현재 탭만 종료
browser.quit()  #전체 브라우저 종료