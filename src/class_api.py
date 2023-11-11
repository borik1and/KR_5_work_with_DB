import requests

# Import employers from 'src/employers.py' assuming it contains a list of employer IDs
from src.employers import emp

HH_API_URL = 'https://api.hh.ru/vacancies'
params = {
    'per_page': 100,
    'area': 1
}

def get_vacancies(employer_id):
    params['employer_id'] = employer_id
    try:
        response = requests.get(HH_API_URL, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def format_vacancies(all_vacancies):
    vacancies = []
    for vacancy in all_vacancies.get('items', []):
        salary = 0
        if vacancy['salary']:
            salary_from = vacancy['salary'].get('from')
            salary_to = vacancy['salary'].get('to')
            if salary_from is not None and salary_to is not None:
                salary = (salary_from + salary_to) // 2
            elif salary_from is not None:
                salary = salary_from
            elif salary_to is not None:
                salary = salary_to
        new_job = {
            'name': vacancy['name'],
            'url': vacancy['url'],
            'salary': salary,
            'experience': vacancy['experience']['name'],
            'employer_name': vacancy['employer']['name'],
            'vacancy_id': vacancy['id']
        }
        vacancies.append(new_job)
    return vacancies

def get_employers_vacancy():
    for employer_id in emp:
        all_vacancies = get_vacancies(employer_id)
        if all_vacancies:
            formatted_vacancies = format_vacancies(all_vacancies)
            print(f"Vacancies for employer {employer_id}:")
            print(formatted_vacancies)
            print("\n")

get_employers_vacancy()
