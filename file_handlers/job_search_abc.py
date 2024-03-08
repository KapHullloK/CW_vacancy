from abc import ABC, abstractmethod


class JobABC(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass
