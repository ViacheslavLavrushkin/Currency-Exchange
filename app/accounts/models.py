import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.static import static


def user_directory_path(instance, filename):
    return 'uploads/avatars/{0}/{1}'.format(instance.id, filename)


class User(AbstractUser):
    avatar = models.FileField(
        null=True, blank=True, default=None, upload_to=user_directory_path)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    phone = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        default=None,
        # validators=(validate_is_digits,)
    )
    email = models.EmailField(
        'email address',
        blank=False,
        null=False,
        unique=True,
    )

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static('img/default-avatar.jpeg')

    def save(self, *args, **kwargs):
        print('Before Save')  # noqa
        if not self.username:  # if object was created
            self.username = str(uuid.uuid4())
        if self.phone:
            self.phone = ''.join(char for char in self.phone if char.isdigit())

        super().save(*args, **kwargs)
        print('After Save')  # noqa
