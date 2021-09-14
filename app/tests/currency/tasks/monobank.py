from unittest.mock import MagicMock

from currency import consts
from currency.models import Bank, Rate
from currency.tasks import parse_monobank


def test_parse_monobank(mocker):
    json_mock = lambda: [  # noqa
        {"currencyCodeA": 840, "currencyCodeB": 980, "date": 1631604006, "rateBuy": 26.58, "rateSell": 26.7702},
        {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1631604006, "rateBuy": 31.37, "rateSell": 31.6696},
    ]
    requests_get = mocker.patch('requests.get', return_value=MagicMock(json=json_mock))  # noqa

    code_name = consts.CODE_NAME_MONOBANK
    monobank_data = {
        'name': 'MonoBank',
        'url': 'https://api.monobank.ua/bank/currency',
        'original_url': 'https://www.monobank.ua',
    }
    Bank.objects.create(code_name=code_name, **monobank_data)

    initial_count = Rate.objects.count()
    parse_monobank()

    assert Rate.objects.count() == initial_count + 2
