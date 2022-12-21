# Python

import os
from email.message import EmailMessage
import ssl
import smtplib


# Defining variables

email_sender = "<your_email>"
email_recipient = "<recipient_email>"

# 16 digit password created in google

email_password = "****************"

# Email subject

affair = "proof of delivery of mails with google"

# Email body

body = """
this is an email sending test made with python.
Remember that the shipment is only with google mail
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_recipient
em["Subjet"] = affair
em.set_content(body)

# Adding security with ssl

context = ssl.create_default_context()

# Sending email
## Default port google (465)

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
    
    ### Login 
    
    smtp.login(email_sender, email_password)
    
    ### Email send
    
    smtp.sendmail(email_sender, email_recipient, em.as_string())