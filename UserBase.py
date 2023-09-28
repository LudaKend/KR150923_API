import json
from GeneralBase import GeneralBase
RATE_EUR = 100
RATE_USD = 90

class UserBase(GeneralBase):
    '''класс для работы с вакансиями согласно предпочтениям пользователя'''
    #name_array = 'all_vacancies'
    name_array = 'vacancies_hh'

    def __init__(self, list_base): #, user_name, resourse):
        self.list_base = list_base

    def take_only_big(self, user_salary):
        '''метод, чтобы выбрать вакансии с минимальной оплатой >= указанной пользователем суммы'''
        user_list_base = []
        for item in self.list_base:
            item_salary = item.give_away_salary_min()
            #print(f'item_salary равно {item_salary}')
            if item_salary >= user_salary:
                user_list_base.append(item)
        print(user_list_base)
        return user_list_base

    def print_user_list(self, user_list_base):
        '''метод для печати вакансий из списка user_list_base, выбранных пользователем'''
        for item in user_list_base:
            print(item)

    def take_non_zero(self):
        '''метод, чтобы выбрать вакансии с минимальной оплатой >= указанной пользователем суммы'''
        user_list_base = []
        for item in self.list_base:
            item_salary = item.give_away_salary_min()
            #print(f'item_salary равно {item_salary}')
            if item_salary != 0 or item.give_away_salary_max() != 0:
                user_list_base.append(item)
        print(user_list_base)
        return user_list_base

    def sort_min_salary(self):
        '''сортировать по возврастанию МИНИМАЛЬНОГО РАЗМЕРА ОПЛАТЫ'''
        return sorted(self.list_base,key=lambda x: x.give_away_salary_min())

    def sort_max_salary(self):
        '''сортировать по возврастанию МАКСИМАЛЬНОГО РАЗМЕРА ОПЛАТЫ'''
        return sorted(self.list_base,key=lambda x: x.give_away_salary_max())

    @classmethod
    def instantiate_from_json(cls, name_array):
        '''формируем экземпляры класса из данных json-файла'''
        cls.data_file = cls.from_json(name_array)
        for _dict in cls.data_file:
            base = GeneralBase(_dict['id'], _dict['name'], _dict['salary_from'], _dict['salary_to'],
                               _dict['currency'], _dict['gross'], _dict['url'],_dict['requirement'])
            print()
            print('Проверяем экземпляры')
            print(base.__dict__)

    @classmethod
    def from_json(cls, name_array='no_vacancies'):
        '''Чтение данных из JSON-файла'''
        if name_array == 'no_vacancies':
            raise 'файлы с вакансиями не получены'
        else:
            with open(name_array) as f:  # encoding='cp1251'
                # print(json.load(f))
                cls.data_file = json.load(f)
            # print(cls.data_file)
            return cls.data_file

    # def to_json(self):
    #     '''Запись данных в файл в формате JSON'''
    #     data = [self.id_item, self.name, self.salary, self.url, self.requirement, self.responsibility]
    #     with open(self.name_array, 'a') as f:
    #         json.dump(data, f)

    # def write_user_name(self, user_name):
    #     self.user_name = user_name
    #     return self.user_name

    # def write_sourse(self, sourse):
    #     self.sourse = sourse
    #     return self.sourse
