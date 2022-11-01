import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
site_HTML = response.text

soup = BeautifulSoup(site_HTML, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
titles_text = []

for title in all_movies:
    titles_text.insert(0, title.getText())

with open("movies.txt", mode="w") as file:
    for movie in titles_text:
        file.write(f"{movie}\n")
