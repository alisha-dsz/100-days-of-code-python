import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movie_website = response.text


soup = BeautifulSoup(movie_website, "html.parser")

titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
reversed_title_list = titles[::-1]

with open("movie.txt","w", encoding='utf-8') as file:
    for movie in reversed_title_list:
        file.write(f"{movie}\n")