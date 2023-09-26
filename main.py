import requests
from ForAPI import ForAPI_hh
from ForAPI import ForAPI_superjob
from GeneralBase import GeneralBase

URL_SITE_HH = 'https://api.hh.ru/vacancies/'
URL_SITE_SUPERJOB = 'https://api.superjob.ru/2.0/vacancies/?t=4&count=10'
#print(len(URL_SITE_HH))

if __name__ == '__main__':
    # site_hh = ForAPI_hh(URL_SITE_HH)  #создаем экземпляр класса
    # site_hh.make_requests()           #запрашиваем информацию
    # site_hh.make_list_vacancies()     #формируем список вакансий
    # site_hh.to_json()                 #записываем в файл


    site_superjob = ForAPI_superjob(URL_SITE_SUPERJOB)
    site_superjob.make_requests()
    site_superjob.make_list_vacancies()
    site_superjob.to_json()
    print()
    print()
    GeneralBase.instantiate_from_json('vacancies_hh') # создаём экземпляры класса из данных файла
    GeneralBase.instantiate_from_json('vacancies_superjob')  # создаём экземпляры класса из данных файла

    #base.from_json('vacancies_hh')
    # base.from_json('vacancies_superjob')

    #base.to_json()
    #GeneralBase.to_json()
