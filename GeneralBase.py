import json
RATE_EUR = 100
RATE_USD = 90

class GeneralBase:
    '''класс для работы с данными о вакансиях'''
    #name_array = 'vacancies'  #посмотрим, что приоритетней - эта переменная в классе или параметр, с которым буду вызывать метод from_json из main!!!
    all = []
    #name_array = 'all_vacancies'
    name_array = 'vacancies_hh'

    def __init__(self, id_item, name, salary_from, salary_to, currency, gross, url, requirement): # responsibility):
        self.id_item = id_item
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.gross = gross
        self.url = url
        self.requirement = requirement
        #self.responsibility = responsibility
        self.salary_min = self.find_salary_relevant(salary_from)
        self.salary_max = self.find_salary_relevant(salary_to)

    @classmethod
    def from_json(cls, name_array='no_vacancies'):
        '''Чтение данных из JSON-файла'''
        if name_array == 'no_vacancies':
            raise 'файлы с вакансиями не получены'
        else:
            with open(name_array) as f:  #encoding='cp1251'
                #print(json.load(f))
                cls.data_file = json.load(f)
            #print(cls.data_file)
            return cls.data_file

    @classmethod
    def instantiate_from_json(cls, name_array):
        cls.data_file = cls.from_json(name_array)
        for _dict in cls.data_file:
            base = GeneralBase(_dict['id'], _dict['name'], _dict['salary_from'], _dict['salary_to'],
                               _dict['currency'], _dict['gross'], _dict['url'],_dict['requirement']) #, _dict['responsibility'])
            print()
            print('Проверяем экземпляры')
            print(base.__dict__)

    def validate_id_item(self):
        '''проверяем id вакансии'''
        if type(self.id_item) == 'int':
            return True

    def validate_name(self):
        '''проверяем name вакансии'''
        if type(self.name) == 'str' and self.name != '':
            return True

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
        temp_salary = self.recount_salary(salary)  #пересчитываем в рубли
        relevant_salary = self.count_salary_without_tax(temp_salary)
        return relevant_salary

    def validate_url(self):
        '''проверяем корректность url вакансии '''
        if self.url[0:len(URL_SITE_HH)] == URL_SITE_HH:
            return True

    def to_json(self):
        '''Запись данных в файл в формате JSON'''
        data = [self.id_item, self.name, self.salary, self.url, self.requirement, self.responsibility]
        with open(self.name_array, 'a') as f:
            json.dump(data, f)
