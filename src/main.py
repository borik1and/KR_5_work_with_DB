from src.class_api import get_vacancies, all_vacanciess, format_vacancies
from src.class_dbmanager import create_database
from src.config import config
from src.employers import emp

params = config()

hh = get_vacancies(i for i in emp)
hh_formating = format_vacancies(hh)
print(hh_formating)


# create_database('vacancies', params)


