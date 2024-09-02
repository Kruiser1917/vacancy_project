# db/db_manager.py

import psycopg2
from psycopg2 import sql

class DBManager:
    def __init__(self, db_name, user, password, host="localhost", port="5432"):
        self.connection = psycopg2.connect(
            dbname=db_name, user=user, password=password, host=host, port=port
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """Создает таблицы компаний и вакансий в БД."""
        create_companies_table = """
        CREATE TABLE IF NOT EXISTS companies (
            id SERIAL PRIMARY KEY,
            hh_id VARCHAR(50) UNIQUE NOT NULL,
            name VARCHAR(255) NOT NULL,
            url TEXT
        );
        """
        create_vacancies_table = """
        CREATE TABLE IF NOT EXISTS vacancies (
            id SERIAL PRIMARY KEY,
            hh_id VARCHAR(50) UNIQUE NOT NULL,
            name VARCHAR(255) NOT NULL,
            salary_from INTEGER,
            salary_to INTEGER,
            url TEXT,
            employer_id INTEGER REFERENCES companies(id) ON DELETE CASCADE
        );
        """
        self.cursor.execute(create_companies_table)
        self.cursor.execute(create_vacancies_table)

    def insert_company(self, hh_id, name, url):
        """Вставляет данные о компании в таблицу companies."""
        insert_query = """
        INSERT INTO companies (hh_id, name, url) VALUES (%s, %s, %s)
        ON CONFLICT (hh_id) DO NOTHING;
        """
        self.cursor.execute(insert_query, (hh_id, name, url))

    def insert_vacancy(self, hh_id, name, salary_from, salary_to, url, employer_id):
        """Вставляет данные о вакансии в таблицу vacancies."""
        insert_query = """
        INSERT INTO vacancies (hh_id, name, salary_from, salary_to, url, employer_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (hh_id) DO NOTHING;
        """
        self.cursor.execute(insert_query, (hh_id, name, salary_from, salary_to, url, employer_id))

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        query = """
        SELECT c.name, COUNT(v.id) as vacancies_count
        FROM companies c
        LEFT JOIN vacancies v ON c.id = v.employer_id
        GROUP BY c.name;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты."""
        query = """
        SELECT c.name, v.name, v.salary_from, v.salary_to, v.url
        FROM vacancies v
        JOIN companies c ON v.employer_id = c.id;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        query = """
        SELECT AVG((v.salary_from + v.salary_to)/2) as avg_salary
        FROM vacancies v;
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        avg_salary = self.get_avg_salary()
        query = """
        SELECT c.name, v.name, v.salary_from, v.salary_to, v.url
        FROM vacancies v
        JOIN companies c ON v.employer_id = c.id
        WHERE ((v.salary_from + v.salary_to)/2) > %s;
        """
        self.cursor.execute(query, (avg_salary,))
        return self.cursor.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова."""
        query = """
        SELECT c.name, v.name, v.salary_from, v.salary_to, v.url
        FROM vacancies v
        JOIN companies c ON v.employer_id = c.id
        WHERE v.name ILIKE %s;
        """
        self.cursor.execute(query, (f'%{keyword}%',))
        return self.cursor.fetchall()

    def close(self):
        """Закрывает соединение с БД."""
        self.cursor.close()
        self.connection.close()

# Пример использования методов класса DBManager:
# db_manager.get_companies_and_vacancies_count()
# db_manager.get_all_vacancies()
# db_manager.get_avg_salary()
# db_manager.get_vacancies_with_higher_salary()
# db_manager.get_vacancies_with_keyword('Python')
