x = 50

def func(x):
   print('x is',x)
   x = 2
   print('changed local x',x)
   print('now x is' ,x)
func(x)
print('x is still ',x)

