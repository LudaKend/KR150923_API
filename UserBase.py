import json
from GeneralBase import GeneralBase


class UserBase(GeneralBase):
    '''класс для работы с вакансиями согласно предпочтениям пользователя'''
    def __init__(self, list_base):
        self.list_base = list_base

    def take_only_big(self, user_salary):
        '''метод, чтобы выбрать вакансии с минимальной оплатой >= указанной пользователем суммы'''
        user_list_base = []
        for item in self.list_base:
            item_salary = item.give_away_salary_min()
            #print(f'item_salary равно {item_salary}')
            if item_salary >= user_salary:
                user_list_base.append(item)
        #print(user_list_base)
        return user_list_base

    def print_user_list(self, user_list_base):
        '''метод для печати вакансий из списка user_list_base, выбранных пользователем'''
        for item in user_list_base:
            print(item)

    def take_non_zero(self):
        '''метод, чтобы выбрать вакансии с ненулевой оплатой'''
        user_list_base = []
        for item in self.list_base:
            item_salary = item.give_away_salary_min()
            #print(f'item_salary равно {item_salary}')
            if item_salary != 0 or item.give_away_salary_max() != 0:
                user_list_base.append(item)
        #print(user_list_base)
        return user_list_base

    def sort_min_salary(self):
        '''сортировать по возврастанию МИНИМАЛЬНОГО РАЗМЕРА ОПЛАТЫ'''
        return sorted(self.list_base,key=lambda x: x.give_away_salary_min())

    def sort_max_salary(self):
        '''сортировать по возврастанию МАКСИМАЛЬНОГО РАЗМЕРА ОПЛАТЫ'''
        return sorted(self.list_base,key=lambda x: x.give_away_salary_max())

    def find_word(self, user_word_lower):
        '''ищем заданное слово в названиии (name) и в требованиях (requirement) к вакансии'''
        user_list_base = []
        for item in self.list_base:
            item_name = item.give_away_name()
            if user_word_lower in item_name:
                user_list_base.append(item)
            else:
                item_requirement = item.give_away_requirement()
                if user_word_lower in item_requirement:
                    user_list_base.append(item)
        #print(user_list_base)
        return user_list_base

    def to_json(self, user_name, resourse, list_user_base):
        '''Запиываем вакансии, выбранные пользователем, в персональный пользовательский файл в формате JSON'''
        resourse = str(resourse)
        file_name = '_'.join((user_name, resourse))
        # data = [self.id_item, self.name, self.salary, self.url, self.requirement, self.responsibility]
        data = []
        for vacancy in list_user_base:
            vacancy_id_item = vacancy.give_away_id_item()
            vacancy_name = vacancy.give_away_name()
            vacancy_salary_min = vacancy.give_away_salary_min()
            vacancy_salary_max = vacancy.give_away_salary_max()
            vacancy_url = vacancy.give_away_url()
            vacancy_requirement = vacancy.give_away_requirement()
            temp_dict = {'id_item':vacancy_id_item, 'name':vacancy_name, 'salary_min':vacancy_salary_min,
                         'salary_max':vacancy_salary_max, 'url':vacancy_url, 'requirement':vacancy_requirement}
            data.append(temp_dict)
        #print(data)
        with open(file_name, 'w') as f:
            json.dump(data, f)
