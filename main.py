from tools.HHtools import validate_params, HandleJobHH


def user_interaction():
    while True:
        filter_words = input("Введите ключевое слово/фразу для поиска: ")
        salary = input("Введите желаемую зарплату: ")
        if validate_params(filter_words, salary):
            print("Invalid input")
        else:
            hh_vacancies = HandleJobHH(filter_words, salary)
            top_n = input("Введите N(ое) количество топ вакансий или нажмите ENTER: ")
            print()
            hh_vacancies.validate_top_n(top_n)
            hh_vacancies.output_vacancies()
            break


if __name__ == "__main__":
    user_interaction()
