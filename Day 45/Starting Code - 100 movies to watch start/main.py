import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL, verify=False)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = soup.find_all(name="h3", class_="title")
empty_list = []
for x in titles:
    empty_list.append(x.text.strip())

empty_list.reverse()

with open("example.txt", "w", encoding="utf-8") as txt_file:
    for index, y in enumerate(empty_list, start=1):
        txt_file.write(f"{y}\n")