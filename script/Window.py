import tkinter as tk

win = tk.Tk()
h = 500
w = 600
icon = tk.PhotoImage(file='sources/icon.png')
win.iconphoto(False, icon)
# иконка в углу сверху слева
win.title('Cash_RoboForex')
# название окна всерху
win.geometry(f'{h}x{w}+100+200')
# размер окна + размещение
win.resizable(False, False)
# запрещаем менять размер окна
win.config(bg='gray')
# цвет фона
Tittle = tk.Label(win, text= '')


if __name__ == '__main__':
    win.mainloop()