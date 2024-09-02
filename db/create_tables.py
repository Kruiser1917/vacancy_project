# db/create_tables.py

from db.db_manager import DBManager

def create_tables(db_manager):
    """Создает таблицы в базе данных."""
    db_manager.create_tables()

# Пример использования:
# db_manager = DBManager(DB_NAME, DB_USER, DB_PASSWORD)
# create_tables(db_manager)
