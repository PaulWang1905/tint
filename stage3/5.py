a = ['a','b','c','d','e','f','g','h']
print('First four:', a[:4])
print('Last four:',a[-4:])
print('Middle two:',a[3:-3])
print('Overload',a[:20])
b = a[4:]
print('Before:    ',b)
b[1] = 99 
print('After:',b)
print('no change:',a)
