# http://www.pythonchallenge.com/pc/def/equality.html
import re


with open('solve/3.txt', 'r') as f:
    data = f.read()

regexp = re.compile('[^A-Z][A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]{1}')

res = regexp.findall(data)

print(''.join(res))
