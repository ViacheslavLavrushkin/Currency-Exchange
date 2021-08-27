from currency import choices

from django.db import models


# class Source(models.Model):
#     name = models.CharField(max_length=255)
#     url = models.URLField(max_length=200)


class Bank(models.Model):
    name = models.CharField(max_length=255)
    code_name = models.CharField(
        max_length=64,
        unique=True,
        # null=True,
        # default=None,
    )
    url = models.URLField(max_length=200)
    original_url = models.URLField()


class Rate(models.Model):
    # def get_{field_name}_display()
    type = models.PositiveSmallIntegerField(choices=choices.RATE_TYPE_CHOICES)  # noqa
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    # source = models.CharField(max_length=64)
    bank = models.ForeignKey(
        Bank,
        on_delete=models.CASCADE,
        # null=True,
        # default=None,
    )
    # bank = models.ForeignKey(Source)

    def __str__(self):
        return f'Rate id: {self.id}'


class ContactUs(models.Model):
    object = models.CharField(max_length=120) # noqa
    email_from = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)


class Analytics(models.Model):
    path = models.CharField(max_length=255)
    counter = models.PositiveBigIntegerField()
    request_method = models.PositiveSmallIntegerField(choices=choices.REQUEST_METHOD_CHOICES)
    status_code = models.CharField(max_length=20)

    class Meta:
        unique_together = [
            ['path', 'request_method', 'status_code'],
        ]
