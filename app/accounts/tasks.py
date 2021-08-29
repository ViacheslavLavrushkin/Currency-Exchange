
from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail


@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs={
        'max_retries': 5,
        'default_retry_delay': 60,
    },
)
def send_registration_email(body, email_to):
    title = 'Activate Your Account'
    send_mail(
        title,
        body,
        settings.settings_local.DEFAULT_FROM_EMAIL,
        [email_to],
        fail_silently=False,
    )
