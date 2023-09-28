# import requests
# from ForAPI import ForAPI_hh
# from ForAPI import ForAPI_superjob
# from GeneralBase import GeneralBase
from utils import make_start_base

URL_SITE_HH = 'https://api.hh.ru/vacancies/'
URL_SITE_SUPERJOB = 'https://api.superjob.ru/2.0/vacancies/?t=4&count=10'
#print(len(URL_SITE_HH))

if __name__ == '__main__':
    # site_hh = ForAPI_hh(URL_SITE_HH)  #создаем экземпляр класса
    # site_hh.make_requests()           #запрашиваем информацию
    # site_hh.make_list_vacancies()     #формируем список вакансий
    # site_hh.to_json()                 #записываем в файл


    # site_superjob = ForAPI_superjob(URL_SITE_SUPERJOB)
    # site_superjob.make_requests()
    # site_superjob.make_list_vacancies()
    # site_superjob.to_json()
    # print()
    # print()
    # GeneralBase.instantiate_from_json('vacancies_hh') # создаём экземпляры класса из данных файла
    # GeneralBase.instantiate_from_json('vacancies_superjob')  # создаём экземпляры класса из данных файла
    print("Привет! Введи пожалуйста свое имя:")
    user_name = input()
    #UserBase.write_user_name(user_name)
    print('Сделай выбор - на каком ресурсе будем искать вакансии:')
    print(' 1 - hh.ru \n 2 - superjob.ru \n 3 - hh.ru и superjob.ru \n 0 - на других ресурсах')
    resourse = int(input())  # sourse = источник
    #UserBase.write_sourse(sourse)

    make_start_base(user_name,resourse)

