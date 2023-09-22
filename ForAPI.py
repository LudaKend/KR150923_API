from abc import ABC, abstractmethod
import requests
import json
import os

class ForAPI(ABC):
    '''абстрактный класс для API'''
    pass

class ForAPI_hh(ForAPI):
    '''класс для API с сайта hh.ru'''
    name_array = 'vacancies_hh'
    def __init__(self, url_site='https://api.hh.ru/vacancies/'):
        self.url_site = url_site
        self.list_vacancies = []
        # self.id = self.make_requests()
        # self.name = self.make_requests()
        # self.salary = self.make_requests()
        # self.url = self.make_requests()
        # self.requirement = self.make_requests()
        # self.responsibility = self.make_requests()

    def make_requests(self):
        '''выполняем API запрос к сайту hh.ru, полученную информацию раскладываем в экземпляры класса'''
        self.responce = requests.get(self.url_site)
        print(self.responce.status_code)
        #print(self.responce.text)
        all_vacancies = json.loads(self.responce.text)
        #print(all_vacancies)
        self.list_vacancies = []
        for vacancy in all_vacancies['items']:
            # print()
            # print(vacancy)
            temp_dict = vacancy
            # print(temp_dict)
            self.id = temp_dict['id']
            self.name = temp_dict['name']
            self.salary = temp_dict['salary']
            self.url = temp_dict['url']
            self.requirement = temp_dict['snippet']['requirement']
            self.responsibility = temp_dict['snippet']['responsibility']
            # print()
            # print(self.responsibility)


    def to_json(self):
        '''Запись данных, полученных по API, в файл в формате JSON'''
        data = [self.id, self.name, self.salary, self.url, self.requirement, self.responsibility]
        with open(self.name_array, 'w') as f:
            json.dump(data, f)

class ForAPI_superjob(ForAPI):
    '''класс для API с сайта superjob.ru'''
    api_key = os.getenv('API_KEY_superjob')
    name_array = 'vacancies_superjob'

    def __init__(self, url_site ='https://api.superjob.ru/2.0/vacancies/?t=4&count=10'):
        self.url_site = url_site
        self.list_vacancies = []

    def make_requests(self):
        '''выполняем API запрос к сайту superjob.ru, полученную информацию раскладываем в экземпляры класса'''
        self.responce = requests.get(self.url_site, headers={'X-Api-App-Id': self.api_key})
        print(self.responce.status_code)
        print(self.responce.text)
        all_vacancies = json.loads(self.responce.text)
        # print(all_vacancies)
        self.list_vacancies = []
        for vacancy in all_vacancies['objects']:
            print()
            print(vacancy)
            temp_dict = vacancy
            # print(temp_dict)
            self.id = temp_dict['id']
            self.name = temp_dict['profession']
            self.payment_from = temp_dict['payment_from']
            self.payment_to = temp_dict['payment_to']
            self.url = temp_dict['client']['link']
            self.requirement = temp_dict['candidat']
            # self.requirement = temp_dict['snippet']['requirement']
            # self.responsibility = temp_dict['snippet']['responsibility']
            # print()
            print(self.requirement)

    def to_json(self):
        '''Запись данных, полученных по API, в файл в формате JSON'''
        data = [self.id, self.name, self.payment_from, self.payment_to, self.url, self.requirement] #, self.responsibility]
        with open(self.name_array, 'w') as f:
            json.dump(data, f)
