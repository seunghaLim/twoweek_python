import requests
from bs4 import BeautifulSoup
from requests.models import default_hooks 

def create_soup(url):

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
 
    soup = BeautifulSoup(res.text, "lxml")

    return soup

def scrape_weather():
    print("[오늘의 날씨]")

    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8&tqi=hdgoQdp0JywssZNQUYKssssste8-466116"

    soup = create_soup(url)

    today_w = soup.find("p", attrs={"class" : "cast_txt"}).get_text()
    
    pre_t = soup.find("p", attrs = {"class" : "info_temperature"}).get_text().replace("도씨", "")       #도씨 글자 공백으로 바꾸기(도씨 글자 없애기)
    min_t = soup.find("span", attrs = {"class" : "min"}).get_text().strip()     #개행문자 제거
    max_t = soup.find("span", attrs = {"class" : "max"}).get_text().strip()     #개행문자 제거

    mornig_rain = soup.find("span", attrs = {"class" : "point_time morning"}).get_text()
    afternoon_rain = soup.find("span", attrs = {"class" : "point_time afternoon"}).get_text()

    dust_info = soup.find("dl", attrs = {"class" : "indicator"})
    dust = soup.find_all("dd", attrs = {"class" : "lv2"})[0].get_text()
    m_dust = soup.find_all("dd", attrs = {"class" : "lv2"})[1].get_text()

    print(today_w)
    print("현재 {0} (최저 : {1} / 최고 : {2})".format(pre_t, min_t, max_t))
    print("오전 {0} / 오후 {1}".format(mornig_rain, afternoon_rain))
    print()
    print("미세먼지 {}".format(dust))
    print("초미세먼지 {}".format(m_dust))

def scrape_headline():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/"
    soup = create_soup(url)  

    headlines = soup.find("ul", {"class" : "hdline_article_list"}).find_all("li", limit=3)  #find_all에 limit 변수를 넘겨주면 가져오는 개수에 제한을 둘 수 있음

    for idx, headline in enumerate(headlines):
        title = headline.find("a").get_text().strip()
        link =  "https://news.naver.com" + headline.find("a")["href"]

        print("{0}. {1}".format(idx+1, title))
        print("링크 : {}".format(link))
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)  

    news = soup.find("ul", attrs = {"class" : "type06_headline"}).find_all("li", limit = 3)

    for idx, new in enumerate(news):

        a_tag = 0
        img = new.find("img")
        if img :
            a_tag = 1
        title = new.find_all("a")[a_tag].get_text().strip()
        link = new.find_all("a")[a_tag]["href"]
        
        print("{0}. {1}".format(idx+1, title))
        print("링크 : {}".format(link))
    print()

def scrape_today_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english#;"
    soup = create_soup(url)  
    
    kor = soup.find_all("div", {"class" : "conv_txt"})[0].find_all("div")   #div태그이고 class속성이 conv_txt인 모든 요소들을 찾은 다음에, 그 중 첫번째 요소에서 div태그를 전부 찾음
    eng = soup.find_all("div", {"class" : "conv_txt"})[1].find_all("div")   #div태그이고 class속성이 conv_txt인 모든 요소들을 찾은 다음에, 그 중 두번째 요소에서 div태그를 전부 찾음


    print("(영어지문)")
    for lines in eng:
        print(lines.get_text().strip())     #lines 안에 있는 모든 div 태그를 for문으로 돌아가면서 하나씩 텍스트를 따옴
    print()

    print("(한글지문)")
    for lines in kor:
        print(lines.get_text().strip())     
    print()


if __name__ == "__main__":
    #scrape_weather()        #이 창에서 가동할 때만 함수 실행
    #scrape_headline()
    #scrape_it_news()
    scrape_today_english()

