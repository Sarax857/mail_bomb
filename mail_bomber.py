import smtplib
from threading import Thread
m = input("own mail adress :  ")
p = input("own password : ")
a = input("target mail : ")


content = input("enter message : ")
mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login(m,p)
while True:
    mail.sendmail(m,a,content)
    t = Thread(target = mail.sendmail, args = (mail.login,))
    t.start
    print("mail sended")
