from bs4 import BeautifulSoup
import requests
import re

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, "html.parser")
top_100 = soup.find_all(name="h3", class_="title")
titles = [title.getText() for title in top_100]
titles = titles[-1::-1]

with open("movies.txt", "w") as file:
    file.write("\n".join(titles))

