# http://www.pythonchallenge.com/pc/def/oxygen.html
from PIL import Image

img  = Image.open('solve/7.png')

img = img.convert('L')

for x in range(img.size[0]):
    s = chr(img.getpixel((x, img.size[1] // 2)))
    print(s, end='')

print()

m = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for n in m:
    print(chr(n), end='')
