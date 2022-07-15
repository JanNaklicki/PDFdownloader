import time
import mss
import mss.tools
import pyautogui
from win32api import GetSystemMetrics

name = 'image'
print('Podaj Ilosc stron')
N = int(input())
region = {'top': int(0.002*GetSystemMetrics(1)), 'left': int(0.323*GetSystemMetrics(0)), 'width': int(0.353*GetSystemMetrics(0)), 'height': int(0.963*GetSystemMetrics(1))}

for i in range(5,0,-1):
    print(i)
    time.sleep(0.5)
    
def skanuj():
    with mss.mss() as sct:        
        pom = name+str(i)+'.png'
        im = sct.grab(region)
        sct.compression_level = 1
        png = mss.tools.to_png(im.rgb,im.size,output=pom)
        
        
for i in range(N):
    skanuj()
    time.sleep(1)
    pyautogui.press('right')


print('Scanning done!')

