from src.class_api import get_vacancies, format_vacancies
from src.class_dbmanager import create_database, DBManager
from src.class_save import save_data_to_database
from src.config import config
from src.employers import emp

params = config()
db_manager = DBManager(params)

create_database('vacancies', params)
save_data_to_database()

# получает список всех компаний и количество вакансий у каждой компании.
db_manager.get_companies_and_vacancies_count()

# получает список всех вакансий с указанием названия компании,
# названия вакансии и зарплаты и ссылки на вакансию.
db_manager.get_all_vacancies()

# получает среднюю зарплату по вакансиям.
db_manager.get_avg_salary()

# получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
db_manager.get_vacancies_with_higher_salary()

# hh = get_vacancies(i for i in emp)
# hh_formating = format_vacancies(hh)

