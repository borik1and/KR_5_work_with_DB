import psycopg2
import csv


def open_csv_file(file):
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)
    return data


employees = open_csv_file('north_data/employees_data.csv')
customers = open_csv_file('north_data/customers_data.csv')
orders = open_csv_file('north_data/orders_data.csv')

"""Скрипт для заполнения данными таблиц в БД Postgres."""

db_config = {
    'dbname': 'north',
    'user': 'postgres',
    'password': '1975',
    'host': 'localhost'
}

with psycopg2.connect(**db_config) as conn:
    with conn.cursor() as cur:
        cur.executemany("INSERT INTRO employees VALUES(%s, %s, %s, %s, %s, %s)", [i for i in employees])
        cur.executemany("INSERT INTRO customers VALUES(%s, %s, %s)", [i for i in customers])
        cur.executemany("INSERT INTRO orders VALUES(%s, %s, %s, %s, %s)", [i for i in orders])
conn.close()


class DBManager:
    def __init__(self):
        pass

    def get_companies_and_vacancies_count(self):
        # получает список всех компаний и количество вакансий у каждой компании.
        pass

    def get_all_vacancies(self):
        # получает список всех вакансий с указанием названия компании,
        # названия вакансии и зарплаты и ссылки на вакансию.
        pass

    def get_avg_salary(self):
        # получает среднюю зарплату по вакансиям.
        pass

    def get_vacancies_with_higher_salary(self):
        # получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        pass

    def get_vacancies_with_keyword(self):
        # получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        pass
