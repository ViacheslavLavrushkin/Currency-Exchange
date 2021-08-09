from bs4 import BeautifulSoup

from celery import shared_task

from currency.utils import to_decimal

from django.core.mail import send_mail

from currency import choices


import requests


def _get_privatbank_currencies():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    return currencies


def _get_monobank_currencies():
    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    return currencies


def _get_vkurse_currencies():
    url = 'http://vkurse.dp.ua/course.json'
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    return currencies


def _get_iboxbunk_currencies():
    url = 'https://app.iboxbank.online/api/currency/rate-only-base/UAH'
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    currencies_data = currencies['rate']
    return currencies_data


@shared_task
def parse_privatbank():
    from currency.models import Rate

    currencies = _get_privatbank_currencies()

    # available_currencies = frozenset(('USD', 'EUR'))
    available_currency_types = {
        'USD':choices.RATE_TYPE_USD,
        'EUR':choices.RATE_TYPE_EUR,
    }

    source = 'privatbank'

    for curr in currencies:
        currency_type = curr['ccy']
        if currency_type in available_currency_types:
            currency_type = available_currency_types[curr['ccy']]

            buy = to_decimal(curr['buy'])
            sale = to_decimal(curr['sale'])

            previous_rate = Rate.objects.filter(source=source, type=currency_type).order_by('created').last()
            # check if new rate should be created
            if (
                    previous_rate is None or  # rate does not exist, create the first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy  # check if buy was changed after last check
            ):
                print(f'New rate was created: {sale} {buy}')  # noqa
                Rate.objects.create(
                    type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )
            else:
                print(f'Rate already exists: {sale} {buy}')  # noqa


@shared_task
def parse_monobank():
    from currency.models import Rate

    currencies = _get_monobank_currencies()

    # available_currencies = frozenset(('USD' -- 840, 'EUR' -- 978))
    available_currency_types = {
        840: choices.RATE_TYPE_USD,
        978: choices.RATE_TYPE_EUR
    }
    main_currency_type = (980,)
    source = 'monobank'

    for curr in currencies:
        currency_type = curr['currencyCodeA']
        main_type = curr['currencyCodeB']
        if (
                currency_type in available_currency_types and
                main_type in main_currency_type
        ):
            currency_type = available_currency_types[curr['currencyCodeA']]
            buy = to_decimal(curr['rateBuy'])
            sale = to_decimal(curr['rateSell'])

            previous_rate = Rate.objects.filter(source=source, type=currency_type).order_by('created').last()
            # check if new rate should be created
            if (
                    previous_rate is None or  # rate does not exist, create the first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy  # check if buy was changed after last check
            ):
                print(f'New rate was created: {sale} {buy}')  # noqa
                Rate.objects.create(
                    type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )
            else:
                print(f'Rate already exists: {sale} {buy}')  # noqa


@shared_task
def parse_vkurse():
    from currency.models import Rate

    currencies = _get_vkurse_currencies()

    available_currency_type = {
        'Dollar': choices.RATE_TYPE_USD,
        'Euro': choices.RATE_TYPE_EUR,
    }

    source = 'vkurse'

    for currency_type, val in currencies.items():
        if currency_type in available_currency_type:
            currency_type = available_currency_type[currency_type]
            buy = to_decimal(val['buy'])
            sale = to_decimal(val['sale'])

            # in the selection by the cur_type field, a function for reverse conversion of the currency type
            # has been added, in accordance with the Rate model
            previous_rate = Rate.objects.filter(source=source, type=currency_type).order_by('created').last()
            # check if new rate should be create
            if (
                    previous_rate is None or  # rate does not exists, create first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )
            else:
                print(f'Rate already exists: {sale} {buy}')  # noqa


@shared_task()
def parse_iboxbank():
    from currency.models import Rate

    currencies = _get_iboxbunk_currencies()

    available_currencies_type = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }
    source = 'iboxbank'

    for curr in currencies:
        currency_type = curr['currency']
        if currency_type in available_currencies_type:
            currency_type = available_currencies_type[curr['currency']]
            buy = to_decimal(curr['buyValue'])
            sale = to_decimal(curr['saleValue'])

            previous_rate = Rate.objects.filter(source=source, type=currency_type).order_by('created').last()
            # check if new rate should be created
            if (
                    previous_rate is None or  # rate does not exist, create the first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy  # check if buy was changed after last check
            ):
                print(f'New rate was created: {sale} {buy}') # noqa
                Rate.objects.create(
                    type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )
            else:
                print(f'Rate already exists: {sale} {buy}')  # noqa


@shared_task
def parse_alfabank():
    from currency.models import Rate

    url = 'https://alfabank.ua/'
    # parameter to prevent blocking
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit 537.36'
                             '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
               }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='currency-block', limit=3)

    currencies = []

    for curr in items:
        currencies.append({
            'c_type': curr.find('div', class_='title').get_text(strip=True),
            'buy': curr.findAll('span')[1].get_text(strip=True),
            'sale': curr.findAll('span')[3].get_text(strip=True),
        })
    available_currency_type = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }

    source = 'alfabank'

    for curr in currencies:
        currency_type = curr['c_type']
        if currency_type in available_currency_type:
            currency_type = available_currency_type[curr['c_type']]
            buy = to_decimal(curr['buy'])
            sale = to_decimal(curr['sale'])

            previous_rate = Rate.objects.filter(source=source, type=currency_type).order_by('created').last()
            # check if new rate should be create
            if (
                    previous_rate is None or  # rate does not exists, create first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )
            else:
                print(f'Rate already exists: {sale} {buy}')  # noqa


@shared_task
def parse_oschadbank():
    from currency.models import Rate

    url = 'https://www.oschadbank.ua/ua'
    # parameter to prevent blocking
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit 537.36'
                             '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
               }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='paragraph paragraph--type--exchange-rates '
                                       'paragraph--view-mode--default currency-item', limit=3)

    currencies = []

    for curr in items:
        currencies.append({
            'c_type': curr.find('span', class_='currency-sign').get_text(strip=True),
            'buy': curr.findAll('strong')[0].get_text(strip=True),
            'sale': curr.findAll('strong')[1].get_text(strip=True),
        })

    available_currency_type = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }

    source = 'oschadbank'

    for curr in currencies:
        currency_type = curr['c_type']
        if currency_type in available_currency_type:
            currency_type = available_currency_type[curr['c_type']]
            buy = to_decimal(curr['buy'])
            sale = to_decimal(curr['sale'])

            previous_rate = Rate.objects.filter(source=source, type=currency_type).order_by('created').last()
            # check if new rate should be create
            if (
                    previous_rate is None or  # rate does not exists, create first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )
            else:
                print(f'Rate already exists: {sale} {buy}')  # noqa


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
