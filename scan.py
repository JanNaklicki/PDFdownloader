import pyautogui
import time
name = 'image'
print('Podaj Ilosc stron')
N = int(input())

for i in range(5,0,-1):
    print(i)
    time.sleep(1)
print('Start!')
time.sleep(1)

for i in range(N):
    pom = name+str(i)+'.png'
    im = pyautogui.screenshot(pom,region=(621,3, 678, 1040))
    pyautogui.press('right')
    time.sleep(1)

print('Scanning done!')

