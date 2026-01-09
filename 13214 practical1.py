Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#first program
x=[10,20,30,40]
x.insert(2,25)
print(x)
[10, 20, 25, 30, 40]
#second program
p={}
print(type(p))
<class 'dict'>

# third program
x=set()
print(x)
set()
>>> 
>>> #fourth program
>>> product ={"pid":101,"pname":"swamini"}
>>> product["prize"]=200
>>> print(product)
{'pid': 101, 'pname': 'swamini', 'prize': 200}
>>> 
>>> # fifth program
>>> a=(4,5,7,20)
>>> b=list(a)
>>> b.append(20)
>>> a=tuple(b)
>>> print(a)
(4, 5, 7, 20, 20)
>>> 
>>> 
>>> #numpy program
>>> import numpy as np
>>> x1=np.zeros((3,4))
>>> print(x1)
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
>>> 
>>> x2=np.ones((3,5))
>>> print(x2)
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
>>> 
>>> x3=np.full((2,3),7)
>>> print(x3)
[[7 7 7]
 [7 7 7]]
>>> 
>>> x4=np.eye(3)
>>> print(x4)
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
