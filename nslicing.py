Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
20^12<<2
36

14&14<<3
0
25&14<<3
16

x="codegnan"
x[-8::1]
'codegnan'
x[-8::2]
'cdga'

x[-8::3]
'cea'
x[-8::4]
'cg'


============================ RESTART: D:/slicing.py ============================

============================ RESTART: D:/slicing.py ============================

============================ RESTART: D:/slicing.py ============================
y="codegnan"
y[-8::1]
y[-8::2]
y[-8::3]
y[-8::4]
y[4:8:1]

SyntaxError: multiple statements found while compiling a single statement
y="codegnan"
y[-8::1]
... y[-8::2]
... y[-8::3]
... y[-8::4]
... y[4:8:1]
SyntaxError: multiple statements found while compiling a single statement
>>> y="codegnan"
>>> y[4:8:1]
'gnan'
>>> y[7:0:2]
''
>>> y[8:1:2]
''
>>> y[8:1:2]
''
>>> print(y[8:1:2])

>>> s="nothing is imposible"
... s.upper()
... s.lower()
... s.title()
... s.capitalize()
... s.swapcase()
SyntaxError: multiple statements found while compiling a single statement
>>> s
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s
NameError: name 's' is not defined
