#requests 함수를 썼을 때 403 오류가 발생하는 걸 user agent로 막을 수 있음 (우리가 크롬이나 익스플로워에서 접속하는 것처럼 꾸며주는거임)

import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

res = requests.get(url, headers=headers) #페이지에 접속할 때 정의한 유저 에이전트 값을 넘겨줌
res.raise_for_status()

with open ("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)

