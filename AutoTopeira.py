import pyautogui
import threading
from time import sleep

imglist = ["img\\Alquimistas.PNG", "img\\Benzeno.PNG", "img\\Carbono.PNG", "img\\Fogo.PNG", "img\\Joaquim.PNG", "img\\Kekule.PNG", "img\\Petroleo.PNG","img\\Wholer.PNG", "img\\Grana.png","img\\Plastico.png", "img\\Ureia.png", "img\\estrela.png", "img\\Tempo.png"]

def findAlquimista():
    while 1:
        localimg = pyautogui.locateOnScreen(imglist[0], confidence=.6)
        if localimg != None:
            pyautogui.click(localimg[0], localimg[1])
            sleep(.1)
            continue
        else:
            continue

def findBenzeno():
    while 1:
        localimg = pyautogui.locateOnScreen(imglist[1], confidence=.6)
        if localimg != None:
            pyautogui.click(localimg[0], localimg[1])
            sleep(.1)
            continue
        else:
            continue

def findCarbono():
    while 1:
        localimg = pyautogui.locateOnScreen(imglist[2], confidence=.6)
        if localimg != None:
            pyautogui.click(localimg[0], localimg[1])
            sleep(.1)
            continue
        else:
            continue

def findFogo():
    while 1:
        localimg = pyautogui.locateOnScreen(imglist[3], confidence=.6)
        if localimg != None:
            pyautogui.click(localimg[0], localimg[1])
            sleep(.1)
            continue
        else:
            continue

def findJoaquim():
    while 1:
        localimg = pyautogui.locateOnScreen(imglist[4], confidence=.6)
        if localimg != None:
            pyautogui.click(localimg[0], localimg[1])
            sleep(.1)
            continue
        else:
            continue

def findKekule():
    while 1:
        localimg = pyautogui.locateOnScreen(imglist[5], confidence=.6)
        if localimg != None:
            pyautogui.click(localimg[0], localimg[1])
            sleep(.1)
            continue
        else:
            continue

def findPetroleo():
    while 1:
        localimg = pyautogui.locateOnScreen(imglist[6], confidence=.6)
        if localimg != None:
            pyautogui.click(localimg[0], localimg[1])
            sleep(.1)
            continue
        else:
            continue

def findWholer():
    while 1:
        localimg = pyautogui.locateOnScreen(imglist[7], confidence=.6)
        if localimg != None:
            pyautogui.click(localimg[0], localimg[1])
            sleep(.1)
            continue
        else:
            continue

def findGrana():
    while 1:
        localimg = pyautogui.locateOnScreen(imglist[8], confidence=.6)
        if localimg != None:
            pyautogui.click(localimg[0], localimg[1])
            sleep(.1)
            continue
        else:
            continue

def findPlastico():
    while 1:
        localimg = pyautogui.locateOnScreen(imglist[9], confidence=.6)
        if localimg != None:
            pyautogui.click(localimg[0], localimg[1])
            sleep(.1)
            continue
        else:
            continue

def findUreia():
    while 1:
        localimg = pyautogui.locateOnScreen(imglist[10], confidence=.6)
        if localimg != None:
            pyautogui.click(localimg[0], localimg[1])
            sleep(.1)
            continue
        else:
            continue

def findTempo():
    while 1:
        localimg = pyautogui.locateOnScreen(imglist[11], confidence=.6)
        if localimg != None:
            pyautogui.click(localimg[0], localimg[1])
            sleep(.1)
            continue
        else:
            continue

t1 = threading.Thread(target=findAlquimista)
t2 = threading.Thread(target=findBenzeno)
t3 = threading.Thread(target=findCarbono)
t4 = threading.Thread(target=findFogo)
t5 = threading.Thread(target=findJoaquim)
t6 = threading.Thread(target=findKekule)
t7 = threading.Thread(target=findPetroleo)
t8 = threading.Thread(target=findWholer)
t9 = threading.Thread(target=findGrana)
t10 = threading.Thread(target=findPlastico)
t11 = threading.Thread(target=findUreia)
t12 = threading.Thread(target=findTempo)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()