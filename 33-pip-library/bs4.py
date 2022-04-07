# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)

soup = BeautifulSoup(r.text, 'html.parser')
# yangiliklar mavzusini ajratib olamiz
news = soup.find_all(class_="news-title")
# eng birinchi yangiliklarni konsolga chiqaramiz
print(news[0].text)






