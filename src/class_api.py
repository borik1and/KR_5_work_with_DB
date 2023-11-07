import requests


class HH_API:
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

    # def load_areas(self):
    #     req = requests.get(HeadHunterAPI.HH_API_URL_AREAS)
    #     dict_areas = req.json()
    #
    #     areas = {}
    #     for k in dict_areas:
    #         for i in range(len(k['areas'])):
    #             if len(k['areas'][i]['areas']) != 0:
    #                 for j in range(len(k['areas'][i]['areas'])):
    #                     areas[k['areas'][i]['areas'][j]['name'].lower()] = k['areas'][i]['areas'][j]['id']
    #             else:
    #                 areas[k['areas'][i]['name'].lower()] = k['areas'][i]['id']
    #     return areas

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
                       'experience': vacancy['experience']['name']}
            vacancies['vacancies'].append(new_job)
        return vacancies
