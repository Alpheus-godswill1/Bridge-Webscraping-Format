from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.jumia.com.ng/men-sneakers/adidas/#catalog-listing'
html_file = requests.get(url).text
soup = BeautifulSoup(html_file, 'lxml')
Adidas = soup.find('div', class_ = '-paxs row _no-g _4cl-3cm-shs').text.replace(' ', '\n')
Href = soup.find('a', class_ ='core').text.replace(' ', '\n')
image = soup.find('div', 'img-c').text.replace(' ', '\n')
official_store = soup.find('div','bdg _mall _xs').text
Adidas_title = soup.find('h3','name').text


data = []

print(Adidas_title)
