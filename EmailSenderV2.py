import tkinter as tk
import smtplib, ssl
import getpass

# Root window  
window = tk.Tk()

window.title("Simple Email Sender v2")

from_label = tk.Label(text="From")
from_field = tk.Entry(text="", width= 62)

to_label = tk.Label(text="To")
to_field = tk.Entry(text="", width= 62)

subject_label = tk.Label(text="Subject")
subject_field = tk.Entry(text="", width= 62)

body_label = tk.Label(text="Body")
body_field = tk.Text(window, height = 27)

password_label = tk.Label(text="Password")
password_field = tk.Entry(show="*", width= 62)

def email_handler():
    # Sender and Receiver Emails
    sender = from_field.get().lower()
    receiver = to_field.get().lower()
    message = (f'Subject: {subject_field.get()}' + '\n\n' + f'{body_field.get("1.0","end-1c")}')
    print(subject_field.get())
    
    # Gmail requires that port 465 be used if connecting using SMTP_SSL
    port = 465

    # Creating a secure SSL context
    context = ssl.create_default_context()

    # Prevents the password being stored within the code
    password = password_field.get()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)


submit_button = tk.Button(window, text="Send", command = email_handler, width= 62)

from_label.grid(row=1, column=1)
from_field.grid(row=1, column=2)

to_label.grid(row=2, column=1)
to_field.grid(row=2, column=2)


subject_label.grid(row=3, column=1)
subject_field.grid(row=3, column=2)

body_label.grid(row=4, column=1)
body_field.grid(row=4, column=2)

password_label.grid(row=5, column=1)
password_field.grid(row=5, column=2)


submit_button.grid(row=6, column=2)

window.mainloop()
