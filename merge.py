from PIL import Image
import pathlib


name = 'image'
tab = []
# path = pathlib.Path(__file__).parent.resolve()+"\image0.png"
path = ".\image0.png"

print(path)
print('Podaj Ilosc stron')
N = int(input())
print('Jak nazwac plik pdf?')
fileName = str(input())


image1 = Image.open(path)
im1 = image1.convert('RGB')
for i in range(1,N):
    # path = str(pathlib.Path(__file__).parent.resolve())+"\\"+ str(name)+str(i)+".png"
    path = "."+"\\"+name + str(i)+".png"

    pom = Image.open(path)
    pomRGB = pom.convert('RGB')
    tab.append(pomRGB)
print()
# print(str(pathlib.Path(__file__).parent.resolve())+"\\"+ fileName+".pdf")
im1.save("."+"\\"+ fileName+".pdf",save_all=True, append_images=tab)
print()
input("Aby zakonczyc nacisnij enter")
