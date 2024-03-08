import json
import os


class JSONSaver:

    def __init__(self, file_path="./data/vacancies.json"):
        self.file_path = file_path
        self.vacancies = []

        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file, ensure_ascii=False)

    def get_vacancies(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data
        except json.JSONDecodeError:
            return []

    def save_vacancy(self, data):
        vacancies = self.get_vacancies()
        for vacancy in data:
            vacancies.append(vacancy)
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False)

    def delete_vacancy(self, vacancy_data):
        vacancies = self.get_vacancies()
        if vacancy_data in vacancies:
            vacancies.remove(vacancy_data)
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False)

    def delete_all(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.truncate()
