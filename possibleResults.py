import pyautogui
from time import sleep
from PIL import ImageGrab
import keyboard

pyautogui.PAUSE = 0.00001
pixels = []
def Point(x,y,c):
    return x, y, c
closePoint = [Point(x=1213, y=865,c="Delpoint"), Point(x=1025, y= 334,c="ColourSpot")]
points = [Point(x=712, y=868, c="White"), Point(x=795, y=862, c="Tan"), Point(x=865, y=862, c="Yellow"), Point(x=926, y=869, c="Orange"), Point(x=972, y=864, c="Brown"), Point(x=1048, y=856, c="Magenta"), Point(x=1112, y=855, c="Maroon"), Point(x=720, y=923, c="Light Blue"), Point(x=793, y=923, c="Light Green"), Point(x=858, y=923,c="Lime"), Point(x=926, y=923,c="Green"), Point(x=1010, y=924,c="Barf green"), Point(x=1055, y=927,c="Cyan"), Point(x=752, y=997,c="Pink"), Point(x=829, y=997, c="Light purple"), Point(x=899, y=997, c="Deep pink"), Point(x=953, y=995,c="Purple"), Point(x=1034, y=994,c="Blue"), Point(x=1101, y=996,c="Navy"), Point(x=1153, y=999,c="Black")]
try:
    with open('possibleColours.txt','w') as outFile:
        for e in points:
            pyautogui.moveTo(e[0],e[1])
            pyautogui.leftClick()
            for g in points:
                it = False
                pyautogui.moveTo(g[0],g[1])
                pyautogui.leftClick()
                for y in points:
                    if e != g and y != g and e != y:
                        if keyboard.is_pressed("="):
                            raise ValueError("done")
                        pyautogui.moveTo(y[0],y[1])
                        pyautogui.leftClick()
                        px = ImageGrab.grab().load()
                        targetColor = px[closePoint[1][0],closePoint[1][1]]
                        outFile.write(str([e[2],g[2],y[2],targetColor]))
                        outFile.write("\n")
                        pyautogui.moveTo(closePoint[0][0],closePoint[0][1])
                        pyautogui.click()
                        it = True
                if it == True:
                    pyautogui.moveTo(closePoint[0][0],closePoint[0][1])
                    pyautogui.click()
            pyautogui.moveTo(closePoint[0][0],closePoint[0][1])
            pyautogui.click()        
except:
    outFile.close()
    print("Ended forcefully")
    print(pixels)
