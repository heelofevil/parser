import requests
import fake_useragent
from bs4 import BeautifulSoup
import soupsieve as ss

# ua = fake_useragent.UserAgent()
# headers = {"user-agent": ua.random}
#
# urls = 'https://prodoctorov.ru/perm/diagnostika/uzi-parashitovidnyh-zhelez/'
# pars = BeautifulSoup(requests.get(urls, headers=headers).text, 'lxml')

# urls_emerg = ss.select('div[data-filter-target="services_cards"] a[data-qa="service_card_lpu_name"]', pars)
# name_diagnostic = [i.get_text().strip('\n').strip(' ').rstrip('\n') for i in ss.select('span.b-card__price-list-service', pars)]
# price_diagnostic = [i.get_text().strip('\n                                ').strip(' ').rstrip('\n') for i in ss.select('span.b-card__price-list-price', pars)]
#
# total = {}
# for i in range(0,len(urls_emerg)):
#     total[i] = urls_emerg[i].get_text().strip('\n').strip(' '),name_diagnostic[i], price_diagnostic[i], 'https://prodoctorov.ru' + urls_emerg[i]['href']
#
# print(*total.values())

'''парс имя клиники'''
# name_list = [i.get_text().strip('\n').strip(' ').rstrip('\n') for i in ss.select('div[data-filter-target="services_cards"] a[data-qa="service_card_lpu_name"]', bs)]
# phone_list = [i.get_text().strip('\n').strip(' ').rstrip('\n') for i in ss.select('div[data-filter-target="services_cards"] div.mb-0 :last-child', bs)]
# time_list = [i.get_text().strip('\n                            \n                                ') for i in ss.select('div[data-filter-target="services_cards"] div[data-qa="service_card_schedule"]', bs)]
# adress_list = [i.get_text().strip('\n').strip(' ').rstrip('\n') for i in ss.select('div[data-filter-target="services_cards"] span[data-qa="service_card_address"]', bs)]

''' Парсинг: Название + ссылка на страницу больницы '''
# urls_emerg = ss.select('div[data-filter-target="services_cards"] a[data-qa="service_card_lpu_name"]', bs)
# for i in range(0,len(urls_emerg)):
#     print(urls_emerg[i].get_text().strip('\n').strip(' '), 'https://prodoctorov.ru' + urls_emerg[i]['href'])

city = {1: 'moskva/', 2: 'spb/', 3: 'ekaterinburg/', 4: 'perm/'}
start_var_1 = (input('Выберите город (1-Москва, 2-Санкт-Петербург, 3-Екатеринбург, 4-Пермь): '))
if start_var_1 not in ('1234'):
    while start_var_1 in ('1234'):
        print("Выберите в указанном даипозоне")
        start_var_1 = (input('Выберите город (1-Москва, 2-Санкт-Петербург, 3-Екатеринбург, 4-Пермь): '))
print(start_var_1)

