from celery import shared_task
from django.core.mail import send_mail


@shared_task
def print_hello_world(rate_id):
    from currency.models import Rate

    rate = Rate.objects.get(id=rate_id)
    print(f'Got Rate with id: {rate.id}')


@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs={
        'max_retries': 5,
        'default_retry_delay': 60,
    },
)
def send_email_in_background(body):
    send_mail(
        'Contact Us from Client',
        body,
        'testofamilo25@gmail.com',
        ['lavrushkinvv@gmail.com'],
        fail_silently=False,
    )


