import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
res = requests.get(url, headers=header)

res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# #이름 가져오기
# items = soup.find_all("li", attrs={"class": re.compile("^search-product")})     #태그가 li인 것 중 속성에서 class가 search_product로 시작하는 것들을 받아오기. 정규식 사용해서 정규식 패턴과 일치하는 것만 받아오고 있음
# #print( items[0].find("div", attrs={"class" : "name"}).get_text())     #items 중 제일 첫번째 아이템인데 태그가 div이고 속성에서 class가 name인 것의 텍스트만 받아오기

# #해당 url 페이지에 있는 아이템 이름, 가격, 평점, 평점수 가져오기
# for item in items:
#     name = item.find("div", attrs={"class" : "name"}).get_text()
#     price = item.find("strong", attrs={"class" : "price-value"}).get_text() 
#     rate =  item.find("em", attrs={"class" : "rating"}) 
#     if rate:
#         rate = rate.get_text()
#     else:
#         rate = "평점 없음"
#     rate_count = item.find("span", attrs={"class" : "rating-total-count"}) 
#     if rate_count:
#         rate_count = rate_count.get_text()
#     else:
#         rate_count = "평점 없음"
    
#     print(name, price, rate, rate_count)

# 광고 상품 제외 + 리뷰 100개 이상, 평점 4.5 이상 되는 것, 애플 제외해서 조회
items = soup.find_all("li", attrs={"class": re.compile("^search-product")})     #태그가 li인 것 중 속성에서 class가 search_product로 시작하는 것들을 받아오기. 정규식 사용해서 정규식 패턴과 일치하는 것만 받아오고 있음
#print( items[0].find("div", attrs={"class" : "name"}).get_text())     #items 중 제일 첫번째 아이템인데 태그가 div이고 속성에서 class가 name인 것의 텍스트만 받아오기

for item in items:

    ad_badge = item.find("span", attrs={"class" : "ad-badge-text"})
    if ad_badge:
        print("     <광고 상품 제외합니다>  ")
        continue

    name = item.find("div", attrs={"class" : "name"}).get_text()
    if "Apple" in name:
        print("     <애플 상품 제외합니다>      ")
        continue

    price = item.find("strong", attrs={"class" : "price-value"}).get_text()

    rate =  item.find("em", attrs={"class" : "rating"}) 
    if rate:
        rate = rate.get_text()
    else:
        print("     <평점 없는 상품 제외합니다>     ")
        continue
    
    rate_count = item.find("span", attrs={"class" : "rating-total-count"}) 
    if rate_count:
        rate_count = rate_count.get_text()  #(596)
        rate_count = rate_count[1:-1]
    else:
        print("     <평점 없는 상품 제외합니다>     ")
        continue
    
    if float(rate) >= 4.5 and int(rate_count) >= 100:
        print(name, price, rate, rate_count)