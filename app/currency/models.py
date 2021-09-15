from currency import choices

from django.db import models
from django.templatetags.static import static


# class Source(models.Model):
#     name = models.CharField(max_length=255)
#     url = models.URLField(max_length=200)


def bank_directory_path(instance, filename):
    return 'uploads/bank_logo/{0}/{1}'.format(instance.id, filename)


class Bank(models.Model):
    bank_logo = models.FileField(
        null=True, blank=True, default=None, upload_to=bank_directory_path)
    name = models.CharField(max_length=64)
    code_name = models.CharField(
        max_length=64,
        unique=True,
        null=True,
        default=None,
    )
    url = models.URLField(max_length=200)
    original_url = models.URLField()

    @property
    def get_bank_logo_url(self):
        if self.bank_logo:
            return self.bank_logo.url
        return static('img/default-bank-logo.png')


class Rate(models.Model):
    # def get_{field_name}_display()
    type = models.PositiveSmallIntegerField(choices=choices.RATE_TYPE_CHOICES)  # noqa
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    date_parsed = models.DateTimeField(auto_now=True)
    # source = models.CharField(max_length=64)
    bank = models.ForeignKey(
        Bank,
        on_delete=models.CASCADE,
        # null=True,
        # default=None,
    )
    # bank = models.ForeignKey(Source)

    def __str__(self):
        return f'Rate id: {self.id} {self.bank_id}'


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
