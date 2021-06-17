import decimal
import random

from currency.models import ContactUs
from currency.models import Rate

from django.core.management.base import BaseCommand

from faker import Faker

from mdgen import MarkdownPostProvider


fake = Faker()
fake.add_provider(MarkdownPostProvider)


class Command(BaseCommand):
    help = 'Generate Random records' # noqa

    def handle(self, *args, **options):

        for index in range(100):
            Rate.objects.create(
               type=random.choice(('usd', 'eur', 'gpb', 'uah', 'rub')),
               sale=decimal.Decimal(random.randrange(2000, 2999))/100,
               buy=decimal.Decimal(random.randrange(2000, 2999))/100,
               source=random.choice(('monobank', 'privatbank', 'vkurse')),
            )

            ContactUs.objects.create(
               email_from=fake.free_email(),
               subject=fake.name(),
               message=fake.post(size='medium'),
            )
