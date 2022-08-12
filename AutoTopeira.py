from http.client import CONTINUE
from time import sleep
import pyautogui

imglist = ["img\\Alquimistas.PNG", "img\\Benzeno.PNG", "img\\Carbono.PNG", "img\\Fogo.PNG", "img\\Joaquim.PNG", "img\\Kekule.PNG", "img\\Petroleo.PNG", "img\\Plásticos.PNG", "img\\Uréia.PNG", "img\\Wholer.PNG", "img\\Teste.PNG"]

while True:
    for imagem in imglist:
        try:
            localimg = pyautogui.locateOnScreen(imagem)
            pyautogui.click(localimg[0], localimg[1])
            print(localimg)
            print("passou")
        except:
            continue
