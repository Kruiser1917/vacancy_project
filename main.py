# main.py

from db.db_manager import DBManager
from db.create_tables import create_tables
from db.load_data import load_data_to_db
from hh_api.hh_client import HHAPI
from interface.user_interface import user_interface
from db.config import DB_NAME, DB_USER, DB_PASSWORD


def main():
    # Настройка подключения к БД
    db_manager = DBManager(db_name=DB_NAME, user=DB_USER, password=DB_PASSWORD)

    # Создание таблиц
    create_tables(db_manager)

    # Получение данных через API
    hh_api = HHAPI()
    employer_ids = ['1740', '1455', '1558']  # Пример ID компаний
    load_data_to_db(hh_api, db_manager, employer_ids)

    # Взаимодействие с пользователем
    user_interface(db_manager)

    # Закрытие соединения с БД
    db_manager.close()


if __name__ == '__main__':
    main()
