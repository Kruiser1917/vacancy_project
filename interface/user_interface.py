# interface/user_interface.py

def user_interface(db_manager):
    """Интерфейс взаимодействия с пользователем для работы с БД."""
    while True:
        print("\nВыберите действие:")
        print("1. Показать список всех компаний и количество вакансий")
        print("2. Показать список всех вакансий")
        print("3. Показать среднюю зарплату по вакансиям")
        print("4. Показать вакансии с зарплатой выше средней")
        print("5. Показать вакансии по ключевому слову")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            companies = db_manager.get_companies_and_vacancies_count()
            for company in companies:
                print(f"Компания: {company[0]}, Количество вакансий: {company[1]}")
        elif choice == '2':
            vacancies = db_manager.get_all_vacancies()
            for vacancy in vacancies:
                print(f"Компания: {vacancy[0]}, Вакансия: {vacancy[1]}, Зарплата: {vacancy[2]}-{vacancy[3]}, URL: {vacancy[4]}")
        elif choice == '3':
            avg_salary = db_manager.get_avg_salary()
            print(f"Средняя зарплата: {avg_salary}")
        elif choice == '4':
            vacancies = db_manager.get_vacancies_with_higher_salary()
            for vacancy in vacancies:
                print(f"Компания: {vacancy[0]}, Вакансия: {vacancy[1]}, Зарплата: {vacancy[2]}-{vacancy[3]}, URL: {vacancy[4]}")
        elif choice == '5':
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            vacancies = db_manager.get_vacancies_with_keyword(keyword)
            for vacancy in vacancies:
                print(f"Компания: {vacancy[0]}, Вакансия: {vacancy[1]}, Зарплата: {vacancy[2]}-{vacancy[3]}, URL: {vacancy[4]}")
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Пример запуска интерфейса:
# db_manager = DBManager(DB_NAME, DB_USER, DB_PASSWORD)
# user_interface(db_manager)
