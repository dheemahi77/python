Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=5
print(a+b)
15
a
10
b
5
print(a%b)
0
print(a/b)
2.0
print(a>b)
True
print(a<b)
False
print(a==b)
False
print(a>=b)
True
print(a!=b)
True
a&b
0
a^b
15
a+10
20
b+2
7
a=True
type(a)
<class 'bool'>
a+2
3
a//b
0
10//b
2
a/b
0.2
a=5
b=3
a/b
1.6666666666666667
a//b
1
type(a)
<class 'int'>
a and b
3
a or b
5
a not b
SyntaxError: incomplete input
a not a
SyntaxError: incomplete input
a%b
2
a%=b
a
2
a!=b
True
a==b
False
a+=b
a
5
a-=b
a
2
a=25
b=22
a&b
16
a|b
31
a>b and a<b
False
10>20
False
20>10
True
age=20
age
20
age>25
False
age<12
False
age>13
True
10==10
True
10!=10
False
10>=10
True
10<=10
True
x='a'
y='b'
x>b
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    x>b
TypeError: '>' not supported between instances of 'str' and 'int'
x>y
False
X>y
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    X>y
NameError: name 'X' is not defined. Did you mean: 'x'?
20>20.0
False
20>20.1
False
20<=20.1
True
20>20
False
20>=20
True
24>25
False
24>=27
False
24>=24
True
24>24.1
False
24>24.5
False
a~b
SyntaxError: invalid syntax
20<1>2
False
20>3>8
False
24>23>45>1
False
27>34>23<7
False
7>2>4>23<23
False

age=20:name="mahi"
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: incomplete input
age=20;name="mahi"
age
20
name
'mahi'
age>15 and name="mahi"
SyntaxError: cannot assign to expression
age>15 and name=="mahi"
True
age>=15 and name=="mahi"
True
age>=21 and name="mahi"
SyntaxError: cannot assign to expression
age>=21 and name=="mahi"
False
ticket=200; bike="royal enfeild"
ticket=="yes" and bike=="yes"
False
ticket=200; bike="royal enfeild"
ticket=200 and bike="royal enfeild"
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
ticket==200 and bike=="royal enfeild"
True
pen="blue";pen="black"
pen="blue or pen="black"
SyntaxError: unterminated string literal (detected at line 1)
pen=="blue or pen=="black"
SyntaxError: unterminated string literal (detected at line 1)
pen=="blue" or pen=="black"
True
pen=="blue" or pen==""
False
travel="bus" or travel=="train"
test="scam"
test=="scam" or test=="genuine"
True
>>> not(true)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    not(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> not(True)
False
>>> not(False)
True
>>> soap="medimix"
>>> soap="santoor"
>>> soap=="medimix" soap="santoor"
SyntaxError: invalid syntax
>>> soap=="medimix" soap=="santoor"
SyntaxError: invalid syntax
>>> soap="medimix";shampoo="meera"
>>> soap="medimix" and shampoo="meera"
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> soap=="medimix" and shampoo=="meera"
True
>>> soap="santoor"
>>> soap="santoor" or shampoo=""
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> soap="santoor"soap="santoor" or shampoo=""
SyntaxError: invalid syntax
>>> soap=="santoor" or shampoo==""
True
>>> 
