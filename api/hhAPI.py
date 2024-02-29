from api.job_search_abc import JobSearchSite
import requests
from pprint import pprint


class HHSearchSite(JobSearchSite):
    def __init__(self, search_params: dict):
        self.__search_params: dict = search_params

    def fetch_vacancies(self):
        return requests.get("https://api.hh.ru/vacancies", params=self.__search_params).json()
