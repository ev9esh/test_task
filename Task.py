from bs4 import BeautifulSoup as bs
import requests
import json

# URL = 'https://www.oriencoop.cl/sucursales.htm'
# r = requests.get(URL)
# src = r.text

# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(src)

# with open('index.html', 'r') as file:
#     src = file.read()
#
# soup = bs(src, 'lxml')
# all_href = soup.find('ul', class_='c-list c-accordion').find_all('ul')
#
# dict_all_href = {}
# for i in all_href:
#     find_li = i('li')
#     for item in find_li:
#         find_a = item('a')
#         for href in find_a:
#             text = href.text
#             all_href = 'https://www.oriencoop.cl' + href.get('href')
#             # print(f'{text}:{all_href}')
#             dict_all_href[text] = all_href
#
# with open('dict_all_href.json', 'w') as file:
#     json.dump(dict_all_href, file, indent=4, ensure_ascii=False)

with open('dict_all_href.json', 'r') as file:
    all_href = json.load(file)

for category_name, category_href in all_href.items():
    # r = requests.get(url=category_href)
    # src = r.text
    #
    # with open(f'data/{category_name}.html', 'w', encoding='utf-8') as file:
    #     file.write(src)

    with open(f'data/{category_name}.html') as file:
        src = file.read()

    soup = bs(src, 'lxml')

    res_dict = {
        'address': soup.find_all('span')[5].text,
        'name': soup.find('div', class_='c-title').find('h2').text,
        'phones': soup.find_all('span')[6].text,
        'working_hours': [soup.find_all('span')[9].text, soup.find_all('span')[8].text],
    }

    with open('result.json', 'a') as file:
        json.dump(res_dict, file, indent=4, ensure_ascii=False)
