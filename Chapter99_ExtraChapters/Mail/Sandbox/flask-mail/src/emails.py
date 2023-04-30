from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from threading import Thread

from src.extensions import mail
from src.config import Config, Constants


def send_email(subject, text, recipients):
    message = Message(subject=subject, html=text, recipients=[recipients], sender="Unilab")
    thread = Thread(target=mail.send(message))
    thread.start()


def create_key(payload):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    key = serializer.dumps(payload, salt=Constants.SERIALIZER_SALT)
    return key


def confirm_key(key):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    try:
        payload = serializer.loads(key, salt=Constants.SERIALIZER_SALT, max_age=600)
        return payload
    except:
        return False




