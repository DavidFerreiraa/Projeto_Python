from time import sleep
import pyautogui

imglist = ["img\\Alquimistas.PNG", "img\\Benzeno.PNG", "img\\Carbono.PNG", "img\\Fogo.PNG", "img\\Joaquim.PNG", "img\\Kekule.PNG", "img\\Petroleo.PNG", "img\\Plásticos.PNG", "img\\Uréia.PNG", "img\\Wholer.PNG"]

execucao = True

while execucao:
    for imagem in imglist:
        localimg = pyautogui.locateOnScreen(imagem)
        if localimg != None:
            pyautogui.click(localimg[0], localimg[1])
            continue
        else:
            continue