# #방법 1
# import requests

# res = requests.get("http://naver.com")

# print("응답코드 :", res.status_code)    #200이 출력이 되면 정상 403-접근 권한이 없음

# #웹 스크래핑을 할 수 있는지 없는지 검사
# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 발생했습니다. [에러코드 " + res.status_code + "]")

# #방법 2
# import requests

# res = requests.get("http://google.com")

# res.raise_for_status()  #웹스크리핑을 못하는 웹페이지일 경우 여기서 오류가 발생하고 그 밑에 코드는 실행되지 않음
# print("웹스크래핑을 실행합니다")

# print(len(res.text))
# print(res.text)


# with open ("mygoogle.html", "w", encoding="utf8") as f:
#     f.write(res.text)

