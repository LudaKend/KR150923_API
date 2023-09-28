import json
RATE_EUR = 100
RATE_USD = 90

class GeneralBase:
    '''класс для работы с данными о вакансиях'''
    #name_array = 'all_vacancies'
    name_array = 'vacancies_hh'  #???

    def __init__(self, id_item, name, salary_from, salary_to, currency, gross, url, requirement):
        self.id_item = id_item
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.gross = gross
        self.url = url
        self.requirement = requirement

        self.salary_min = self.find_salary_relevant(salary_from)
        self.salary_max = self.find_salary_relevant(salary_to)

    def __str__(self):
        return (f'ОПИСАНИЕ ВАКАНСИИ:\n {self.name}\n ТРЕБОВАНИЯ:\n {self.requirement}\n МИНИМАЛЬНЫЙ РАЗМЕР ОПЛАТЫ:'
                f' {self.salary_min}\n МАКСИМАЛЬНЫЙ РАЗМЕР ОПЛАТЫ: {self.salary_max}')

    def give_away_salary_min(self):
        return self.salary_min

    def give_away_salary_max(self):
        return self.salary_max

    @classmethod
    def instantiate_from_json(cls, name_array):
        cls.data_file = cls.from_json(name_array)
        cls.list_base = []
        for _dict in cls.data_file:
            base = GeneralBase(_dict['id'], _dict['name'], _dict['salary_from'], _dict['salary_to'],
                               _dict['currency'], _dict['gross'], _dict['url'],_dict['requirement'])
            print()
            # print('Проверяем экземпляры')
            print(base.__dict__)
            print(base)  #красивый вывод для пользователя с использованием метода __str__
            cls.list_base.append(base)  #формирую список экземпляров
        #print(cls.list_base)
        return cls.list_base

    @classmethod
    def from_json(cls, name_array='no_vacancies'):
        '''Чтение данных из JSON-файла'''
        if name_array == 'no_vacancies':
            raise 'файлы с вакансиями не получены'
        else:
            with open(name_array) as f:  # encoding='cp1251'
                # print(json.load(f))
                cls.data_file = json.load(f)
                #print(cls.data_file)
            return cls.data_file


    def recount_salary(self,salary):
        '''переводим зарплату в рублевый эквивалент'''
        if self.currency == 'RUR' or self.currency == 'rub':
            return salary
        elif self.currency == 'EUR':
            return salary * RATE_EUR
        elif self.currency == 'USD':
            return salary * RATE_USD
        else:
            salary = 0
            return salary

    def count_salary_without_tax(self, salary):
        '''определяем размер зарплаты без налогов'''
        if self.gross == True:
            return 0.87 * salary
        else:
            return salary

    def find_salary_relevant(self, salary):
        '''определяем значения релевантные для сравнения'''
        if salary == None:
            salary = 0

        temp_salary = self.recount_salary(salary)  #пересчитываем в рубли
        relevant_salary = self.count_salary_without_tax(temp_salary)
        return relevant_salary

    def validate_url(self):
        '''проверяем корректность url вакансии '''
        if self.url[0:len(URL_SITE_HH)] == URL_SITE_HH:
            return True

    def to_json(self):
        '''Запись данных в файл в формате JSON'''
        data = [self.id_item, self.name, self.salary, self.url, self.requirement]
        with open(self.name_array, 'a') as f:
            json.dump(data, f)
