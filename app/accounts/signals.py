from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver

from accounts.models import User


@receiver(pre_save, sender=User)
def pre_save_user(sender, instance, **kwargs):
    print('PRE SAVE WORKS')


@receiver(post_save, sender=User)
def post_save_user_send_to_cool_service(sender, instance, created, **kwargs):
    # print(f'Instance is created: {created} Instance: {instance}')
    if created:
       print('Send to some cool service')


@receiver(post_save, sender=User)
def post_save_user_send_to_awesome_service(sender, instance, created, **kwargs):
    # print(f'Instance is created: {created} Instance: {instance}')
    if created:
       print('Send to some awesome service')


class DeleteIsNotAllowed(Exception):
    pass


@receiver(pre_delete, sender=User)
def stop_delete(*args, **kwargs):
    raise DeleteIsNotAllowed('Instance could not be deleted')
