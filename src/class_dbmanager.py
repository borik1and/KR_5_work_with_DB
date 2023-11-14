from typing import Any

import psycopg2


# with psycopg2.connect(**db_config) as conn:
#     with conn.cursor() as cur:
#         cur.executemany("INSERT INTRO vacancyes VALUES(%s, %s, %s, %s, %s, %s)", [i for i in employees])
#         cur.executemany("INSERT INTRO employers VALUES(%s, %s, %s)", [i for i in customers])
# conn.close()
#

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
                    vacancy_id INT,                          
                    vacancy_name VARCHAR(100) NOT NULL,      
                    url TEXT,                                
                    salary INT,                              
                    experience INT,                          
                    employer_name VARCHAR(100)               
                )                                            
        """)

    # Создаем таблицу 'employer'
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employer (
                employer_id INT,         
                employer_name VARCHAR        
            )                            
        """)

    conn.commit()
    conn.close()


def save_data_to_database(data: list[dict[str, Any]], database_name='vacancies') -> None:
    """сохранение данных в базу данныз"""

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for channel in data:
            channel_data = channel['channel']['snippet']
            channel_stats = channel['channel']['statistics']
            cur.execute(
                """
                INSERT INTO channels (title, views, subscribers, videos, channel_url)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING channel_id
                """,
                (channel_data['title'], channel_stats['viewCount'], channel_stats['subscriberCount'],
                 channel_stats['videoCount'], f"https://www.youtube.com/channel/{channel['channel']['id']}")
            )
            channel_id = cur.fetchone()[0]
            videos_data = channel['videos']
            for video in videos_data:
                video_data = video['snippet']
                cur.execute(
                    """
                    INSERT INTO videos (channel_id, title, publish_date, video_url)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (channel_id, video_data['title'], video_data['publishedAt'],
                     f"https://www.youtube.com/watch?v={video['id']['videoId']}")
                )

    conn.commit()
    conn.close()
