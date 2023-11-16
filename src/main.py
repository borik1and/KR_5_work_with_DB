from src.class_dbmanager import create_database, DBManager
from src.class_save import save_data_to_database
from src.config import config
from src.user_interaction import user_interaction

params = config()
db_manager = DBManager(params)

create_database('vacancies', params)
save_data_to_database()
user_interaction()
