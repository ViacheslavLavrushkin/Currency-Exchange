from accounts.models import User

from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def pre_save_user(sender, instance, **kwargs):
    print('PRE SAVE WORKS')  # noqa


@receiver(post_save, sender=User)
def post_save_user_send_to_cool_service(sender, instance, created, **kwargs):
    # print(f'Instance is created: {created} Instance: {instance}')
    if created:
       print('Send to some cool service')  # noqa


@receiver(post_save, sender=User)
def post_save_user_send_to_awesome_service(sender, instance, created, **kwargs):
    # print(f'Instance is created: {created} Instance: {instance}')
    if created:
       print('Send to some awesome service')  # noqa


class DeleteIsNotAllowed(Exception):
    pass


@receiver(pre_delete, sender=User)
def stop_delete(*args, **kwargs):
    raise DeleteIsNotAllowed('Instance could not be deleted')


@receiver(pre_save, sender=User)
def change_email_to_lower(sender, instance, **kwargs):
    instance.email = instance.email.lower()
