Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=10
x
10
bin(10)
'0b1010'
'
bin(3)
'0b11'
n="11"
print(int(n,2))
3
print(int("1010",2))
10
10<<3
80
37>>3
4
oct(7)
'0o7'
oct(18)
'0o22'
oct(98)
'0o142'
print(int("142",8))
98

oct(8)
'0o10'
print(int("10",8))
8
oct(13)
'0o15'
>>> print(int("13",8))
11
>>> hex(10)
'0xa'
>>> print(int("a",16))
10
>>> hex(22)
'0x16'
>>> print("16",16))
SyntaxError: unmatched ')'
>>> print(nt("16",16))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(nt("16",16))
NameError: name 'nt' is not defined. Did you mean: 'n'? Or did you forget to import 'nt'?
>>> print(int("16",16))
22
>>> ~10
-11
>>> bin(17)
'0b10001'
>>> ~17
-18
>>> bin(18)
'0b10010'
>>> ~18
-19
