Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l = [1,2,3,4,5,6]
l[0]
1
l[-1]
6
l[-2]
5

l[0:3]
[1, 2, 3]
l[4:]
[5, 6]
l[:3]
[1, 2, 3]
l.append(1000)
l
[1, 2, 3, 4, 5, 6, 1000]
l.insert(0,199)
l
[199, 1, 2, 3, 4, 5, 6, 1000]
l.insert(0,100)
l
[100, 199, 1, 2, 3, 4, 5, 6, 1000]
l.sort()
l
[1, 2, 3, 4, 5, 6, 100, 199, 1000]
l.sort(reservse=True)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l.sort(reservse=True)
TypeError: 'reservse' is an invalid keyword argument for sort()
l.sort(reverse=True)
l
[1000, 199, 100, 6, 5, 4, 3, 2, 1]
l.sort()
l.reverse()
l
[1000, 199, 100, 6, 5, 4, 3, 2, 1]

min(l)
1
max(l)
1000

l.remove(1000)
l
[199, 100, 6, 5, 4, 3, 2, 1]

l[0]
199
l[0]=500
l
[500, 100, 6, 5, 4, 3, 2, 1]


t = (1,2,3,4,5,6,True)
min(t)
1
max(t)
6

l.remove(1000)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    l.remove(1000)
ValueError: list.remove(x): x not in list
d = {'ahmed':70 , 'ali':80}
d['ali']
80
d['ali'] = 90
d
{'ahmed': 70, 'ali': 90}

d.keys()
dict_keys(['ahmed', 'ali'])
d.values()
dict_values([70, 90])
d.items()
dict_items([('ahmed', 70), ('ali', 90)])

= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
ahmed
ali

= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
Traceback (most recent call last):
  File "C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py", line 3, in <module>
    for x in d.values:
TypeError: 'builtin_function_or_method' object is not iterable

= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
70
80

= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
ahmed 70
ali 80
d = {'ahmed':70 , 'ali':80}



x = 'mahmoud'
x.upper()
'MAHMOUD'
x.lower()
'mahmoud'

type(x)
<class 'str'>

= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
Traceback (most recent call last):
  File "C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py", line 10, in <module>
    c1 = Calc()
NameError: name 'Calc' is not defined. Did you mean: 'calc'?

= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
15
45

= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
15
200

= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
welcome
15
200

= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
Traceback (most recent call last):
  File "C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py", line 16, in <module>
    c1 = Calc('ahmed')
TypeError: Calc.__init__() takes 1 positional argument but 2 were given

= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
Traceback (most recent call last):
  File "C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py", line 16, in <module>
    c1 = Calc('ahmed')
TypeError: Calc.__init__() takes 1 positional argument but 2 were given

= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
welcome ahmed

= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
7
12
Traceback (most recent call last):
  File "C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py", line 29, in <module>
    s.power(3.4)
TypeError: SciCalc.power() missing 1 required positional argument: 'y'

= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
7
12
Traceback (most recent call last):
  File "C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py", line 27, in <module>
    s.power(3.4)
TypeError: SciCalc.power() missing 1 required positional argument: 'y'
>>> 
= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
7
12
81
>>> 
= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
7
12
81
>>> 
= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
welcome
7
12
81
>>> 
= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
Traceback (most recent call last):
  File "C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py", line 21, in <module>
    s = SciCalc('ahmed')
TypeError: Calc.__init__() takes 1 positional argument but 2 were given
>>> 
= RESTART: C:/Users/bayan/Desktop/my codes/python Basics/Functions&loop.py
welcome ahmed
7
12
81
