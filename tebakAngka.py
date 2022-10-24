import PySimpleGUI as sg
import random

# Var System
angka = random.randint(0, 5)
print(angka)
inp = None

# Var Data
mIcon = 'img/ico.ico'
mFont = 'Poppins'

sg.theme("DarkAmber")


home_layout = [ [sg.Column([[sg.Text('Selamat Datang, dan Selamat Bermain :D', font="Poppins")]], justification='center')],
           [sg.Column([[sg.Button(' Play ', key='Play', font=mFont)]], justification='center')],
           [sg.Column([[sg.Button(' Help ', key='Help', font=mFont)]], justification='center')],
           [sg.Column([[sg.Button(' About ', key='About', font=mFont)]], justification='center')],
           [sg.Column([[sg.Button(' Exit ', key='Exit', font=mFont)]], justification='center')],
        ]

# game_layout = [  [sg.Text('Masukan Angka', font="Poppins"), sg.InputText()],
#             [sg.Button('Ok', key="Ok"), sg.Button('Cancel')]]

# Create the Window
home_window = sg.Window("Tebak Angka - Layar Beranda", layout=home_layout, icon=r'img/ico.ico', resizable=True)
# game_window = sg.Window('Tebak Angka', layout=game_layout, icon=r'img/ico.ico')
# Event Loop to process "events" and get the "values" of the inputs

def open_window_true():
    layout = [[sg.Text("Benar", key="new"), sg.Image('img/true.png'),sg.Button('Exit')]]
    window = sg.Window("Tebak Angka", layout, modal=True, icon=r"img/ico.ico")
    # choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()

def open_window_false():
    layout = [[sg.Text("Salah", key="new"), sg.Image('img/test.png'), sg.Button('Exit')]]
    window = sg.Window("Tebak Angka", layout, modal=True, icon=r"img/ico.ico")
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()

def hasil():
    global inp
    global angka
    # while int(values[0]) != angka:
        # inp = input("Masukan Angka: ")
        # inpA = int(inp)
    if(int(values[0]) == angka):
        open_window_true()
            # break
    else:
        if(int(values[0]) > angka):
            open_window_false()
        if(int(values[0]) < angka):
            open_window_false()

def game():
    global event, values
    layout = [  [sg.Text('Masukan Angka', font="Poppins"), sg.InputText()],
                     [sg.Button('Ok', key="Ok"), sg.Button('Cancel')]]
    window = sg.Window('Tebak Angka', layout, icon=r'img/ico.ico')
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()

while True:
    event, values = home_window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit': # if user closes window or clicks cancel
        break
    if event == "Ok":
        hasil()
    if event == 'Play':
        game()
        # open_window_true()
        print(event)
        print(values[0])
        # if(values[0] == angka):
            # open_window_true()
        # else:
            # window()
        # popup()
        # open_window()
        # hasil()
    # print('You entered ', values[0])

home_window.close()