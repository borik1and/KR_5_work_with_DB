import json
import os
from src.class_api import get_vacancies, format_vacancies
from src.config import config
from src.employers import emp

params = config()

hh = get_vacancies(i for i in emp)
hh_formating = format_vacancies(hh)

import psycopg2


class JsonSave:
    all_vacancies = {}

    @staticmethod
    def delete_file():
        if os.path.exists('vacancies.json'):
            os.remove('vacancies.json')

    @classmethod
    def get_vacancies(cls):
        with open('vacancies.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data


def add_vacancy():
    with open('vacancies.json', 'w', encoding='utf-8') as json_file:
        json.dump(JsonSave.all_vacancies, json_file, indent=4, ensure_ascii=False)



def save_data_to_database() -> None:
    """сохранение данных в базу данныз"""
    with psycopg2.connect(dbname='vacancies', **params) as conn:
        with conn.cursor() as cur:
            # Преобразование словарей в кортежи перед вставкой
            values_for_orders = [
                (v['employer_id'], v['vacancy_id'], v['vacancy_name'], v['url'], v['salary'], v['experience'],
                 v['employer_name']) for v in
                hh_formating]

            # Выполнение множественной вставки с кортежами
            cur.executemany("INSERT INTO vacancy VALUES(%s, %s, %s, %s, %s, %s, %s)", values_for_orders)
            #
            if isinstance(emp, dict):  # Проверяем, что emp - это словарь
                cur.executemany("INSERT INTO employers VALUES(%s, %s)", [i for i in emp.items()])

