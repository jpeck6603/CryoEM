#!/usr/bin/python3

# Monitors the job.log file for a cryoSPARC job and sends a text or email when the job is completed
# Keeps me from obsessively watching the computer for job completion
# I set up a separate email account from which to send notifications, you may need to reduce the privacy settings on gmail for the script to log in and send the notification.
#All sections that need to be customized are in CAPS

import os, time
import datetime
import pathlib
#request directory
file_to_watch = input("Enter log /file/to/monitor : ")
job_number = input("Enter job name : ")

fname = pathlib.Path(file_to_watch)
assert fname.exists(), f'No such file: {fname}'  # check that the file exists
print(fname.stat())


while True:
	mtime1 = datetime.datetime.fromtimestamp(fname.stat().st_mtime)
	time.sleep(30)
	mtime2 = datetime.datetime.fromtimestamp(fname.stat().st_mtime)
	if mtime1 == mtime2:
		break
	else:
		pass



import sys
import smtplib, ssl

port = 465 #for SSL
password = "ENTER_EMAIL_PASSOWRD_HERE"

#secure SSL context
context = ssl.create_default_context()
sender_email = "ENTER_SENDER_EMAIL_HERE"
message = job_number + " finished."

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	server.login(sender_email, password)
	server.sendmail(sender_email, 'PHONE_NUMBER@mms.att.net', message)
	server.sendmail(sender_email, 'RECIPIENT_EMAIL@gmail.com', message)
	print("Monitoring stopped.  Re-run script if you wish to continue monitoring.")
