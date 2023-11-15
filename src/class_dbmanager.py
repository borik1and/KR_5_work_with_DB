import psycopg2

from src.class_api import get_vacancies, format_vacancies
from src.config import config
from src.employers import emp

params = config()
hh = get_vacancies(i for i in emp)
hh_formating = format_vacancies(hh)


class DBManager:

    def __init__(self, params):
        self.params = params

    def get_companies_and_vacancies_count(self):
        # получает список всех компаний и количество вакансий у каждой компании.
        with psycopg2.connect(dbname='vacancies', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute('''SELECT employers.employer_name AS "список всех компаний", COUNT(vacancy.employer_id) AS
                            "количество вакансий" FROM employers LEFT JOIN vacancy ON employers.employer_id
                             = vacancy.employer_id GROUP BY employers.employer_id, employers.employer_name;''')

                # Получаем результаты
                results = cur.fetchall()

                # Выводим результаты
                for row in results:
                    print(f"Компания: {row[0]}, Количество вакансий: {row[1]}")

    def get_all_vacancies(self):
        # получает список всех вакансий с указанием названия компании,
        # названия вакансии и зарплаты и ссылки на вакансию.
        with psycopg2.connect(dbname='vacancies', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT employer_name, vacancy_name, salary, url FROM vacancy")

                # Получаем результаты
                results = cur.fetchall()

                # Выводим результаты
                for row in results:
                    print(f"Работадатель: {row[0]}, Название вакансии: {row[1]}, Зарплата: {row[2]},"
                          f" Cсылка на вакансию: {row[3]}")

    def get_avg_salary(self):
        # получает среднюю зарплату по вакансиям.
        with psycopg2.connect(dbname='vacancies', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute('''SELECT vacancy_name, ROUND(AVG(salary)) AS
                 average_salary FROM vacancy GROUP BY vacancy_name''')

                # Получаем результаты
                results = cur.fetchall()

                # Выводим результаты
                for row in results:
                    print(f"Название вакансии: {row[0]}, Средняя зарплата: {row[1]}")

    def get_vacancies_with_higher_salary(self):
        # получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        pass

    def get_vacancies_with_keyword(self):
        # получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        pass


def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о вакансиях."""

    # Подключаемся к базе данных PostgreSQL (по умолчанию postgres), чтобы создать новую базу данных
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    # Удаляем существующую базу данных с указанным именем (если она существует)
    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
    # Создаем новую базу данных с указанным именем
    cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()

    # Подключаемся к базе данных
    conn = psycopg2.connect(dbname=database_name, **params)

    # Создаем таблицу 'vacancy'
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS vacancy ( 
                    employer_id INT,  
                    vacancy_id INT,                          
                    vacancy_name VARCHAR(100) NOT NULL,      
                    url TEXT,                                
                    salary INT,                              
                    experience VARCHAR(50),                          
                    employer_name VARCHAR(100)               
                )                                            
        """)

    # Создаем таблицу 'employers'
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employers (
                employer_id INT,         
                employer_name VARCHAR     
            )                            
        """)

    conn.commit()
    conn.close()
