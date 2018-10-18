it = (x for x in open('my_file.txt'))
print(it)

while True:
    try:
        print(next(it))
    except:
        break
print('done!')
