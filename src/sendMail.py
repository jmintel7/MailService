import os
import json
import smtplib
from email.message import EmailMessage

#to get the directory of running python script
file_path = os.path.realpath(__file__)
file_path = os.path.split(file_path)[0]

file = os.path.join(file_path,'config.json')

with open(file,'r') as fr:
    config = json.load(fr)

email_id = config['email_id']
email_pass = config['email_pass']
contacts = config['contacts']



# images = os.listdir('images')


msg = EmailMessage()
msg['Subject'] = 'Test Email'
msg['From'] = email_id
msg['To'] = contacts
msg.set_content('This is the content')

# for image in images:
#     with open('images/'+image, 'rb') as file:
#         file_data = file.read()
#         file_name = os.path.basename(file.name)
#     msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email_id,email_pass)
    smtp.send_message(msg)