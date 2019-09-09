from database import insert_id
from email_helper import get_emails

from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
accountSID = os.getenv("ACCOUNT_SID")
authToken = os.getenv("AUTH_TOKEN")

twilioClient = Client(accountSID, authToken)
myTwilioNumber = os.getenv("MY_TWILIO_NUMBER")
myPhone = os.getenv("MY_NUMBER")


def send_messages(msg):
    message = twilioClient.messages.create(
                            body=msg,
                            from_=myTwilioNumber,
                            to=myPhone
                            )

if __name__ == "__main__":
    for email in get_emails():
        send_messages(email['msg'])
        try:
            insert_id(email['id'])
        except:
            pass
