import requests
import fake_useragent
from bs4 import BeautifulSoup
import soupsieve as ss

ua = fake_useragent.UserAgent()
headers = {"user-agent": ua.random}

""" Start program"""
city = {1: 'moskva/', 2: 'spb/', 3: 'ekaterinburg/', 4: 'perm/'}
start_var_1 = city[int(input('Выберите город (1-Москва, 2-Санкт-Петербург, 3-Екатеринбург, 4-Пермь): '))]

# diagnostika и словари узи можно соеденить
diagnostika = {1: 'uzi_shei', 2: 'uzi_bryushnoy', 3: 'uzi_taza', 4: 'uzi_polovoy'}
start_var_2 = diagnostika[int(input('Выберите область узи (1-УЗИ шеи, 2-УЗИ брюшной полости, 3-УЗИ малого таза, 4-УЗИ половой системы ): '))]

uzi_shei = {1: 'uzi-parashitovidnyh-zhelez/', 2: 'uzi-shitovidnoy-zhelezy/'}
uzi_bryushnoy = {1: 'uzi-zheludka/', 2: 'uzi-zhelchnogo-puzyrya/', 3: 'uzi-pecheni/', 4: 'uzi-pochek/', 5: 'uzi-vseh-organov/'}
uzi_taza = {1: 'uzi-mochevogo-puzyrya/', 2: 'uzi-mochevogo-puzyrya-s-opredeleniem-ostatochnoy-mochi/'}
uzi_polovoy = {1: 'uzi-matki-i-pridatkov/', 2: 'uzi-molochnyh-zhelez/', 3: 'uzi-moshonki/', 4: 'uzi-predstatelnoy-zhelezy/'}

vardiagnos = ''
if start_var_2 == 'uzi_shei':
    vardiagnos = uzi_shei[int(input("Выберите вид узи (1-паращитовидных желез, 2-щитовидной железы): "))]
elif start_var_2 == 'uzi_bryushnoy':
    vardiagnos = uzi_bryushnoy[int(input("Выберите вид узи (1-желудка, 2-желчного пузыря, 3-печени, 4-почек, 5-обзорное всех органов): "))]
elif start_var_2 == 'uzi_taza':
    vardiagnos = uzi_taza[int(input("Выберите вид узи (1-мочевого пузыря, 2-УЗИ мочевого пузыря с определением остаточной мочи): "))]
elif start_var_2 == 'uzi_polovoy':
    vardiagnos = uzi_polovoy[int(input("Выберите вид узи (1-матки и придатков, 2-молочных желез, 3-мошонки, 4-предстательной железы): "))]
""""""
url = 'https://prodoctorov.ru/' + start_var_1 + 'diagnostika/' + vardiagnos

def parsing(url):
    request = requests.get(url, headers=headers)
    pars = BeautifulSoup(request.text, 'lxml')

    urls_emerg = ss.select('div[data-filter-target="services_cards"] a[data-qa="service_card_lpu_name"]', pars)
    name_diagnostic = [i.get_text().strip('\n').strip(' ').rstrip('\n') for i in ss.select('span.b-card__price-list-service', pars)]
    price_diagnostic = [i.get_text().strip('\n                                ').strip(' ').rstrip('\n') for i in ss.select('span.b-card__price-list-price', pars)]

    total = {}
    for i in range(0,len(urls_emerg)):
        total[i] = urls_emerg[i].get_text().strip('\n').strip(' ').rstrip('\n'), name_diagnostic[i], price_diagnostic[i], 'https://prodoctorov.ru' + urls_emerg[i]['href']

    return total.values()
print(*parsing(url))

if input('Следующая страница? y/n = ') == 'y':
    print(*parsing(url+'?page=2'))
else:
    print('Спасибо за использование парсера')