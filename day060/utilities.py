from smtplib import SMTP
import flask
import dotenv
import os

dotenv.load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def send_contact_mail(request: flask):
    content = "\n".join([f"{label.title()}: {content}" for (label, content) in request.values.items()])
    message = "Subject:New Message\n\n" + content
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=message)
