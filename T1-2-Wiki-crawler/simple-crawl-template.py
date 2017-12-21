from bs4 import BeautifulSoup
import requests
response = requests.get('https://en.wikipedia.org/wiki/Ireland')

html = response.text

soup = BeautifulSoup(html, 'html.parser')

content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
for element in content_div.find_all("p", recursive=False):
    if element.find('a', recursive=False):
        first_relative_link = element.find('a', recursive=False).get('href')
        break
print(first_relative_link)
