#!/usr/bin/python3

#Captures user input and monitors specified directory for addition of new files or folders within a specified time interval.
#Originally written to monitor data collection directory for a Talos Arctica cryoTEM and send notification if data collection stopped
#I set up a separate email account from which to send notifications, you may need to reduce the privacy settings on gmail for the script to log in and send the notification.
#All sections that need to be customized are in CAPS

import os, time
#request directory
path_to_watch = input("Enter /directory/to/monitor : ")

#can add another person to notify here, hash out if you plan to only run this for yourself
customer = input("Do you wish to send additional notifications? Enter (y/n): ")
if customer == 'y':

	choice = input("Text or email? Enter (t/e): ")
	if choice == 't':
		phone_num = input("Enter phone number. Note that AT&T numbers should be entered ad 1115550123@mms.att.net and Verizon numbers as 1115550123@vtext.com: ")
	elif choice == 'e':
		receiver_email = input("Enter the email to be notified: ")

elif customer == 'n':
	print("Skipping additional notifications.")

#creates a dictionary of the directory contents, waits the specified sleep interval and creates another dictionary.  
#If the dictionaries are the same, no files have been added in the time interval, so data addition has likely stopped
#Time interval is set in seconds


print("Now monitoring " + path_to_watch)
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (1200)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  if added:
  	print ("Added: ", ", ".join (added))
  if before == after:
  	print("No files have been added for 20 minutes.")
  	break
   
  before = after

#once the dictionaries are the same, sends notifications via text and email
import sys
import smtplib, ssl

port = 465 #for SSL
password = "ENTER_EMAIL_PASSWORD"

#secure SSL context
context = ssl.create_default_context()

#email message content
sender_email = "ENTERSENDEREMAILHERE@gmail.com"
message = """\
Subject: Data collection stopped

It has been 20 minutes since a file was added to the collection directory."""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	server.login(sender_email, password)

#	will email and text the following, as well as any from user input
	server.sendmail(sender_email, 'ENTER_RECIPIENT_EMAIL_HERE@gmail.com', message)
	server.sendmail(sender_email, 'VERIZON_NUMBER@vtext.com', message)
	server.sendmail(sender_email, 'ATT_NUMBER@mms.att.net', message)
	if customer == "y":
		if choice == "e":
			server.sendmail(sender_email, receiver_email, message)	
		elif choice == "t":
			server.sendmail(sender_email, phone_num, message)
		else:
			pass
	else:
		pass
	print("Monitoring stopped.  Re-run script if you wish to continue monitoring.")
