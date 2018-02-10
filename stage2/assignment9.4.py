'''

9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
book=dict()
lst =list()
for line in handle :
    line =line. rstrip()
    if line.startswith('From '):
        lst = line.split()
        book[lst[1]] = book.get(lst[1],0) + 1
big = 0
bigman = None
for key in book:
    if book[key] > big:
        big = book[key]
        bigman= key
print(bigman,big)

    
