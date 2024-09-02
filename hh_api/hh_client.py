# hh_api/hh_client.py

import requests

class HHAPI:
    BASE_URL = "https://api.hh.ru"

    def get_company_vacancies(self, employer_id, per_page=100):
        """Получает вакансии компании по ее ID."""
        url = f"{self.BASE_URL}/vacancies"
        params = {
            "employer_id": employer_id,
            "per_page": per_page
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_employer_info(self, employer_id):
        """Получает информацию о компании по ее ID."""
        url = f"{self.BASE_URL}/employers/{employer_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

# Пример использования:
# hh_api = HHAPI()
# employer_info = hh_api.get_employer_info('1740')  # Пример ID компании
# vacancies = hh_api.get_company_vacancies('1740')
