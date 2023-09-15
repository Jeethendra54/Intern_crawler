from bs4 import BeautifulSoup
import requests


def intern_page_limit(url): 
    pagination_text = requests.get(url).text 
    soup = BeautifulSoup(pagination_text, 'lxml')
    total_pages = soup.find('span' , id='total_pages' )
    total_pages = str(total_pages.text)
    int_total_pages = int(total_pages)
    return int_total_pages 

