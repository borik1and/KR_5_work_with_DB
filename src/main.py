from src.class_api import Hh_api
# from src.class_dbmanager import create_database
# from src.class_dbmanager import save_data_to_database
# from src.vacancies import Vacancy
# from src.class_save import JsonSave, add_vacancy
# from src.config import config

# params = config()

keyword = input('Введите ключевые слова для фильтрации вакансий: ')
hh = Hh_api(keyword)
hh_vacancies = hh.format_vacancies(hh.get_vacancies())
hh_employers = hh.format_employers(hh.get_vacancies())
# add_vacancy()
# Vacancy.compare_vacancies_by_salary()

# save_data_to_database(data, 'vacancies', params)

# create_database('vacances', {'localhost', 'postgres', '1975', '5432'})

print(hh_vacancies)
print(hh_employers)
# print(hh.get_vacancies())