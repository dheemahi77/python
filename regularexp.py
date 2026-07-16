'''import re
help(re)
text="this is the text i am giving to test these regular expressions 1 to 2026 using these ****"
pattern="[A-Za-z\d]+"#print all text #A-Za-z\s print only text and devide the ',' i numbers [A-Za-z\d\s] remove nums spaces letters remaining prints
result=re.findall(pattern,text)
print(result)
print()


pattern="\d+"#"[0-9]+"#numbers
number=re.findall(pattern,text)
print(number)
print()


pattern="[^\w\s]+"#"[0-9]+"#remove spaces and print special cahracters
symbols=re.findall(pattern,text)
print(symbols)

pattern=r"\w"
symbols=re.findall(pattern,text)
print(symbols)'''


#form validation
'''import re
#help(re)
text1=input()
pattern=r"[A-Za-z]+"
if re.fullmatch(pattern,text1):
    print(text1.capitalize())
else:
    print("Invalid")'''

'''import re #number
text2=input()
pattern=r"[9876][0-9]{9}#only using for starts the value9876" #r"\d\d{9} #r"^[6789]\d{9}"
if re.fullmatch(pattern,text2):
    print("valid")
else:
    print("Invalid")'''

'''import re
text3=input()#adhar
pattern=r"\d{12}"
if re.fullmatch(pattern,text3):
    print("valid")
else:
    print("invalid")'''

'''import re
text3=input()#pan
pattern=r"[A-Z0-9]{10}"
if re.fullmatch(pattern,text3):
    print("valid")
else:
    print("invalid")'''


'''import re
text=input()
#pattern=r"[a-z]+@gmail\.com"
pattern=r"[a-z0-9]+@[a-z]+\.[a-z]*"
if re.fullmatch(pattern,text):
    print("valid")
else:
    print("not valid")'''


import re
text=input()
#pattern=r"[A-Za-z0-9!@#$%^&*_]{8,15}"
pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,15}"
if re.fullmatch(pattern,text):
    print("valid")
else:
    print("Invaild")
    
    





