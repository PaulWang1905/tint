#This is my shopping list
shoplist = ['apple','mango','carrot','banana']
print('I have ', len(shoplist),'items to purchase.')
print('These items are:', end='')
for item in shoplist:
    print(item,end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)
print('Now I have ',len(shoplist),'items to purchase.')
print('These items are:',end=' ')
for item in shoplist: 
    print(item,end= ' ')
for item in shoplist:
    print('\nNow I will buy ',item)
    olditem = item
    del item 
    #shoplist.sort
    print('I bought the ', olditem)
    continue
print('I got everything!They are ', shoplist)




