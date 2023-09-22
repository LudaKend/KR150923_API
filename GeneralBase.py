import json

class GeneralBase:
    '''класс для работы с данными о вакансиях'''
    #name_array = 'vacancies'  #посмотрим, что приоритетней - эта переменная в классе или параметр, с которым буду вызывать метод from_json из main!!!

    # def __init__(self, id, name, salary, url, requirement, responsibility):
    #     self.id = id
    #     self.name = name
    #     self.salary = salary
    #     self.url = url
    #     self.requirement = requirement
    #     self.responsibility = responsibility
    all = []

    @classmethod
    def from_json(cls, name_array='no_vacancies'):
        '''Чтение данных из JSON-файла'''
        if name_array == 'no_vacancies':
            raise 'файлы с вакансиями не получены'
        else:
            with open(name_array, encoding='cp1251') as f:
                print(json.load(f))
                data_file = json.load(f)

                for line in data_file:
                    cls.id = line[0]
                    cls.name = line[1]
                    item = (cls.id, cls.name)
                    cls.all.append(item)



