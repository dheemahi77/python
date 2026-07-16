Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> email="no"
>>> phone="yes"
>>> email=="no" and phone=="yes"
True
>>> email=""
>>> phone="yes"
>>> email=="" and phone=="yes"
True
>>> email=""phone="yes"email=="" and phone=="yes"
SyntaxError: invalid syntax
>>> email=""
>>> phone="yes"
>>> email=="" or phone=="yes"
True
>>> email
''
>>> phone="yes"
>>> email=="" and phone="yes"
SyntaxError: cannot assign to expression
>>> email=="" and phone=="yes"
True
