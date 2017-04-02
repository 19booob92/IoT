import smtplib

USER = 'webtestkonto2015@gmail.com'
PASS = 'samolot123'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def send_email(recipient, subject, text):
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(USER, PASS)
    header = 'Do:' + recipient + '\n' + 'Od: ' + USER
    header = header + '\n' + 'Temat:' + subject + '\n'
    msg = header + '\n' + text + ' \n\n'
    smtpserver.sendmail(USER, recipient, msg)
    smtpserver.close()

send_email('19mateusz92@gmail.com', 'test', 'test')