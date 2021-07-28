import requests
import re
from bs4 import BeautifulSoup

for i in range(1, 6): 
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    res = requests.get(url, headers=header)

    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # 광고 상품 제외 + 리뷰 100개 이상, 평점 4.5 이상 되는 것, 애플 제외해서 조회
    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})     #태그가 li인 것 중 속성에서 class가 search_product로 시작하는 것들을 받아오기. 정규식 사용해서 정규식 패턴과 일치하는 것만 받아오고 있음

    for item in items:

        ad_badge = item.find("span", attrs={"class" : "ad-badge-text"})
        if ad_badge:
            continue

        name = item.find("div", attrs={"class" : "name"}).get_text()
        if "Apple" in name:
            continue

        price = item.find("strong", attrs={"class" : "price-value"}).get_text()

        rate =  item.find("em", attrs={"class" : "rating"}) 
        if rate:
            rate = rate.get_text()
        else:
            continue
        
        rate_count = item.find("span", attrs={"class" : "rating-total-count"}) 
        if rate_count:
            rate_count = rate_count.get_text()  #(596)
            rate_count = rate_count[1:-1]
        else:
            continue

        link = item.find("a", attrs={"class": "search-product-link"})["href"]           #item에서 태그가 a인 엘리먼트 중 속성에서 class = search-product-link이고 href인 값 
        
        if float(rate) >= 4.5 and int(rate_count) >= 100:
            print(f"제품명: {name}")
            print(f"가격: {price}")
            print(f"평점 : {rate}점 {rate_count}개")
            print("바로가기 : {}".format( "https://www.coupang.com" + link))
            print("-"*100)