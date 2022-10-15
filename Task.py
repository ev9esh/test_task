from bs4 import BeautifulSoup as bs
import requests
import json
import io


URL = 'https://www.oriencoop.cl/sucursales.htm'

res_list = {}
res_list['data'] = []
r = requests.get(URL)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL2 = 'https://www.oriencoop.cl/sucursales/127'
r = requests.get(URL2)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL3 = 'https://www.oriencoop.cl/sucursales/165'
r = requests.get(URL3)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL4 = 'https://www.oriencoop.cl/sucursales/167'
r = requests.get(URL4)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL5 = 'https://www.oriencoop.cl/sucursales/170'
r = requests.get(URL5)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL6 = 'https://www.oriencoop.cl/sucursales/173'
r = requests.get(URL6)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL7 = 'https://www.oriencoop.cl/sucursales/180'
r = requests.get(URL7)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL8 = 'https://www.oriencoop.cl/sucursales/182'
r = requests.get(URL8)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL9 = 'https://www.oriencoop.cl/sucursales/184'
r = requests.get(URL9)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL10 = 'https://www.oriencoop.cl/sucursales/187'
r = requests.get(URL10)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL11 = 'https://www.oriencoop.cl/sucursales/188'
r = requests.get(URL11)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL12 = 'https://www.oriencoop.cl/sucursales/194'
r = requests.get(URL12)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL13 = 'https://www.oriencoop.cl/sucursales/196'
r = requests.get(URL13)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL14 = 'https://www.oriencoop.cl/sucursales/208'
r = requests.get(URL14)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL15 = 'https://www.oriencoop.cl/sucursales/219'
r = requests.get(URL15)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL16 = 'https://www.oriencoop.cl/sucursales/231'
r = requests.get(URL16)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL17 = 'https://www.oriencoop.cl/sucursales/267'
r = requests.get(URL17)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

URL18 = 'https://www.oriencoop.cl/sucursales/312'
r = requests.get(URL18)
soup = bs(r.text, 'html.parser')
res_list['data'].append({'address': soup.find_all('span')[5].text,
                         'name': soup.find_all('span')[4].text,
                         'phones': soup.find_all('span')[6].text,
                         'working_hours': soup.find_all('span')[9].text})

# print(res_list)

with io.open('test.txt', 'w', encoding='utf-8') as file:
    s = json.dumps(res_list, ensure_ascii=False, indent=4)
    file.write(s)
