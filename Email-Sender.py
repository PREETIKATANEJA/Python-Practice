
# E-Mail sender

import smtplib

to = input("Enter the email of reciepient: \n ")
content = input("Enter the content of the email")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com', 'passwordOfSender')
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()
    
    
sendEmail(to, content)
