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

    def calculate_koef(self, top):
        top[self.game_name] = {}
        a = top[self.game_name]
        # 512 mb 100 %
        # 2 gb 99,95 %
        # 4 gb 98,5 %
        # 6 gb 93,5 %
        # 8 gb 89 %
        # 10 gb 62 %
        # 16 gb 56 %
        # 16+ gb 11 %
        if self.ram == ' 512 MB RAM':
            a['ram'] = float(1)
        elif self.ram == ' 1 GB RAM':
            a['ram'] = float(1)
        elif self.ram == ' 2 GB RAM':
            a['ram'] = float(0.999)
        elif self.ram == ' 4 GB RAM':
            a['ram'] = float(0.985)
        elif self.ram == ' 4 Гигабайт RAM':
            a['ram'] = float(0.985)
        elif self.ram == ' 6 GB RAM':
            a['ram'] = float(0.935)
        elif self.ram == ' 8 GB RAM':
            a['ram'] = float(0.89)
        elif self.ram == ' 10 GB RAM':
            a['ram'] = float(0.64)
        elif self.ram == ' 16 GB RAM':
            a['ram'] = float(0.56)
        elif self.ram == ' 32 GB RAM':
            a['ram'] = float(0.11)
        p = self.processor
        # 2 duo - 90%
        # Core 2 - 90%
        # i3 - 80%
        # i5 - 60%
        # 2.6 GHz - 80%
        # Dual core - 90%
        # 1.7 GHz - 100%
        # i7 - 40%
        if p.find('2 Duo') != -1:
            a['cpu'] = float(0.9)
        elif p.find('Dual core') != -1:
            a['cpu'] = float(0.9)
        elif p.find('Core 2') != -1:
            a['cpu'] = float(0.9)
        elif p.find('i3') != -1:
            a['cpu'] = float(0.8)
        elif p.find('i5') != -1:
            a['cpu'] = float(0.6)
        elif p.find('2.6 GHz') != -1:
            a['cpu'] = float(0.8)
        elif p.find('1.7') != -1:
            a['cpu'] = float(1)
        elif p.find('i7') != -1:
            a['cpu'] = float(0.4)
        v = self.graphics
        # 256 mb - 99%
        # GeForce 8600/9600GT - 95%
        # 2GB - 85%
        # GT 640 - 90%
        # 1GB - 90%
        # GTX 460 - 80%
        # GTX 950 - 85%
        # HD 7730 - 85%
        # GeForce 760
        if v.find('256 MB') != -1:
            a['gpu'] = float(1)
        # elif v.find(''):
        #     a['gpu'] = float()
        elif v.find('GeForce 8600/9600GT') != -1:
            a['gpu'] = float(0.95)
        elif v.find('2GB') != -1:
            a['gpu'] = float(0.85)
        elif v.find('GT 640') != -1:
            a['gpu'] = float(0.9)
        elif v.find('1GB') != -1:
            a['gpu'] = float(0.9)
        elif v.find('GTX 460') != -1:
            a['gpu'] = float(0.7)
        elif v.find('GTX 950') != -1:
            a['gpu'] = float(0.85)
        elif v.find('HD 7730') != -1:
            a['gpu'] = float(0.85)
        elif v.find('GeForce 760') != -1:
            a['gpu'] = float(0.85)
        game = self.game_name
        treatment_new(game, top)
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
    href(soup, your_game_list, to_monitor)


def check2(value, game, to_monitor):
    result_value = ''
    for i in range(0, len(value)):
        if value[i] != '\n':
            if value[i] != '\xa0':
                result_value = result_value + value[i]
    to_monitor[game] = result_value


def href(soup, your_game_list, to_monitor):
    link_games = {}
    for a in soup.find_all('a', class_='gameLink', href=True):
        if a.text in your_game_list:
            link_games[a.text] = a['href']
    system_req(link_games, your_game_list, to_monitor)


def system_req(link_games, your_game_list, to_monitor, type_os='win'):
    top = {}
    steam_games = []  # здесь будут лежать объекты для каждой игры
    if type_os not in OS_LIST:
        exit(-1)
    for game in your_game_list:
        rate = SteamGame
        rate.game_name = game
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
                        rate.ram = str(v)
                    elif str(b) == 'Processor:':
                        rate.processor = str(v)
                    elif str(b) == 'Graphics:':
                        rate.graphics = str(v)
            SteamGame.calculate_koef(rate, top)
            break
    sort_dict(top, to_monitor)

def treatment_new(game, top):
    a = top[game]['cpu']
    b = top[game]['ram']
    c = top[game]['gpu']
    x = (a + b + c) / 3
    x = int(x * 100)
    top[game].clear
    top[game] = x


def sort_dict(top, to_monitor):
    top_new = {}
    list_dict = list(top.items())
    list_dict.sort(key=lambda i: i[1])
    top.clear()
    k = 0
    for i in list_dict:
        k += 1
        top_new[k] = f'{i[0]} - {i[1]}%'
    print('Список игр выбранными вами и их максимальная активность за сегодня\n')
    pprint(to_monitor)
    print()
    print('Топ выбранными вами игр, в которые больше вероятность и игроков, играюших на playkey'
          '\nУказан процент игроков, которые могут себе позволить в '
          'них поиграть, исходя из системных требований\n')
    pprint(top_new)


if __name__ == '__main__':
    list_all_status = []
    list_all_game = []
    main(list_all_game, list_all_status)
