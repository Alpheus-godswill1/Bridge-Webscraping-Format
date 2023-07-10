from bs4 import BeautifulSoup
import lxml

with open('index.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    
    Tags = soup.find_all('div', 'item-info')
    
    for particularTags in Tags:
        print(particularTags.text)
    