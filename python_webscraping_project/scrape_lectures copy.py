import requests
from bs4 import BeautifulSoup

url = "https://mediacom.korea.ac.kr/mediacom/faculty/subject.do"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("div", attrs={"class" : "t_list scrollbox"}).find("tbody").find_all("tr")

training_L = []
theory_L = []

for row in data_rows:
    column = row.find_all("td") 

    if len(column) != 14:
        continue

    title =  column[2].get_text().strip()
    data = column[5].get_text().strip()

    if data == '2' or data == '4':        
        training_L.append(title)
    
    else:
        theory_L.append(title)

print("<실습 과목 목록>")
for lec in training_L:
    print(lec)
print()

print("<이론 과목 목록>")
for lec in theory_L:
    print(lec)


