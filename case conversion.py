#string methods

#case conversion
s="nothing is imposible"
s
'nothing is imposible'
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())

#type checking
g="PhotoGRapHy"
f="abc def ghi jkl"
i="bad2ab5ada6"
print(g.swapcase())
t="12345"
print(g.isalpha())
print(t.isdigit())
print(g.isdigit())
print(g.islower())
print(g.isupper())
print(g.istitle())
print(f.isalpha())
print(i.isalnum())
print(f.isnumeric())
print(t.isnumeric())
print(t.isdecimal())
print(g.isprintable())

#searching
x="Dheemahi"
print(x.find("e"))
print(x.rfind("e"))
print(x.index("Dhee"))
print(x.count("i"))

email="abc@gmail.com"
print(email.endswith("gmail.com"))
print(email.startswith("gmail.com"))

#modification methods
word="                     matter enti anna                     "
print(word)
print(word.rstrip())
print(word.lstrip())
print(word.strip())
print(word.replace("anna","thammudu"))
      
