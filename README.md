you will need src/config.json with keys 'email_id', 'email_pass' and 'contacts' which is list of recipients

you will need a folder 'src/images' with all images to send

for customized subjects, add each subjects in new line in the 'src/subjects.txt' file

#Daily Mail
0 5 * * * /home/ubuntu/scripts/MailService/venv/bin/python3.6 /home/ubuntu/scripts/MailService/src/sendMailEmbedded.py

#Customized Mail
minute hour date month * /home/ubuntu/scripts/MailService/venv/bin/python3.6 /home/ubuntu/scripts/MailService/src/sendMailEmbedded.py <Subject> <image> <Inline message>


