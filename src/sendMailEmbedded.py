from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import random
import json
import os
import sys

args = sys.argv

#to get the directory of running python script
file_path = os.path.realpath(__file__)
file_path = os.path.split(file_path)[0]

file = os.path.join(file_path,'config.json')

with open(file,'r') as fr:
    config = json.load(fr)

email_id = config['email_id']
email_pass = config['email_pass']
contacts = config['contacts']


image_path = os.path.join(file_path,'images')
images = os.listdir(image_path)

if (len(args)>3):
	message=args[3]
else:
	message="Its another beautiful day in our life. Rise and Shine. I Love You."

if (len(args)>2):
	image = args[2]
else:
	image = random.choice(images)

if (len(args)>1):
	subject = args[1]
elif (os.path.exists(os.path.join(file_path,'subjects.txt'))):
	with open(os.path.join(file_path,'subjects.txt'),'r') as file:
		subjects = file.read().split('\n')
		subjects.pop()
		subject = random.choice(subjects)
else:
	subject = "I Love You"

msg = MIMEMultipart()
msg['From'] = email_id
msg['To'] = (',').join(contacts)
msg['Subject'] = Header(f"{subject}",'utf-8').encode()

if(os.path.exists(os.path.join(image_path,image))):
	with open(os.path.join(image_path,image),'rb') as file:
    		mime = MIMEBase('image',os.path.splitext(image)[1],filename=image)
    		mime.add_header('Content-Disposition','attachment',filename=image)
    		mime.add_header('X-Attachment-Id','0')
    		mime.add_header('Content-ID','<0>')
    		mime.set_payload(file.read())
    		encoders.encode_base64(mime)
    		msg.attach(mime)


msg_content = MIMEText(f"""\
<!DOCTYPE html>
<html lang="en">
<body>
    <h1>{message}</h1>
    <p><img src="cid:0"></p>
</body>
</html>
""",'html','utf-8')
msg.attach(msg_content)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
#    smtp.set_debuglevel(1)
    smtp.login(email_id,email_pass)
    smtp.sendmail(email_id,contacts,msg.as_string())

print("------------Completed----------------")
