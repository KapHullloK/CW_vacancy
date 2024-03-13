def validate_params(filter_words: str, salary: str) -> bool:
    if (not filter_words) or (not salary.isdigit()):
        return True
    return False


def validate_top_n(top: str):
    if top.isdigit():
        return True
    return False


def output_vacancies(vacancies: list, top_n=10 ** 6) -> None:
    for vacancy in vacancies:
        print(vacancy["name"])
        print(vacancy["area_name"])
        print(vacancy["employer"])
        print(vacancy["employment"])
        print(vacancy["experience"])
        print(vacancy["salary"])
        print(vacancy['responsibility'], "\n")
        top_n -= 1
        if top_n <= 0:
            break
