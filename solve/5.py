# http://www.pythonchallenge.com/pc/def/peak.html
import pickle

trans_str = b''
with open('solve/5.txt', 'rb') as f:
    for line in f.readlines():
        trans_str += (line.decode().strip() + '\n').encode()

data = pickle.loads(trans_str)

for i in data:
    s = ''
    for x in i:
        s += x[0] * x[1]
    print(s)