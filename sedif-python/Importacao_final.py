import pyautogui
import os
import keyboard
import defs

diretorio = 'C:/Users/Andre/Desktop/DESTDASEDIF'
arquivos = os.listdir(diretorio)

if __name__ == '__main__':
    keyboard.wait('F1')
    for arquivo in arquivos:
        defs.click_coordinates('importar')
        defs.click_coordinates('pasta')
        list = pyautogui.write(arquivo)
        pyautogui.press('ENTER')
        defs.click_coordinates('importar_1')
        defs.dados()
        defs.box()
        defs.click_coordinates('importar')