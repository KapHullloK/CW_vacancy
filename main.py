from tools.HHtools import HandleJobHH
from tools.SuperJobTools import HandleJobSJ
from tools.allTools import validate_params, validate_top_n, output_vacancies
from file_handlers.json_file_handler import JSONSaver

json_saver = JSONSaver()


def user_interaction():
    while True:
        filter_words = input("Введите ключевое слово/фразу для поиска: ")
        salary = input("Введите желаемую зарплату: ")
        if validate_params(filter_words, salary):
            print("Invalid input")
        else:
            hh_vacancies = HandleJobHH(filter_words, salary).get_vacancies()
            sj_vacancies = HandleJobSJ(filter_words, salary).get_vacancies()
            json_saver.delete_all()
            json_saver.save_vacancy(hh_vacancies)
            json_saver.save_vacancy(sj_vacancies)

            top_n = input("Введите N(ое) количество топ вакансий или нажмите ENTER: ")
            if validate_top_n(top_n):
                print("| HH_vacancies /")
                output_vacancies(hh_vacancies, abs(int(top_n)))
                print("| SJ_vacancies /")
                output_vacancies(sj_vacancies, abs(int(top_n)))
            else:
                print("| HH_vacancies /")
                output_vacancies(hh_vacancies, abs(int(top_n)))
                print("| SJ_vacancies /")
                output_vacancies(sj_vacancies, abs(int(top_n)))
            break


if __name__ == "__main__":
    user_interaction()
