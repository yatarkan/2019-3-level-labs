import requests
from bs4 import BeautifulSoup

page_url = 'https://lenta.ru/rubrics/sportasdasd'

lenta_sport_request = requests.get(page_url)

lenta_sport_content = lenta_sport_request.text

if lenta_sport_request.status_code == 200:
    print('Yay! We performed a successful request!')
else:
    print('Oops.. Something went wrong')

parsed_page = BeautifulSoup(lenta_sport_content)

print(type(parsed_page))

print(parsed_page.title.text)

#root > section.b-section.b-layout.js-layout.b-layout_rubric > div > div > div.span8.js-rubric__content > div.row.js-content > div:nth-child(1) > section