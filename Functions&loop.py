
'''
class Calc:
    def __init__(self,name):
        print(f'welcome {name}')

    
    def mysum(self,x,y):
        print(x+y)


    def mymul(self,x,y):
        print(x*y)


class SciCalc(Calc):

    def power(self,x,y):
        print(x**y)

s = SciCalc('ahmed')

s.mysum(3,4)
s.mymul(3,4)
s.power(3,4)
'''






'''
class A:
    def do(self):
        print('in A')


class B(A):
    pass

class C:
    def do(self):
        print('in C')


class D(C,B):
    pass

j=D()
j.do()

'''






# encapsulation : self
# inheritance 
# polymorphism
# abstraction

'''

class str :
    def len


class list:
    def len


class tuple:
    def len
'''


'''
class Calc # main  super  parent


class SciCalc(Calc) #derived  sub  Child
'''







class Calc:


    total = 0    # class value

    def sum(self,x,y):
        print(x+y)





c = Calc()
print(c.total)


c.total = 100      # instance=object value
print(c.total)


del c.total
print(c.total)

del c.total
print(c.total)




#c.sum(3,4)










































































