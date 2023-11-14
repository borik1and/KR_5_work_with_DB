from src.class_api import get_employers_vacancy, all_vacanciess
from src.class_dbmanager import create_database
from src.config import config

# get_employers_vacancy()


params = config()
create_database('vacancies', params)

# print(all_vacanciess)
# print(hh_employers)
