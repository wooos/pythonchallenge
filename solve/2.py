# http://www.pythonchallenge.com/pc/def/ocr.html

char_count = 0
chars = {}

with open('solve/2.txt', 'r') as f:
    for line in f.readlines():
        char_count += len(line.strip())
        for char in line.strip():
            chars[char] = chars.get(char, 0) + 1

char_avg = char_count / len(chars)

dest_str = ''
for char in chars:
    if chars[char] < char_avg:
        dest_str += char

print(dest_str)
