#!/usr/bin/python
import imaplib
import email
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

from database import get_ids

load_dotenv()


EMAIL  = os.getenv("EMAIL")
PWD    = os.getenv("PASSWORD")
SMTP_SERVER = "smtp-mail.outlook.com"
SMTP_PORT   = 587

def get_emails():
    messages = []

    try:
        already_read_ids = get_ids()
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(EMAIL,PWD)
        mail.select('inbox')
        state, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()

        for id in id_list:
            if id in already_read_ids:
                pass
            state, data = mail.fetch(id, '(RFC822)')

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    msgstr = str(msg)
                    if 'ebay' in msg['from']:
                        if 'question' in msg['subject']:
                            msg['subject']
                            messages.append({
                                'id': id,
                                'msg': msg['subject']
                            })

    except Exception, e:
        print str(e)

    return messages
