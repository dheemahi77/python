import re
"help(re)"
text="this is the text i am giving to test these regular expressions 1 to 2026 using these ****"
'''r=re.match("this",text)#match
print(r)
print(r.group())# this 
print(r.span())#index 0 to 4
print(r.start())
print(r.end())'''

#search
r=re.search("these",text)
print(r)
print(r.group()) 
print(r.span())
print(r.start())
print(r.end())

#findall
r=re.findall("these",text)
print(r)#how many times in word in variable
 
#finditer

r=list(re.finditer("these",text))
print(r)#how many times in same word and display index for both

for i in re.finditer("these",text):
    print(i.span())
    print(i.group())
    print(i.start())
    print(i.end())
    
# sub
r=re.sub("these","python",text)
print(r)#change value replaced in python
r1=re.subn("python","java",r)
print(r1)#change the word and display the count how many times we change





import re
text="my name is Dheemahi I am from repalle"
r=re.match("my",text)
print(r)
print(r.group())
print(r.span())
print(r.start())
print(r.end())
r=re.search("from",text)
