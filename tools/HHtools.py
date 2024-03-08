from api.hhAPI import HHAPI
from file_handlers.json_file_handler import JSONSaver

jsonTool = JSONSaver()


class HandleJobHH(HHAPI):

    def __init__(self, text: str, salary: str):
        self.top_n: int = 0
        self.__params = {"text": text,
                         "salary": salary,
                         "only_with_salary": "true",
                         "order_by": "relevance",
                         'per_page': "100",
                         }
        super().__init__(self.__params)

    def output_vacancies(self):
        vacancies = super().get_vacancies()
        jsonTool.delete_all()
        jsonTool.save_vacancy(vacancies)
        cnt = 10 ** 6
        if self.top_n > 0:
            cnt = self.top_n

        for vacancy in vacancies:
            print(vacancy["name"])
            print(vacancy["area_name"])
            print(vacancy["employer"])
            print(vacancy["employment"])
            print(vacancy["experience"])
            print(vacancy["salary"])
            print(vacancy["schedule"])
            print(vacancy['responsibility'], "\n")
            cnt -= 1
            if cnt == 0:
                break

    def validate_top_n(self, top: str):
        if top.isdigit():
            self.top_n = int(top)


def validate_params(filter_words: str, salary: str):
    if (not filter_words) or (not salary.isdigit()):
        return True
    return False
