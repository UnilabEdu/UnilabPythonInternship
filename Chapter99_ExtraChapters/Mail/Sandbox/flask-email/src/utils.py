from flask import copy_current_request_context
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from threading import Thread

from src.extensions import mail
from src.config import Config


def send_email(subject, text, recipients):
    message = Message(subject=subject, html=text, recipients=recipients, sender="testagain@yahoo.com")

    @copy_current_request_context
    def send_message(message):
        mail.send(message)

    thread = Thread(target=send_message, args=[message])
    thread.start()


def create_key(user_email):

    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    key = serializer.dumps(user_email, salt=Config.SERIALIZER_SALT)
    return key


def confirm_key(activation_key):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    try:
        email = serializer.loads(activation_key, salt=Config.SERIALIZER_SALT, max_age=120)
    except:
        return False
    else:
        return email
