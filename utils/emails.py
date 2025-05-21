from django.core.mail import send_mail
from django.conf import settings


def send_email(data):
    to = data.get("to")
    subject = data.get("subject")
    message = data.get("message") 
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=[to]
    )