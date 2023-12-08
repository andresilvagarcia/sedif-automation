import pyautogui
from time import sleep

coord = {'importar': [347+10, 59+10], 'pasta': [1336+10, 129+10], 'importar_1': [22+10, 151+10], 'dados': [731, 449]}

def box():
    while True:
        ok = pyautogui.locateOnScreen('img/ok.png', confidence=0.8)
        if ok != None:
            sleep(1)
            pyautogui.press('ENTER')
            break

def dados():
    while True:
        dados = pyautogui.locateOnScreen('img/dados.png', confidence=0.8)
        if dados is not None:
            sleep(1)
            click_coordinates('dados')
            break

def click_coordinates(button):
    x, y = coord[button]
    pyautogui.click(x, y)
    sleep(2)