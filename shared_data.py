import re
from bs4 import BeautifulSoup
import requests


def intern_count(url):
    url_text = requests.get(url).text
    soup = BeautifulSoup(url_text, 'lxml')
    total = soup.find('div', class_='heading heading_4_6').text
    integer_part = re.findall(r'\d+', total)[0]
    total_count = int(integer_part)
    return total_count

