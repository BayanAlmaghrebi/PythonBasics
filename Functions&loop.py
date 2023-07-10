

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
