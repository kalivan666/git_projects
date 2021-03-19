import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup, Tag

OS_LIST = ['win', 'mac', 'linux']


class SteamGame:
    def __init__(self, name):
        self.game_name = name
        self.ram = None
        self.graphics = None
        self.processor = None

    def calculate_koef(self):
        """Метод возвращает коэффицент на основе требований
        """
        # ...
        return True


def check(a):
    try:
        int(a)
        return True
    except ValueError:
        return False


def Input(list_all_game, list_all_status, soup):
    your_game_list = []
    i = 0
    while i == 0:
        quantity = input('Хотите топ из топ 10 игр на сайте?\nИли топ из своих игр создать?\nY/F\n')
        if quantity.lower() == 'y':
            m = 0
            while m != 10:
                your_game_list.append(list_all_game[m])
                m += 1
        elif quantity.lower() == 'f':
            i = 0
            while i == 0:
                quantity = input('Из скольки игр вы хотите составить топ?\n')
                if check(quantity):
                    i += 1
                    pprint(list_all_game)
                    quantity = int(quantity)
                    a = 0
                    while a != quantity:
                        new_game = input('Введите игру, которую вы хотите\nТочь в точь как в списке\n')
                        if new_game in list_all_game:
                            your_game_list.append(new_game)
                            a += 1
                        else:
                            print('Вы ввели неверно!\n')
                else:
                    print('Вы неправильно ввели число!\nНужно именно число\n')
        else:
            print('Вы ввели неверное Y или F')
            i -= 1
        i += 1
    treatment(list_all_status, list_all_game, your_game_list, soup)


def main(list_all_game, list_all_status):
    url = 'https://store.steampowered.com/stats/?l=russian'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    states = soup.find_all('tr', class_='player_count_row')
    games = soup.find_all('a', class_='gameLink')
    for state in states:
        list_all_status.append(state.text)
    for game in games:
        list_all_game.append(game.text)

    Input(list_all_game, list_all_status, soup)


def treatment(list_all_status, list_all_game, your_game_list, soup):
    a = len(list_all_game)
    to_monitor = {}
    for game in your_game_list:
        i = 0
        while i != a:
            b = list_all_status[i]
            x = b.find(game)
            if x != int(-1):
                value = b[11:x]
                check2(value, game, to_monitor)
            i += 1
    pprint(to_monitor)
    href(soup, your_game_list)


def check2(value, game, to_monitor):
    result_value = ''
    for i in range(0, len(value)):
        if value[i] != '\n':
            if value[i] != '\xa0':
                result_value = result_value + value[i]
    to_monitor[game] = result_value


def href(soup, your_game_list):
    link_games = {}
    for a in soup.find_all('a', class_='gameLink', href=True):
        if a.text in your_game_list:
            link_games[a.text] = a['href']
    system_req(link_games, your_game_list)


def system_req(link_games, your_game_list, type_os='win'):
    steam_games = []  # здесь будут лежать объекты для каждой игры
    if type_os not in OS_LIST:
        exit(-1)
    for game in your_game_list:
        url = link_games[game]
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        systems_req = soup.find_all('ul', class_='bb_ul')
        for req in systems_req:
            a: Tag = req
            tmp = a.contents
            for i in range(len(tmp)):
                if isinstance(tmp[i].contents[0], Tag):
                    b = tmp[i].contents[0].contents[0]
                    b = str(b)
                    v = tmp[i].contents[1]
                    if str(b) == 'Memory:':
                        print(game, 'оперативная память', v)
                    elif str(b) == 'Processor:':
                        print(game, 'процессор', v)
                    elif str(b) == 'Graphics:':
                        print(game, 'видеокарта', v)
            break






if __name__ == '__main__':
    list_all_status = []
    list_all_game = []
    main(list_all_game, list_all_status)
