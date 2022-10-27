from bs4 import BeautifulSoup as bs
import requests
import json


# URL = 'https://www.oriencoop.cl/sucursales.htm'
# r = requests.get(URL)
# src = r.text

# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(src)

with open('index.html', 'r') as file:
    src = file.read()

soup = bs(src, 'lxml')
all_href = soup.find('ul', class_='c-list c-accordion').find_all('ul')

dict_all_href = {}
for i in all_href:
    find_li = i('li')
    for item in find_li:
        find_a = item('a')
        for href in find_a:
            text = href.text
            all_href = 'https://www.oriencoop.cl' + href.get('href')
            # print(f'{text}:{all_href}')
            dict_all_href[text] = all_href

with open('dict_all_href.json', 'w') as file:
    json.dump(dict_all_href, file, indent=4, ensure_ascii=False)















