import os
def getFile():
    a = os.listdir()
    b = []
    for text in a:
        if ('.' in text) or ('_' in text):
            #b.append(text)
            print('Skip ',text)
        else:
            print('add ', text)
            b.append(text)
    return b

