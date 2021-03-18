import os


# при кажом запуске меняет клавиши 'атака' и 'стоп' местами в файлах конфигурации пользоателя
# данный файл, который изменяется, принимается игрой при каждом ее запуске и открытия настроек в игре

def treatment(path):
    dotakeys = open(path, 'r+')
    a = dotakeys.readlines()
    b = a.index('\t\t\t"Key"\t\t"A"\n')
    if b == 65:
        a.pop(73)
        a.insert(73, '\t\t\t"Key"\t\t"A"\n')
        a.pop(65)
        a.insert(65, '\t\t\t"Key"\t\t"S"\n')
    else:
        a.pop(65)
        a.insert(65, '\t\t\t"Key"\t\t"A"\n')
        a.pop(73)
        a.insert(73, '\t\t\t"Key"\t\t"S"\n')
    listt = a
    dotakeys.close()

    dotakeys = open(path, 'w')
    dotakeys.writelines(listt)
    dotakeys.close()
    open()


# '\t\t\t"Key"\t\t"S"\n' - 65
# '\t\t\t"Key"\t\t"A"\n' - 73

# эта функция открывает стим через консоль

def open():
    os.system('Steam')
    # если виндовс
    os.system('C:\Program Files\Steam\Steam.exe')  # стандартный путь


if __name__ == '__main__':
    path = '/home/vovucho/.steam/steam/userdata/323343420/570/remote/cfg/dotakeys_personal.lst'
    treatment(path)