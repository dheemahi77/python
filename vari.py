Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
a
10
name="mahi"
name
'mahi'
a=10
b=20
print(b,a)
20 10
x=y=z=codegnan
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x=y=z=codegnan
NameError: name 'codegnan' is not defined
x=y=z="codegnan"
x
'codegnan'
y
'codegnan'
z
'codegnan'
d=2+5j
type(d)
<class 'complex'>
type(a)
<class 'int'>
<class 'int'>
SyntaxError: invalid syntax
<class 'int'>d.real
SyntaxError: invalid syntax
SyntaxError: invalid syntaxd.real
SyntaxError: invalid syntax

=========================== RESTART: D:/variables.py ===========================
10 20 0.7 False mahi

=========================== RESTART: D:/variables.py ===========================
10 20 0.7 False mahi
10 20 0.7 False mahi
SyntaxError: invalid syntax
10 20 0.7 False mahi
SyntaxError: invalid syntax
number=200
str(number)
'200'
int(number)
200
float(number)
200.0
bool(number)
True
complex(number)
(200+0j)
number=0.7
str(number)
'0.7'
>>> complex(number)
(0.7+0j)
>>> bool(number)
True
>>> number=-0.7
>>> bool(number)
True
>>> s="data"
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'data'
>>> s="123456"
>>> float(s)
123456.0
>>> s.real
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s.real
AttributeError: 'str' object has no attribute 'real'
>>> b=20
>>> b.real
20
>>> c=0.1
>>> c.real
0.1
