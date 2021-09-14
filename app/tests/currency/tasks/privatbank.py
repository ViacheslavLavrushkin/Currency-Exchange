from unittest.mock import MagicMock

from currency import consts
from currency.models import Bank, Rate
from currency.tasks import parse_privatbank


def test_parse_privatbank(mocker):
    json_mock = lambda: [  # noqa
        {"ccy": "USD", "base_ccy": "UAH", "buy": "26.50000", "sale": "26.90000"},
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "31.20000", "sale": "31.80000"},
        {"ccy": "RUR", "base_ccy": "UAH", "buy": "0.35000", "sale": "0.38000"},
        {"ccy": "BTC", "base_ccy": "USD", "buy": "43381.5230", "sale": "47947.9992"}
    ]
    requests_get = mocker.patch('requests.get', return_value=MagicMock(json=json_mock))  # noqa

    code_name = consts.CODE_NAME_PRIVATBANK
    privatbank_data = {
        'name': 'PrivatBank',
        'url': 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5',
        'original_url': 'https://privatbank.ua',
    }
    Bank.objects.create(code_name=code_name, **privatbank_data)

    initial_count = Rate.objects.count()
    parse_privatbank()

    assert Rate.objects.count() == initial_count + 2
