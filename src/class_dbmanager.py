import psycopg2
import csv
from typing import Any




"""Скрипт для заполнения данными таблиц в БД Postgres."""

db_config = {
    'dbname': 'north',
    'user': 'postgres',
    'password': '1975',
    'host': 'localhost'
}

with psycopg2.connect(**db_config) as conn:
    with conn.cursor() as cur:
        cur.executemany("INSERT INTRO vacancyes VALUES(%s, %s, %s, %s, %s, %s)", [i for i in employees])
        cur.executemany("INSERT INTRO employers VALUES(%s, %s, %s)", [i for i in customers])
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


def create_database(database_name: str, params: dict) -> None:
    """создание базы данных и таблиц"""

    conn = psycopg2.connect(dbname='postgres', **db_config)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE vacancy (
                    id_vacancy INT,
                    title_vacancy VARCHAR(100) NOT NULL,
                    url_vacancy TEXT,
                    selary_from INT,
                    selary_to INT,
                    selary_currency VARCHAR(10),
                    employer_id INT
                )
            """)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE employer (
                    employer_id INT REFERENCES vacancy(employer_id),
                    employer_name VARCHAR(50),
                    employer_url TEXT
                )
            """)

    conn.commit()
    conn.close()


def save_data_to_database(data: list[dict[str, Any]], database_name: str, params: dict) -> None:
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
