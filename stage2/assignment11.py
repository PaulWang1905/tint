import re

name = input('Enter File Name:')
handle = open(name)
total = 0
for line in handle:
    x = line
    y = re.findall('[0-9]+',x)
    for number in y:
        number = int(number)
        total += number
print(total)       

