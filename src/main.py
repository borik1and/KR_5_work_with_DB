from src.class_api import Hh_api
from src.vacancies import Vacancy
from src.class_save import JsonSave, add_vacancy


keyword = input('Введите ключевые слова для фильтрации вакансий: ')
hh = Hh_api(keyword)
hh_vacancies = hh.format_vacancies(hh.get_vacancies())
# add_vacancy()
# Vacancy.compare_vacancies_by_salary()

print(hh_vacancies)
