from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    #
    # email = models.EmailField(
    #     'email address', blank=False, null=False, unique=True,
    # )
