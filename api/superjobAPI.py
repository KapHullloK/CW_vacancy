from file_handlers.job_search_abc import JobABC
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_key')


class SuperJobAPI(JobABC):
    def __init__(self, search_params: dict):
        self.__headers = {'X-Api-App-Id': api_key}
        self.__search_params = search_params
        self.__request = requests.get("https://api.superjob.ru/2.0/vacancies/",
                                      headers=self.__headers, params=self.__search_params).json()
        self.__vacancies = []

    def get_vacancies(self) -> list:
        new_request = self.__request['objects']
        for vacancy in new_request:
            tmp = {}
            try:
                tmp["name"] = vacancy['profession']
                tmp["area_name"] = vacancy['town']['title']
                tmp["employer"] = [vacancy['firm_name'], vacancy['client']['link']]
                tmp["employment"] = vacancy['type_of_work']['title']
                tmp["experience"] = vacancy['experience']['title']
                tmp["salary"] = [vacancy['payment_from'], vacancy['payment_to'], vacancy['currency']]
                tmp['responsibility'] = vacancy['client']['description']
            except KeyError:
                continue
            self.__vacancies.append(tmp)
        return self.__vacancies
