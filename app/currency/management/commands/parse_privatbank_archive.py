import datetime
from datetime import datetime as dt
from time import sleep

from currency import choices, consts
from currency.models import Bank, Rate
from currency.utils import to_decimal

from django.core.management.base import BaseCommand

import requests


def privatbank_archive_parsed():
    rate = Rate.objects.filter(
        bank='1',
        created__hour='00',
        created__minute='00',
        created__second='00',
    ).last()
    if rate:
        latest_data_start = rate.created.date()
        return latest_data_start
    return datetime.date(2014, 12, 1)


def get_convert_date(currency_date):
    created_db_date = dt.strptime(currency_date, "%d.%m.%Y")
    created_db_date = f'{created_db_date}.000001'
    return created_db_date


def get_date_str_start(date_start):
    string_date = date_start.strftime('%d.%m.%Y')
    return string_date


class Command(BaseCommand):
    def handle(self, *args, **options):
        date = datetime.date.today()
        date_start = date - datetime.timedelta(days=1)
        date_stop = datetime.date(1992, 3, 19)

        available_currency_type = {
            'USD': choices.RATE_TYPE_USD,
            'EUR': choices.RATE_TYPE_EUR,
        }

        while True:
            date_parse = f'json&date={get_date_str_start(date_start)}'
            url = 'https://api.privatbank.ua/p24api/exchange_rates'
            response = requests.get(url, params=date_parse)
            response.raise_for_status()

            currency_list = response.json()['exchangeRate']
            currency_date = response.json()['date']

            bank = Bank.objects.get(code_name=consts.CODE_NAME_PRIVATBANK)

            for curr in currency_list:
                if 'currency' in curr:
                    currency_type = curr['currency']
                    if currency_type in available_currency_type:
                        currency_type = available_currency_type[curr['currency']]
                        buy = to_decimal(curr['purchaseRate'])
                        sale = to_decimal(curr['saleRate'])

                        previous_rate = Rate.objects.filter(
                            bank=bank,
                            type=currency_type
                        ).order_by('created').last()

                        if (
                                previous_rate is None or
                                previous_rate.sale != sale or
                                previous_rate.buy != buy
                        ):
                            Rate.objects.create(
                                type=currency_type,
                                sale=sale,
                                buy=buy,
                                bank=bank,
                            )

                            rate = Rate.objects.last()
                            Rate.objects.filter(id=rate.id).update(created=get_convert_date(currency_date))

            if date_start == date_stop:
                break
            date_start -= datetime.timedelta(days=1)
            sleep(10)
