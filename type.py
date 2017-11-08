#class Hello():
def fn(self, name='world'):
    print('Hello,%s'% name)
Hello = type('Hello',(object,),dict(say_hello=fn))



hello = Hello()

hello.say_hello()
class SayMetaClass(type):

    def __new__(cls,name,bases,attrs):
        attrs['say_'+name] = lambda self,value,saying = name:print(saying+','+value+'!')
        return type.__new__(cls,name,bases,attrs)
class Hello(object,metaclass=SayMetaClass):
    pass
hello.say_hello('Puyu')

