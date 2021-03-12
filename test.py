import requests
import sys
from pprint import pprint


def main(to_monitor):
    a = get_current_valute(to_monitor)
    get_usd_rate(to_monitor)
    get_eur_rate(to_monitor)
    print(to_monitor)
    print(transfer(to_monitor))


def get_current_valute(to_monitor):
    page = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    if page.status_code // 100 != 2:
        print('failed to execute request, status_code: {page.status_code}')
        sys.exit(-1)
    data = page.json()
    valute = data['Valute']
    values = ['USD', 'EUR', 'RUB']

    pprint(valute)
    for value in values:
        if value in valute:
            to_monitor[value] = valute[value]
        else:
            to_monitor['RUB'] = get_rub_rate()


def get_usd_rate(to_monitor):
    usd = {}
    Usd = to_monitor['USD']
    for key in to_monitor['USD']:
        if key == 'Value':
            usd['Value'] = Usd['Value']
    Usd.clear()
    Usd['Value'] = usd['Value']


def get_rub_rate():
    RUB = {}
    RUB['Value'] = 1
    return RUB


def get_eur_rate(to_monitor):
    eur = {}
    Eur = to_monitor['EUR']
    for key in to_monitor['EUR']:
        if key == 'Value':
            eur['Value'] = Eur['Value']
    Eur.clear()
    Eur['Value'] = eur['Value']


def transfer(to_monitor):
    print('В EUR или в USD?')
    a = input()
    a.lower()
    usd = to_monitor['USD']
    eur = to_monitor['EUR']

    if a == 'eur':
        output = eur['Value']
        return output
    elif a == 'usd':
        output = usd['Value']
        return output
    else:
        print('вы ввели неправильно, либо USD либо EUR')
        return None


if __name__ == '__main__':
    to_monitor = {}
    main(to_monitor)