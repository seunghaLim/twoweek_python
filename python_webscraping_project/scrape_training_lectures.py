import requests
from bs4 import BeautifulSoup

url = "https://mediacom.korea.ac.kr/mediacom/faculty/subject.do"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("div", attrs={"class" : "t_list scrollbox"}).find("tbody").find_all("tr")

with open ("실습 과목 목록.txt", "w", encoding = "utf8") as f:

    f.write("<실습 과목 목록>\n")
    for row in data_rows:
        column = row.find_all("td") 

        if len(column) != 14:
            continue

        title =  column[2].get_text().strip()
        data = column[5].get_text().strip()

        if data == '2' or data == '4':
            link = "https://klue.kr/search?query=" + title        
            f.write(title)
            f.write("\n")
            f.write("강의 평가 링크 : {0}".format(link))
            f.write("\n")
            f.write("-"*75)
            f.write("\n")
    


