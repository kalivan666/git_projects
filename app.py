import requests
import sys

class Main():
    def __init__(self, values):
        page = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        if page.status_code // 100 != 2:
            print(f'failed to execute request, status_code: {page.status_code}')
            sys.exit(-1)
        self.data = page.json()
        self.valute = self.data['Valute']
        self.to_monitor = {}
        for value in values:
            if value in self.valute:
                valute = self.valute[value]
                self.to_monitor[value] = valute['Value']
        self.to_monitor['RUB'] = 1


    def translate(self, treatment):
        dictionary = {'в': 'v', 'и': 'i', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
                      'п': 'p', 'с': 's', 'т': 't', 'ж': 'j', 'е': 'e', 'я': 'ya', 'ь': ' '}
        for key in dictionary:
            treatment = treatment.replace(key, dictionary[key])
        return treatment
#положить
#снять
#перевести
#поменять