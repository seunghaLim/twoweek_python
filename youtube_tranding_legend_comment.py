import time
from bs4 import BeautifulSoup
from bs4.element import Comment 
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

url =  "https://www.youtube.com/"
browser.get(url)

#탐색 클릭 후 첫번째 동영상 제목 저장 및 클릭
time.sleep(3)
browser.find_element_by_class_name("style-scope ytd-guide-section-renderer").click()
time.sleep(2)
browser.find_element_by_class_name("style-scope ytd-video-renderer").click()

soup = BeautifulSoup(browser.page_source, "lxml")

title = soup.find("a", attrs = {"id" : "video-title"}).get_text().strip()
print(f"실시간 트렌드 영상 1위 : {title}")

#스크롤 내리기 
time.sleep(1)
browser.execute_script("window.scrollTo(0, 700)")

#상위 5개 댓글 닉네임과 내용 불러오기 
time.sleep(2)

soup = BeautifulSoup(browser.page_source, "lxml")

IDs = []
Comments = []

#닉네임 불러오기
users = soup.find_all("a", attrs = {"id" : "author-text"}, limit=5)
for user in users:
    user.find("span", attrs = {"class" : "style-scope ytd-comment-renderer"})      #여기다가 get text 붙이면 값 더럽게 나옴 왜??
    temp = user.get_text().strip()
    IDs.append(temp)

#내용 불러오기
comments = soup.find_all("yt-formatted-string", attrs ={"id" : "content-text"}, limit=5)
for comment in comments:
    temp = comment.get_text()
    Comments.append(temp)

print("{0} : {1}".format(IDs[0], Comments[0]))
print("{0} : {1}".format(IDs[1], Comments[1]))
print("{0} : {1}".format(IDs[2], Comments[2]))
print("{0} : {1}".format(IDs[3], Comments[3]))
print("{0} : {1}".format(IDs[4], Comments[4]))






