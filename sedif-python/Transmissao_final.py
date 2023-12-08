
import pyautogui
import keyboard
from time import sleep
import defs_transmissao
import os


folder_path = 'C:/Users/Andre/Desktop/PY/empresas/'
name_images = []
arquivos = os.listdir(folder_path)

if __name__ == '__main__':
    keyboard.wait('F1')
    coordenadas = defs_transmissao.coordenadas_json()
    for i in range(len(name_images)):
        defs_transmissao.empresa(folder_path, name_images[i])
        defs_transmissao.click_coordinates(coordenadas['abrir2'])
        defs_transmissao.click_coordinates(coordenadas['encerrar'])
        defs_transmissao.click_coordinates(coordenadas['gerar_documento'])
        defs_transmissao.click_coordinates(coordenadas['iniciar_processamento'])
        defs_transmissao.certificado_box()
        defs_transmissao.processo_finalizado()
        defs_transmissao.click_coordinates(coordenadas['transmitir'])
        defs_transmissao.click_coordinates(coordenadas['iniciar_processamento'])
        defs_transmissao.identificacao_box()
        defs_transmissao.processo_finalizado()
        sleep(2)
        pyautogui.press('ESC')
        defs_transmissao.click_coordinates(coordenadas['fechar_tela'])
        defs_transmissao.click_coordinates(coordenadas['iniciar'])
        defs_transmissao.click_coordinates(coordenadas['fechar_documento'])