import PySimpleGUI as sg
import random
import os
import pygame
from pygame.locals import *
from pygame import mixer

# Var System
angka = random.randint(0, 5)
print(angka)
inp = None

# Var Data
mIcon = 'img/ico.ico'
mFont = 'Poppins'

sg.theme("DarkAmber")


home_layout = [
           [sg.Column([[sg.Image('img/tolol.jpg')]], justification='center')],
           [sg.Column([[sg.Text('Selamat Datang, dan Selamat Bermain :D', font="Poppins")]], justification='center')],
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
file = 'bgm/Spanish Flea.mp3'
# os.system('mpg123' + file)

mixer.init()
mixer.music.load('bgm/Spanish Flea.mp3')
mixer.music.play()

def open_window_true():
    mixer.init()
    song_true = mixer.Sound('bgm/correct.wav')
    song_true.play(0)
    layout = [ [sg.Column([[sg.Text("Benar", key="new", font=mFont)]], justification='center')],
              [sg.Image('img/true.png')],
              [sg.Column([[sg.Button('Exit')]], justification='center')]
             ]
    window = sg.Window("Tebak Angka", layout, modal=True, icon=r"img/ico.ico")
    # choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()

def open_window_false():
    mixer.init()
    # mixer.music.load('bgm/wrong.wav')
    # mixer.music.play()
    song_false = mixer.Sound('bgm/wrong.wav')
    song_false.play(0)
    layout = [[sg.Column([[sg.Text("Salah", key="new", font=mFont)]], justification='center')],
              [sg.Image('img/false.png')],
              [sg.Column([[sg.Button('Exit')]], justification='center')]
              ]
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

    if(int(values[0]) == angka):
        open_window_true()
    else:
        if(int(values[0]) > angka):
            open_window_false()
        if(int(values[0]) < angka):
            open_window_false()

def hint():
    global angka, event, values


    if(angka > 5):
        hint_window()

def hint_window():
    global angka, event, values

    layout_1 = [
        [sg.Text('Angka Kecil', font=mFont)]
    ]

    layout_2 = [
        [sg.Text('Angka Besar', font=mFont)]
    ]

    if(angka >= 0 and angka <= 3):
        window = sg.Window("Hint", layout=layout_1, icon=mIcon)
        while True:
            event, values = window.read()
            if event == "Cancel" or event == sg.WIN_CLOSED:
                break

            window.close()
    elif(angka <= 5 and angka >= 3):
        window = sg.Window("Hint", layout=layout_2, icon=mIcon)
        while True:
            event, values = window.read()
            if event == "Cancel" or event == sg.WIN_CLOSED:
                break

def game():
    global event, values

    layout = [  [sg.Text('Masukan Angka', font="Poppins"), sg.InputText()],
                     [sg.Button('Ok', key="Ok", font=mFont), sg.Button('Cancel', font=mFont), sg.Button('Hint', key='Hint', font=mFont)]]
    window = sg.Window('Tebak Angka', layout, icon=r'img/ico.ico')
    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        if event == "Ok":
            hasil()
        if event == "Hint":
            hint_window()

    window.close()

def about():
    global event, values
    layout = [ [sg.Text('Follow ig gwejh @tomoeisozaki', font=mFont)],
             ]
    window = sg.Window('Tebak Angka - About', layout, icon=mIcon)
    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break

    window.close()

def help():
    layout = [
             [sg.Text('Jadi cara mainnya tu Gini, nantinya begitu, Klik Play ', font=mFont)]
             ]
    window = sg.Window('Tebak Angka - Help', layout, icon=mIcon)
    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
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
    if event == 'About':
        about()
    if event == 'Help':
        help()

home_window.close()