from api.hhAPI import HHAPI


class HandleJobHH(HHAPI):

    def __init__(self, text: str, salary: str):
        self.__params = {"text": text,
                         "salary": salary,
                         "only_with_salary": "true",
                         "order_by": "relevance",
                         'per_page': "100",
                         }
        super().__init__(self.__params)
        self._vacancies = super().get_vacancies()

    def get_vacancies(self):
        return self._vacancies
