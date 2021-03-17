from app import Main
import aiohttp
import asyncio
import pprint


class wallet:
    def __init__(self, values, cash_monitor):
        self.cash = {}
        self.currency = Main.__init__(Main, values)


def check(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def Input():
    i = 0
    values = []
    while i == 0:
        Bool = (input('Add currency? y/f\n')).upper()
        if Bool == 'Y':
            valute = ((input('Enter currency\nExample: usd\n')).upper())
            if valute in Main.valute:
                values.append(valute)
            else:
                print('Wrong currency')
        elif Bool == 'F':
            i = i + 1
            while i == 1:
                N = input('Updating currency data (period)\n')
                if check(N):
                    N = int(N)
                    i = i + 1
                else:
                    print('Wrond period')
        else:
            print('Wrong y/f')


async def sync(values, cash_monitor):
    global translate
    loop = asyncio.get_event_loop()
    the_choice = await loop.run_in_executor(None, input, 'Пополнить или снять деньги? yes/no\n')
    if the_choice.upper() == 'YES':
        list_values = ['RUB'] + values
        a = '\n'.join(list_values)
        the_choice = await loop.run_in_executor(None, input, f'Какую валюту хотите выбрать?\n{a}\n')
        for value in list_values:
            cash_monitor[value] = 0
            if the_choice.upper() == value:
                theChoice = await loop.run_in_executor(None, input, 'Какую операцию хотите провести?\nПополнить, '
                                                                    'снять, перевести или поменять валюту\n')
                translate = Main.translate(Main, theChoice.lower())
        loop.close()
        task = asyncio.create_task(treatmentt(translate))
        await task

    else:
        pass

async def treatmentt(translate):
    if True:
        print(123)
async def main(values, N, cash_monitor):
    while True:
        wallet.__init__(wallet, values, cash_monitor)
        await asyncio.sleep(N)


if __name__ == '__main__':
    Main.__init__(Main, 'USD')
    i = 0
    values = []
    cash_monitor = {}
    while i == 0:
        Bool = (input('Добавить валюту? y/f\n')).upper()
        if Bool == 'Y':
            valute = ((input('Какую валюту?\nExample: usd\n')).upper())
            if valute in Main.valute:
                values.append(valute)
            else:
                print('Неправильно название!')
        elif Bool == 'F':
            i = i + 1
            while i == 1:
                N = input('Частота обновления курса (period)\n')
                if check(N):
                    N = int(N)
                    i = i + 1
                else:
                    print('Неправильно ввели')
        else:
            print('Надо y/f')
    loop = asyncio.get_event_loop()
    main_task = asyncio.wait([main(values, N, cash_monitor), sync(values, cash_monitor)])
    try:
        loop.run_until_complete(main_task)
    except asyncio.CancelledError:
        loop.run_until_complete(main_task)
    loop.close()
