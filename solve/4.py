# http://www.pythonchallenge.com/pc/def/linkedlist.html
import re
import requests

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

for i in range(400):
    response = requests.get(url=url)
    try:
        if response.text == 'Yes. Divide by two and keep going.':
            result = result / 2
        else:
            regexp = re.compile('next nothing is ([0-9]+)')
            result = int(regexp.search(response.text).group(1))
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(result)
    except AttributeError:
        print(response.text)
