Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> x=pd.DataFrame({'rollno':[101,102,103],'name':['priya','riya','siya']},index=[0,1,2],columns=("rollno","name"))
>>> print(x)
   rollno   name
0     101  priya
1     102   riya
2     103   siya
>>> x.head(2)
   rollno   name
0     101  priya
1     102   riya
>>> x.discribe()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x.discribe()
  File "C:\Users\hp\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\generic.py", line 6321, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'discribe'. Did you mean: 'describe'?
>>> x.describe()
       rollno
count     3.0
mean    102.0
std       1.0
min     101.0
25%     101.5
50%     102.0
75%     102.5
max     103.0
>>> x.tail(2)
   rollno  name
1     102  riya
2     103  siya
>>> x={'rollno':[101,102,103],'name':['siya','priya','riya']}
>>> type(x)
<class 'dict'>
