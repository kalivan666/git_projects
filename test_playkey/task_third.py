import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup

def check(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def Input(list_all_game, list_all_status):
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
    treatment(list_all_status, list_all_game, your_game_list)
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

    Input(list_all_game, list_all_status)

def treatment(list_all_status, list_all_game, your_game_list):
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
def check2(value, game, to_monitor):
    result_value = ''
    for i in range(0, len(value)):
        if value[i] != '\n':
            pass
            if value[i] != '\xa0':
                result_value = result_value + value[i]
    to_monitor[game] = result_value



if __name__ == '__main__':
    list_all_status = []
    list_all_game = []
    main(list_all_game, list_all_status)
