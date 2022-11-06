import requests
import lxml 
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/American_football"
page = requests.get(url)

soup = BeautifulSoup(page.content,'lxml')

urls = []
for link in soup.find_all('a'):
    print(link.get('href'))