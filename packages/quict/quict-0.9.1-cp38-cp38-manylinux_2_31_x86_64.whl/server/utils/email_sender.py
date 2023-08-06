import string
import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header


EMAIL_HOST = "smtp.sina.com"
MAIL_USER = "quict_pin_reset"
AUTH_KEY = "ae2725b5ce956101"
SENDER_EMAIL = "quict_pin_reset@sina.com"


def generator_random_password() -> str:
    default_size = 16
    chars = string.ascii_letters + string.digits
    rand_chars = [random.choice(chars) for _ in range(default_size)]

    return "".join(rand_chars)


def send_reset_password_email(receiver: str) -> str:
    """ Send reset password emails to receiver. """
    reset_password = generator_random_password()

    message = MIMEText(
        "Hi, there: \n" +
        f"The new password for QuICT is {reset_password}, please change it after successful login.\n" +
        "Thanks for your support.",
        "plain",
        "utf-8"
    )
    message["From"] = Header(SENDER_EMAIL)
    message["Subject"] = Header("QuICT User Password Reset", "utf-8")

    try:
        smtpObj = smtplib.SMTP()                # Initial SMTP Object
        smtpObj.connect(EMAIL_HOST, 25)         # Connect SMTP Server
        smtpObj.login(MAIL_USER, AUTH_KEY)      # Validation login
        smtpObj.sendmail(SENDER_EMAIL, receiver, message.as_string())    # Send Context.

        return reset_password
    except smtplib.SMTPException as error:
        print("error:{}".format(error))
