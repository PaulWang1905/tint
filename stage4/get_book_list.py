file_name = 'all.txt'
output = open('all_books_url_name.txt',"w+",encoding='utf8')


def get_name(self):
    f =  open(self,'r',encoding='utf8')
    i = 0 
    for line in f:
        
        if '<li class="title"><span>' in line:
            i = i + 1
            names = line.split('<')
            names = names[3]
            names = names.split('>')
            names[0] = names[0][8:]
            names[0] = names[0][:-1]
            print(names[0])
            print(names[1])
            print(i)
            output.write(names[0])
            output.write('\n')

            output.write(names[1])
            output.write('\n')







get_name(file_name)

