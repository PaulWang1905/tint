import time
class Person:
    def say_hi(self):
        print('Hello, how are you?')
    def answer(self):
        print('It is Paul saying hello to the world')
p = Person()
p.say_hi()
#The previous 2 line can also be written as
#Person().say_hi()
class Who:
    def ask_who(self):
        print('Who is saying hello?')
q = Who()
time.sleep(5)
q.ask_who()
time.sleep(5)
p.answer()
