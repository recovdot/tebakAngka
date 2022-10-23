import PySimpleGUI as sg
import random
angka = random.randint(0, 5)
print(angka)
inp = None
sg.theme("DarkAmber")


layout = [  [sg.Text('Masukan Angka', font="Poppins"), sg.InputText()],
            [sg.Button('Ok', key="Ok"), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Tebak Angka', layout, icon=r'img/ico.ico')
# Event Loop to process "events" and get the "values" of the inputs

def open_window_true():
    layout = [[sg.Text("Benar", key="new"), sg.Button('Exit')]]
    window = sg.Window("Tebak Angka", layout, modal=True, icon=r"img/ico.ico")
    # choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()

def open_window_false():
    layout = [[sg.Text("Salah", key="new"), sg.Button('Exit')]]
    window = sg.Window("Tebak Angka", layout, modal=True, icon=r"img/ico.ico")
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()

def open_window_test():
    global window
    global values
    values = window.read()
    def test():
        if(values[0] == angka):
         return "Benar"
    choice = None
    layout = [[sg.Text(test(), key="new")]]
    window = sg.Window("Tebak Angka", layout, modal=True, icon=r"img/ico.ico")
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()

def popup():
    event, values = window.read()
    while int(values[0]) != angka:
        # inp = input("Masukan Angka: ")
        # inpA = int(inp)

        if(int(values[0]) == angka):
            # print("Benar")
            open_window_true()
            break
        else:
            open_window_false()
            # if(int(values[0]) > angka):

            # if(int(values[0]) < angka):



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

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "Ok":
        hasil()
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

window.close()