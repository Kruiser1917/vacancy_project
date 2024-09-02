# db/load_data.py

from hh_api.hh_client import HHAPI
from db.db_manager import DBManager

def load_data_to_db(hh_api, db_manager, employer_ids):
    """Загружает данные о компаниях и вакансиях в базу данных."""
    for employer_id in employer_ids:
        employer_info = hh_api.get_employer_info(employer_id)
        db_manager.insert_company(
            hh_id=employer_info['id'],
            name=employer_info['name'],
            url=employer_info['alternate_url']
        )
        vacancies = hh_api.get_company_vacancies(employer_id)
        for vacancy in vacancies['items']:
            db_manager.insert_vacancy(
                hh_id=vacancy['id'],
                name=vacancy['name'],
                salary_from=vacancy['salary']['from'] if vacancy['salary'] else None,
                salary_to=vacancy['salary']['to'] if vacancy['salary'] else None,
                url=vacancy['alternate_url'],
                employer_id=employer_info['id']
            )

# Пример использования:
# hh_api = HHAPI()
# db_manager = DBManager(DB_NAME, DB_USER, DB_PASSWORD)
# employer_ids = ['1740', '1455', '1558']
# load_data_to_db(hh_api, db_manager, employer_ids)
