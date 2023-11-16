from src.class_dbmanager import create_database, DBManager
from src.class_save import save_data_to_database
from src.config import config

params = config()
db_manager = DBManager(params)

create_database('vacancies', params)
save_data_to_database()

while True:
    word = input('Программа совершит для Вас поиск доступных вакансий с сайта hh.ru, Вы можете выбрать одну из' 
    'ниже перечисленных возможностей сортировки поиска:\n  1  -  чтобы получить список всех компаний и количество '
    'вакансий у каждой компании. \n  2  -  чтобы получить список всех вакансий с указанием названия компании,'
    'названия вакансии, зарплаты и ссылки на вакансию.\n  3  -  чтобы получить среднюю зарплату по вакансиям.\n  4  -  ' 
    'чтобы получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n  5  -  чтобы'
    'получить список всех вакансий, в названии которых содержатся переданные в метод слова, например python.\n'
    '  6  -  чтобы выйти из программы\n'
     'Ваш выбор:  ')
    if word == '1':
        # получает список всех компаний и количество вакансий у каждой компании.
        db_manager.get_companies_and_vacancies_count()
    elif word == '2':
        # получает список всех вакансий с указанием названия компании,
        # названия вакансии и зарплаты и ссылки на вакансию.
        db_manager.get_all_vacancies()
    elif word == '3':
        # получает среднюю зарплату по вакансиям.
        db_manager.get_avg_salary()
    elif word == '4':
        # получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        db_manager.get_vacancies_with_higher_salary()
    elif word == '5':
        # получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        db_manager.get_vacancies_with_keyword()
    elif word == '6':
        break
