import requests


class Hh_api:
    HH_API_URL = 'https://api.hh.ru/vacancies'
    HH_API_URL_AREAS = 'https://api.hh.ru/vacancies'

    def __init__(self, keyword):
        super().__init__()

        self.params = {
            'per_page': 100,
            'text': keyword,
            'area': 1
        }

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.params['per_page']}, "
                f"{self.params['text']}, {self.params['area']})")

    def get_vacancies(self):
        respons = requests.get(self.HH_API_URL, self.params)
        return respons.json()

    def format_vacancies(self, all_vacancies):
        vacancies = {'vacancies': []}
        for vacancy in all_vacancies['items']:
            if vacancy['salary'] is None:
                salary = 0
            elif vacancy['salary']['from'] is None:
                salary = vacancy['salary']['to']
            elif vacancy['salary']['to'] is None:
                salary = vacancy['salary']['from']
            else:
                salary = (vacancy['salary']['from'] + vacancy['salary']['to']) // 2
            new_job = {'name': vacancy['name'], 'url': vacancy['url'], 'salary': salary,
                       'experience': vacancy['experience']['name'],
                       'employer_name': vacancy['employer']['name'],
                       'address': vacancy['address'],
                       'vacancy_id': vacancy['id']}
            vacancies['vacancies'].append(new_job)
        return vacancies
