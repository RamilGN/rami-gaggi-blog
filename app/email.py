from threading import Thread

from app import mail
from flask import current_app
from flask_mail import Message


def send_async_email(app, msg):  # noqa: WPS442
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(
        target=send_async_email,
        args=(
            current_app._get_current_object(),  # noqa: WPS437
            msg,
        ),
    ).start()
