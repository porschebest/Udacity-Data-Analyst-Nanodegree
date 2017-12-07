from bs4 import BeautifulSoup
import requests
response = requests.get('https://en.wikipedia.org/')

html = response.text

soup = BeautifulSoup(html, 'html.parser')
print(soup.title)
print(soup.p)
print(soup.p.a)
