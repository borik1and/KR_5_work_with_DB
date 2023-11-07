from src.class_save import JsonSave


class Vacancy:
    all = []

    def __init__(self, name, url, salary, exp):
        self.name = name
        self.url = url
        self.salary = salary
        self.exp = exp

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.url}', '{self.salary}', '{self.exp}')"

    def __str__(self):
        return (f"{self.__class__.__name__}('Професия: {self.name}', 'Страничка оъявления: {self.url}',"
                f" 'Зарплата: {self.salary}', 'Опыт: {self.exp}')")

    def __ge__(self, other):
        # Сравнение по зарплате для текущей вакансии и другой вакансии (other)
        return self.salary >= other.salary

    def __lt__(self, other):
        # Сравнение по зарплате для текущей вакансии и другой вакансии (other)
        return self.salary < other.salary

    def __eq__(self, other):
        # Сравнение по зарплате для текущей вакансии и другой вакансии (other)
        return self.salary == other.salary

    @staticmethod
    def compare_vacancies_by_salary():
        data = JsonSave.get_vacancies()  # Вызываем функцию, чтобы получить данные
        if data:
            vacancies = [Vacancy(v['name'], v['url'], v['salary'], v['experience']) for v in data['vacancies']]
            sorted_vacancies = sorted(vacancies, key=lambda vacancy: vacancy.salary, reverse=True)
            Vacancy.all = sorted_vacancies
            return sorted_vacancies
        else:
            print("Нет данных о вакансиях.")
            return []

    def sort_vacancy(self):
        pass

    @staticmethod
    def print_vacancies(limit=20):
        """Печатает информацию о вакансиях в консоль, ограничивая количество вакансий до заданного лимита."""
        for_print = Vacancy.all
        count = 1
        for vacancy in for_print:
            if count > limit:
                break  # Завершаем цикл, если достигнуто заданное ограничение
            print(
                f'Вакансия №{count}:\nНазвание:{vacancy.name}\n'
                f'Зарплата:{vacancy.salary} рублей\nОпыт работы: {vacancy.exp}\nСсылка на сайт: {vacancy.url}\n')
            count += 1
