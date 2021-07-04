from django.db import models


class Rate(models.Model):
    type = models.CharField(max_length=5) # noqa
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=64)


class ContactUs(models.Model):
    object = models.CharField(max_length=120) # noqa
    email_from = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)


class Source(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=200)
