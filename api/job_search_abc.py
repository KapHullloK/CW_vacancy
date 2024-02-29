from abc import ABC, abstractmethod


class JobSearchSite(ABC):
    @abstractmethod
    def fetch_vacancies(self):
        pass
