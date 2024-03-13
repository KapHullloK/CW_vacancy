from api.superjobAPI import SuperJobAPI


class HandleJobSJ(SuperJobAPI):
    def __init__(self, text: str, salary: str):
        self.__params = {"keyword": text,
                         "payment_from": salary,
                         "order_field": "date"
                         }
        super().__init__(self.__params)
        self._vacancies = super().get_vacancies()

    def get_vacancies(self):
        return self._vacancies
