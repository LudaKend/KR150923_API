import requests
from ForAPI import ForAPI_hh
from ForAPI import ForAPI_superjob
from GeneralBase import GeneralBase

if __name__ == '__main__':
    site_hh = ForAPI_hh()
    site_hh.make_requests()
    site_hh.to_json()
    #
    # site_superjob = ForAPI_superjob()
    # site_superjob.make_requests()
    # site_superjob.to_json()

    # base = GeneralBase()
    # base.from_json('vacancies_hh')
    # base.from_json('vacancies_superjob')
