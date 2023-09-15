import re
from bs4 import BeautifulSoup
import requests 

# url = 'https://internshala.com/internships/front-end-development-internship/page-1/'
# tsp = 'https://internshala.com/internships/front-end-development-internship/page-1/'
# html_text = requests.get(url).text
# soup = BeautifulSoup(html_text, 'lxml')

# total = soup.find('div' , class_='heading heading_4_6').text 
# print(total) 

def intern_count(url):
    url_text = requests.get(url).text
    soup = BeautifulSoup(url_text, 'lxml')
    total = soup.find('div' , class_='heading heading_4_6').text
    integer_part = re.findall(r'\d+', total)[0]
    integer_part = re.findall(r'Total: (\d+)', total)
    # if integer_part:
    #     total_count = int(integer_part[0])
    # else:
    #      total_count = 0  # or handle it according to your logic
    integer_value = int(integer_part)
    return integer_value


