import getFile
import re
import os
import random  
from time import sleep
book_list = getFile.getFile()
downloaded_book = open('DownloadedBook.txt',"a",encoding='utf8')
def get_title(self):
    for line in self:
        if '<li class="title"><span><a>' in line:
            name = line.replace('<li class="title"><span><a>','')
            name = name.replace('</a></span></li>','')
            name = remove_characters(name)
    return name

def remove_characters(self):
    name = self
    name = name.strip()
    name = name.replace(' ','_')
    name = re.sub('[\/:*?"<>|]','',name)
    name = name.replace("'","")
    name = re.sub('[()]','',name)
    return name

def make_dir(self):
    if os.path.isdir(self):
        print(self,' is already created.')
    else:
        os.mkdir(self)
    return

def download_to_dir(chapter_link,chapter_name,book_dir):
    cmd = 'wget -retries=10 -c' + ' -O ' + book_dir + chapter_name + ' ' + chapter_link 
    os.system(cmd)
    print(cmd)
    print('    Downloaded chapter: ',chapter_name)
    num = round(random.uniform(30,60),2)
    print('sleeping for ', num)
    sleep(num)
    return
    


def get_chapter(self):
    for line in self:
        if ('<li class="title"><span>' in line) and ('href' in line):
            name = line.strip()
            name = name.replace('<li class="title"><span>','')
            name = name.replace('</a></span></li>','')
            name = name.replace('<em>','')
            name = name.replace('</em>','')

            link_and_name = name.split('>')
            link =  link_and_name[0]
            link = link.replace('"','')
            link = link.replace('<a href=','')
            
            link = "https://muse.jhu.edu" + link +'/pdf'
            
            name = link_and_name[1]
            name = remove_characters(name)
            name = name +'.pdf'
            
            download_to_dir(link,name,book_dir)

            





i = 0

for book in book_list:
    
    if i < 2 :

        input_html = open(book,"r",encoding='utf8')
        input_chapter = open(book,"r",encoding='utf8')
        
        book_name = get_title(input_html)
        book_dir = '/mnt/c/Users/paulw/Desktop/MuseProject/music/booklist/'+book_name+'/'
        
        print('\n')
        print('Downloading book:' + ' ' + book_name+'\n')
        
        message = book+' '+book_name+'\n'
        downloaded_book.write(message)

        make_dir(book_dir)
        get_chapter(input_chapter)


        i = i + 1
    else:
        print('You already downloaded ',i,'books.\n')
        txt = input('Type any key to continue.\n')
        i = 0
        



    #print(i)





