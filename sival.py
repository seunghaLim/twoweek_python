import requests
from bs4 import BeautifulSoup 
from selenium import webdriver


url = "https://www.youtube.com/watch?v=YazigoBQBKE"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

comments = soup.find("div", attrs={"id" : "comment-chip-container"})
print(comments)
comments = comments.find("yt-formatted-string", attrs ={"class" : "style-scope ytd-comment-renderer"})
print(comments)