import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls

username="viswanadhapallidheemahi.97@gmail.com"
password="jcbnnobgskpeqgjm"

server.login(username,password)
To="saranyadondapati75@gmail.com"
subject="sending documents using python"
message=f"Hello {To} i have forwarded the document"

msg=MIMEMultipart()
msg["to"]=To
msg["subject"]=subject
msg.attach(MIMEText(message))
filename=r"C:\Users\HP\Downloads\WhatsApp Image 2026-05-27 at 9.14.20 PM.jpeg"
attachement=open(filename,"rb")

part=MIMEBase("application","octet-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)

part.add_header("content-Disposition",f"attachement;filename='{filename}'")

mag.attach(part)
server.sendmail(username,To,msg.as_string())
print("success")
server.quit()


