from bs4 import BeautifulSoup
import requests

html_request = requests.get('')

with open('index.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    
    course_mate = soup.find_all('div', class_ = 'item-info')
    
    # print(course_mate)
    
    for course in course_mate:
        
        courseH4 = course.text.split()[-1]
        print(f'I Just Love a well prepared {courseH4}')