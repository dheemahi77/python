'''import os
print(os.getcwd())
# file=open("just3.txt",mode="x")
# file.write("Hello how are you")
# print("success")
# file.close()

file=open("just3.txt",mode="r")
print(file.read())

print(file.read())
print(file.readline())

data=file.readlines()
for i in data:
    print(i)
file.close()'''


'''file=open("ready","w")#create a ready file and update the data
file.write("this updated data")
print("success")
file.close()'''


'''file=open("ready","w")
file.write("\n hello how are you")
print("success")
file.close()'''

'''file=open("ready","w")
file.write("\n john and johnson")
print("success")
file.close()'''

'''file=open("data.csv","w+")
file.write("name,age,marks")
file.write("john,21,70")
print(file.read())
print("success")
file.close()'''


# file=open("info.txt","x")
# print("success")
# file.close()

'''file=open("info.txt","a")
name="john"
age=32;marks=456
file.seek(0,0)
file.write(f"\n{name:<20}{age:}{marks:>15}")

print("success")
file.close()'''

import smtplib

from email.mime.text import MIMEText
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

username="viswanadhapallidheemahi.97@gmail.com"
password="jcbnnobgskpeqgjm"

server.login(username,password)
To=["ganginenilakshminagachandrika@gmail.com","saranyadondapati75@gmail.com","dheemahiviswanadhapalli.97@gmail.com"]

subject="sending mail"
message="hello chandrika\n hi chandrika"

for m in To:
    msg=MIMEText(message)
    msg["from"]=username
    msg["to"]=m
    msg["subject"]=subject
    server.sendmail(username,m,msg.as_string())
    print(f"success sent to{m}")
server.quit()