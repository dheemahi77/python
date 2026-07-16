import os

print(os.getcwd()) #get current working directer
print(os.chdir('/Users/kasis/Desktop/codegnan/'))#to change the directer

# print(os.mkdir("puple"))
# print(os.rename("hello","puple/hello"))##folder/subfolder
# print(dir(os.getcwd()))#list all the files in the directery
print(os.listdir()) #list the files in the dir

fd = os.open("sample.txt",os.O_CREAT | os.O_WRONLY)#to create file os.O_CREAT/

print(os.getcwd())
with open("sample.txt", "w") as file:#to open the file
    file.write("Hello World")# to create the file in the text
    
fd = os.open("sample.txt", os.O_RDONLY)#to read the file
data = os.read(fd, 100)#this line is to read the data bytes in the file 
print(data)