from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, "html.parser")
titles = soup.find(name="tr", class_="athing submission")
print(titles)







# from bs4 import BeautifulSoup
# # import lxml

# with open("./Day 45/bs4-start/website.html", mode="r") as file:
#     content = file.read()

# soup = BeautifulSoup(content, 'html.parser') # if html.parser doesn't work you might try: lxml

# # print(soup.title)    --> examples
# # print(soup.title.string)    --> examples

# # print(soup.prettify())    # --> makes indentations

# all_anchor_tags = soup.find_all(name="a")  #  --> finds all links in my html file
# # print(all_anchor_tags)

# for x in all_anchor_tags:
#     # print(x.getText())  --> get the Text to all the links
#     # print(x.get("href"))  --> gets all the links in my html file
#     pass

# heading = soup.find(name="h1", id="name")
# # print(heading)
# section_heading = soup.find(name="h3", class_="heading")  #  --> class keyword in python is only for declarating classes
# print(section_heading)

# company_url = soup.select_one(selector="p a")