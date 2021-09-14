from unittest.mock import MagicMock

from currency import consts
from currency.models import Bank, Rate
from currency.tasks import parse_vkurse


def test_parse_vkurse(mocker):
    json_mock = lambda: {  # noqa
        "Dollar": {
            "buy": "26.60",
            "sale": "26.75"
        },
        "Euro": {
            "buy": "31.40",
            "sale": "31.55"
        },
    }
    requests_get = mocker.patch('requests.get', return_value=MagicMock(json=json_mock))  # noqa

    code_name = consts.CODE_NAME_VKURSE
    vkurse_data = {
        'name': 'Vkurse',
        'url': 'http://vkurse.dp.ua/course.json',
        'original_url': 'http://vkurse.dp.ua/',
    }
    Bank.objects.create(code_name=code_name, **vkurse_data)

    initial_count = Rate.objects.count()
    parse_vkurse()

    assert Rate.objects.count() == initial_count + 2
