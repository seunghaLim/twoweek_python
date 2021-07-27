import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#방법 1
# print(soup.title)
# print(soup.title.get_text())        #텍스트만 빼옴

# print(soup.a)       #soup 객체에서 첫번째로 발견되는 a태그에 관한 정보 출력
# #<a href="#menu" onclick="document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"><span>메인 메뉴로 바로가기</span></a>

# print(soup.a.attrs)     #a 엘리먼트의 의 속성(attribute) 정보 출력
# #{'href': '#menu', 'onclick': "document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"}

# print(soup.a["href"])   #a 엘리먼트의 속성 중에서도 href 속성값을 출력
# # #menu

#방법 2
# print(soup.find("a", attrs={"class": "Nbtn_upload"}))   #soup 객체에서 첫번째로 발견되는 a태그이면서, 클래스의 속성이 "Nbtn_upload"인 애들을 찾아줌
# #class=Nbtn_upload인 a 엘리먼트를 찾음
# # <a class="Nbtn_upload" href="/mypage/myActivity" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>
# print(soup.find(attrs={"class": "Nbtn_upload"}))    #class=Nbtn_upload인 엘리먼트를 찾음

#print(soup.find("li", attrs={"class": "rank01"}))      #class=rank01인 li 태그 엘리먼트를 찾음
'''
<li class="rank01">
<a href="/webtoon/detail?titleId=703846&amp;no=172" onclick="nclk_v2(event,'rnk*p.cont','703846','1')" title="여신강림-167화">여신강림-167화</a>
<span class="rankBox">
<img alt="변동없음" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_no.gif" title="변동없음" width="7"/> 0  


                                </span>
</li>
'''

rank1 = soup.find("li", attrs={"class": "rank01"})
#print(rank1.a)     #rank1에서 태그가 a인 것만 골라옴
#<a href="/webtoon/detail?titleId=703846&amp;no=172" onclick="nclk_v2(event,'rnk*p.cont','703846','1')" title="여신강림-167화">여신강림-167화</a>

# rank2 = rank1.next_sibling.next_sibling     #형제 관계의 다음 엘리먼트 가져옴. 개행문자가 없으면 한 번, 있으면 두 번 적어줘야됨
# print(rank2)

# rank1 = rank2.previous_sibling.previous_sibling     #형제 관계의 이전 엘리먼트 가져옴
# print(rank1)


#print(rank1.parent)     #부모 관계의 엘리먼트를 가져옴

# rank2 = rank1.find_next_sibling("li")       #함수로 다음 형제 엘리먼트인데 태그가 li인 것을 찾기
# print(rank2)        
# rank1 = rank2.find_previous_sibling("li")       #함수로 이전 형제 엘리먼트인데 태그가 li인 것을 찾기
# print(rank1)

print(rank1.find_next_siblings("li"))       #rank1 중 태그가 li인 형제 엘리먼트들만 골라옴

webtoon = soup.find("a", text = "중증외상센터 : 골든 아워-2부 10화 : 어찌 됐건")    
print(webtoon) #soup 중에서 a태그이면서 text가 중증외상센터 : 골든 아워-2부 10화 : 어찌 됐건 인 엘리먼트 출력
'''
<a href="/webtoon/detail?titleId=738174&amp;no=75" onclick="nclk_v2(event,'rnk*p.cont','738174','6')" title="중증외상센터 : 골든 아워-2부 10화 : 어찌 됐건">중증외
상센터 : 골든 아워-2부 10화 : 어찌 됐건</a>
'''