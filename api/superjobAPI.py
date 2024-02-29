from pprint import pprint

from api.job_search_abc import JobSearchSite
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_key')


class SuperjobSearchSite(JobSearchSite):
    def __init__(self, search_params: dict):
        self.__headers: dict = {'X-Api-App-Id': api_key}
        self.__search_params: dict = search_params

    def fetch_vacancies(self):
        return requests.get("https://api.hh.ru/vacancies",
                            headers=self.__headers, params=self.__search_params).json()
