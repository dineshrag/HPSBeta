import smtplib

import config


def send_email(subject, msg):

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()



subject = "Test subject"
msg = "Hello there, how are you today?"

send_email(subject, msg)