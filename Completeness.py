import datetime
import cv2
import numpy as np
import time
import config
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders


currentDT = datetime.datetime.now()
print (str(currentDT))
print (currentDT.strftime("%I:%M:%S %p"))

capturedvideo = ''

def record_Video(timeout):
    cap = cv2.VideoCapture(1)
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    capturedvideo = './Videos/output'+str(currentDT.strftime("%I%M%S%p"))+ '.mp4'
    out = cv2.VideoWriter(capturedvideo, fourcc, 20.0, (640,480))
    start_time = time.time()
    while (int(time.time() - start_time) < timeout):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame, 0)
            out.write(frame)
            cv2.imshow('frame', frame)
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    create_Images(capturedvideo)

def create_Images(path):
    print(path)
    cap = cv2.VideoCapture(path)
    currentFrame = 0
    name=''
    while(currentFrame <= 10):
        ret, frame = cap.read()
        if(currentFrame >= 9 ):
            name = './data/TrackImage_' + str(currentDT.strftime("%I%M%S%p")) + '.jpg'
            cv2.imwrite(name, frame)
            print ('Creating...' + name)
        currentFrame += 1
    cap.release()
    cv2.destroyAllWindows()
    send_email(name)

def send_email(Gattachment):
    print(Gattachment)
    toaddr = config.TO_ADDRESS;   
    me = config.EMAIL_ADDRESS;
    subject = "HPS Alert:"+currentDT.strftime("%I:%M:%S %p")

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = toaddr
    msg.preamble = "test " 

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(Gattachment, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= "' + Gattachment + '"')
    msg.attach(part)

    try:
       s = smtplib.SMTP('smtp.gmail.com', 587)
       s.ehlo()
       s.starttls()
       s.ehlo()
       s.login(user = config.EMAIL_ADDRESS, password = config.PASSWORD)
       s.sendmail(me, toaddr, msg.as_string())
       s.quit()
    except SMTPException as error:
          print ("Error")


while (currentDT.strftime("%I")=='04'):
    record_Video(2)
    break