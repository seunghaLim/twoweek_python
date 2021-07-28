import requests
from bs4 import BeautifulSoup


for year in range (2015, 2020):      #2015년부터 2019년까지 이미지 다운

    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class" : "thumb_img"})

    for idx, image in enumerate(images):    #enumerate - 숫자화하다 상위 5개만 반복해서 다운받음
        #print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):      #image_url 앞에 //가 없으면 // 붙여줌 
            image_url = "https:" + image_url

        print(image_url)

        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)  #image_res의 콘텐츠를 파일에 저장

        if idx >= 4:        #상위 5개 이미지만 다운받아옴
            break