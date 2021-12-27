# http://www.pythonchallenge.com/pc/def/channel.html
import re
import zipfile

zip_file = zipfile.ZipFile('solve/6.zip')

start_file = '90052.txt'
bs = b''
while True:
    try:
        with zip_file.open(start_file, 'r') as f:
            data = f.read().decode()
            info = zip_file.getinfo(start_file)
            bs += info.comment
            regexp = re.compile('([0-9]+)')
            start_file = '{}.txt'.format(regexp.search(data).group(1))
    except AttributeError:
        print(bs.decode())
        break
