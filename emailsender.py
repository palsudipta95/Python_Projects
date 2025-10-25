import smtplib

to = input("Enter recipient email address: ")

content = input("Enter email content:\n")

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('palsudipta2003@gamil.com', 'app_password')
    server.sendmail('palsudipta2003@gamil.com', to, content)
    server.close()

send_email(to, content)