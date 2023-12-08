import pyautogui
import cv2
import numpy as np
import json
from time import sleep

def coordenadas_json():
    with open('C:/Users/Andre/Desktop/PY/coordenadas.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def empresa(folder_path, image):
    location = pyautogui.locateOnScreen(folder_path + image + '.png', confidence=0.8)
    if location is not None:
        pyautogui.doubleClick(location)
        sleep(1)
        template = cv2.imread('img/102023.png', cv2.IMREAD_GRAYSCALE)
        if template is not None:
            pyautogui.scroll(-1)
            sleep(0.1)
            pyautogui.scroll(-1)
            sleep(0.1)
        screenshot = np.array(pyautogui.screenshot())
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        top_left = max_loc
        sleep(1)
        pyautogui.click(top_left[0]+20, top_left[1]+10)

def click_coordinates(coordenadas):
    x, y = coordenadas
    pyautogui.click(x, y)
    sleep(1)

def certificado_box():
    while True:
        certificado_box = pyautogui.locateOnScreen('img/certificado_box.png', confidence=0.8)
        if certificado_box is not None:
            sleep(1)
            pyautogui.click(691, 435)
            break

def processo_finalizado():
    while True:
        processo_finalizado = pyautogui.locateOnScreen('img/processo_finalizado_box.png', confidence=0.8)
        if processo_finalizado is not None:
            sleep(1)
            pyautogui.click(818, 406)
            break

def identificacao_box():
    while True:
        identificacao_box = pyautogui.locateOnScreen('img/identificacao.png', confidence=0.8)
        if identificacao_box is not None:
            sleep(1)
            pyautogui.write('')
            sleep(1)
            pyautogui.press('TAB')
            sleep(1)
            pyautogui.write('')
            sleep(1)
            pyautogui.press('TAB')
            sleep(1)
            pyautogui.press('SPACE')
            break
