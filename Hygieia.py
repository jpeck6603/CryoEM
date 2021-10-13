#!/usr/bin/env python

# BE CAREFUL WITH THIS SCRIPT, IT WILL DELETE EVERYTHING IN THE FILEPATH OLDER THAN THE NUMBER OF DAYS YOU SPECIFY
# SERIOUSLY, BE CAREFUL
# If you want to check to see what this script will delete and notify you of, run hygieia_screening.py with the same parameters
# hygieia_screening.py will email a "deleted.txt" file of what this script will delete when run in the same directory

# importing the required modules
import os
import sys
import shutil
import time
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pathlib

# Check to see if warning.txt file already exists from previous run
warning_check = pathlib.Path("warning.txt")
# If so, remove it
if warning_check.exists():
    os.remove("warning.txt")
else:
    pass
# Create a blank version to append
with open("warning.txt", "w") as fp:
	pass


# Check to see if deleted.txt file already exists
deleted_check = pathlib.Path("deleted.txt")
# If so, remove it
if deleted_check.exists():
	os.remove("deleted.txt")
else:
	pass
# Create a blank version to append	
with open("deleted.txt", "w") as fp:
	pass


# Define stdout to modify later to write info to .txt file
original_stdout = sys.stdout

# Set email preferences
# Change receiver_email to the email you want txt files sent to
subject = "Hygieia"
body = "The attached file 'warning.txt' indicates which files and folders are in between the warning and deletion interval.  \nThe 'deleted.txt' file indicates the files and folders that have been deleted."
sender_email = "ENTER_SENDER_EMAIL"
receiver_email = "ENTER_RECIPIENT_EMAIL"
password = "ENTER_SENDER_EMAIL_PASSWORD"


# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body
message.attach(MIMEText(body, "plain"))

# Add attachments
filename = "warning.txt"
filename2 = "deleted.txt"

#-----------------------------------------------------------------------------------------

# main function
def main():

	global days

	# initializing the count
	deleted_folders_count = 0
	deleted_files_count = 0
	warning_folders_count = 0
	warning_files_count = 0

#-------------MUST CHANGE THESE PARAMETERS--------------
	# specify the path
	path = "/ENTER/PATH/TO/DIRECTORY/"

	# specify the days for deletion
	days = 90
	# specify days for warning
	days2 = 60

#-------------MUST CHANGE THESE PARAMETERS--------------

	# converting days to seconds
	# time.time() returns current time in seconds
	seconds = time.time() - (days * 24 * 60 * 60)
	seconds2 = time.time() - (days2 * 24 * 60 * 60)

	# checking whether the file is present in path or not
	if os.path.exists(path):

		# check subfolders and subdir
		for root_folder, folders, files in os.walk(path):
			
			# these get deleted	
			if seconds >= get_file_or_folder_age(root_folder):

				# removing the folder
				remove_folder(root_folder)
				deleted_folders_count += 1 
				
				# write folders to deleted
				with open('deleted.txt', 'a') as f:
					sys.stdout = f
					print(f"\n{root_folder} is older than {days} days and would be deleted.")
					sys.stdout = original_stdout
				
			# these get a warning
			if seconds2 >= get_file_or_folder_age(root_folder) and get_file_or_folder_age(root_folder) > seconds:
			
				warning_folders_count += 1
				# write folders to warning
				with open('warning.txt', 'a') as f:
					sys.stdout = f
					print(f"\n{root_folder} is older than {days2} days and will be removed soon.")
					sys.stdout = original_stdout
			else:
				continue

				# checking folder from the root_folder
				for folder in folders:

					# folder path
					folder_path = os.path.join(root_folder, folder)

					# these get deleted	
					if seconds >= get_file_or_folder_age(folder_path):

						# call remove_folder function
						remove_folder(folder_path)
						deleted_folders_count += 1 
						
						# write folders to deleted
						with open('deleted.txt', 'a') as f:
							sys.stdout = f
							print(f"\n{folder_path} is older than {days} days and would be deleted.")
							sys.stdout = original_stdout
						
					# these get a warning
					if seconds2 >= get_file_or_folder_age(folder_path) and get_file_or_folder_age(folder_path) > seconds:
			
						warning_folders_count += 1
			
						# write folders to warning
						with open('warning.txt', 'a') as f:
							sys.stdout = f
							print(f"\n{folder_path} is older than {days2} days and will be removed soon.")
							sys.stdout = original_stdout


				# checking the current directory files
				for file in files:

					# file path
					file_path = os.path.join(root_folder, file)

					# these get a deleted
					if seconds >= get_file_or_folder_age(file_path):

						# invoking the remove_file function
						remove_file(file_path)
						deleted_files_count += 1 
						
						#write files to deleted
						with open('deleted.txt', 'a') as f:
							sys.stdout = f
							print(f"\n{file_path} is older than {days} days and would be deleted.")
							sys.stdout = original_stdout
						
					
					# these get a warning
					if seconds2 >= get_file_or_folder_age(file_path) and get_file_or_folder_age(file_path) > seconds:
			
						warning_files_count += 1
				
						# write files to warning
						with open('warning.txt', 'a') as f:
							sys.stdout = f
							print(f"\n{file_path} is older than {days2} days and will be removed soon.")
							sys.stdout = original_stdout

		else:

			# if the path is not a directory
			
			if seconds >= get_file_or_folder_age(path):

				# delete file
				remove_file(path)
				deleted_files_count += 1
				
				#write files to deleted
				with open('deleted.txt', 'a') as f:
					sys.stdout = f
					print(f"\n{path} is older than {days} days and would be deleted.")
					sys.stdout = original_stdout
				
			if seconds2 >= get_file_or_folder_age(path) and get_file_or_folder_age(path) > seconds:
			
				warning_files_count +=1
				
				#write files to warning
				with open('warning.txt', 'a') as f:
					sys.stdout = f
					print(f"\n{path} is older than {days2} days and will be removed soon.")
					sys.stdout = original_stdout

	else:

		# file/folder is not found
		print(f'"{path}" is not found')
		deleted_files_count += 1 # incrementing count

	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")
	print(f"Total folders warned: {warning_folders_count}")
	print(f"Total files warned: {warning_files_count}")
    
	with open(filename, "rb") as attachment:
		part = MIMEBase("application", "octet-stream")
		part.set_payload(attachment.read())
	# Encode file in ASCII characters to send by email    
	encoders.encode_base64(part)

	# Add header as key/value pair to attachment part
	part.add_header(
        "Content-Disposition", 
        f"attachment; filename= {filename}",
    )

	# Add attachment to message and convert message to string
	message.attach(part)
	
	with open(filename2, "rb") as attachment:
		part = MIMEBase("application", "octet-stream")
		part.set_payload(attachment.read())
	# Encode file in ASCII characters to send by email    
	encoders.encode_base64(part)

	# Add header as key/value pair to attachment part
	part.add_header(
        "Content-Disposition", 
        f"attachment; filename= {filename2}",
    )

	# Add attachment to message and convert message to string
	message.attach(part)
	
	
	text = message.as_string()

	# Log in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, text)            
      

def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):

		# success
		print(f"{path} removed successfully")

	else:

		# failure
		print(f"Unable to delete {path}")



def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success
		print(f"{path} removed successfully")

	else:

		# failure
		print(f"Unable to delete {path}")


def get_file_or_folder_age(path):

	# getting mtime of the file/folder in seconds
	try:
		mtime = os.stat(path).st_mtime
	except FileNotFoundError:
		mtime = time.time() - ((days + 1) * 24 * 60 * 60)
	# returning the time
	return mtime


if __name__ == '__main__':
	main()
