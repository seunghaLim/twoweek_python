import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=728015&weekday=wed"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#페이지 안에 제목과 링크를 가져오는 방법

# cartoons = soup.find_all("td", attrs={"class" : "title"})
# title = cartoons[0].a.get_text()    #a태그의 텍스트만 가져와라
# link = cartoons[0].a["href"]    #속성 가져올 때는 대괄호. a태그의 href 속성을 가져와라
# print(title)
# print("https://comic.naver.com" + link)

# #페이지 안에 제목과 링크를 전부 가져오는 방법 - 반복문 사용

# cartoons = soup.find_all("td", attrs={"class" : "title"})

# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

#페이지 안에 평점 점수 가져오고 평균 구하기

cartoons = soup.find_all("div", attrs={"class": "rating_type"})

total = 0
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()        #cartoon 안에서 strong 태그를 찾고 거기서 텍스트만 가져옴
    print(rate)
    total += float(rate)        #rate가 str일 테니 float 형으로 바꿔줌

print("전체 점수 : ", total)
print("점수 평균 : ", total / len(cartoons))
