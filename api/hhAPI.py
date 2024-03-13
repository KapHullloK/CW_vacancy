from file_handlers.job_search_abc import JobABC
import requests


class HHAPI(JobABC):
    def __init__(self, search_params: dict = None):
        self.__search_params = search_params
        self.__request = requests.get("https://api.hh.ru/vacancies",
                                      params=self.__search_params).json()
        self.__vacancies = []

    def get_vacancies(self) -> list:
        new_request = self.__request['items']
        for vacancy in new_request:
            tmp = {}
            try:
                tmp["name"] = vacancy['name']
                tmp["area_name"] = vacancy['area']['name']
                tmp["employer"] = [vacancy['employer']['name'], vacancy['employer']['alternate_url']]
                tmp["employment"] = vacancy['employment']['name']
                tmp["experience"] = vacancy['experience']['name']
                tmp["salary"] = [vacancy['salary']['from'], vacancy['salary']['to'], vacancy["salary"]["currency"]]
                tmp['responsibility'] = vacancy['snippet']['responsibility']
            except KeyError:
                continue
            self.__vacancies.append(tmp)
        return self.__vacancies
