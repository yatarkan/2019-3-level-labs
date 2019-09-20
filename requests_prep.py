# Practice 1

import requests
from bs4 import BeautifulSoup

url = 'https://lenta.ru/rubrics/sport'

lenta_sport_request = requests.get(url)

lenta_sport_content = lenta_sport_request.text

parsed_page = BeautifulSoup(lenta_sport_content)

print(parsed_page.find_all('h3'))