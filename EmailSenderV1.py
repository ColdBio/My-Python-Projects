import smtplib, ssl
import getpass

"""
This project was completed as a code along using this guide -> https://realpython.com/python-send-email/

python -m smtpd -c DebuggingServer -n localhost:1025

TODOs:- 
1. Create a simple function that takes in a user defined sender, receiver, subject, and body using the terminal
2. Allow someone to send emails using a GUI ✅ see SendingSimpleEmailV2.py file
"""

# Sender and Receiver Emails
sender = "throwawaynon54321@gmail.com"
receiver = "throwawaynon54321@gmail.com"
message = 'Subject: Hello World :D' + '\n\n' + 'Lorem Ipsum'


# Gmail requires that port 465 be used if connecting using SMTP_SSL
port = 465

# Creating a secure SSL context
context = ssl.create_default_context()

# Prevents the password being stored within the code
password = getpass.getpass()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
