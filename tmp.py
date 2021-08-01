#
# from collections import defaultdict, Counter
#
# #
# # def foo():
# #     return ['Hello']
# #
# # d = defaultdict(list)
# #
# # key1 = 1
# # d[key1].append('TEST')
# # print(d)
#
# d = [1, 1, 1, 3, 2, 2]
# print(Counter(d).most_common(2))






# < a href = "/currency/rate/delete/{{ form.instance.id }}/" > Delete < / a >

# def parse_mono():
#     import requests
#     url = 'https://api.monobank.ua/bank/currency'
#     response = requests.get(url)
#     response.raise_for_status()
#     currencies = response.json()
#
#     available_currency_types = (840, 978)
#
#     # uah_number = (980)
#
#     for curr in currencies:
#         currency_type = curr['currencyCodeA']
#         if currency_type in available_currency_types:
#             print(curr)
#
#
# parse_mono()


def parse_vkurse():
    from currency.models import Rate
    from bs4 import BeautifulSoup
    from currency.utils import to_decimal

    import requests
    url = 'http://vkurse.dp.ua/'
    response = requests.get(url)
    assert response.status_code == 200



    soup = BeautifulSoup(response.text, 'html.parser')
    mydivs = soup.findAll("div", {"class": "pokupka-section"})
    rates = mydivs[0].findAll('td', {'class': 'right'})

    rates = [to_decimal(rate.text.replace(',', '.')) for rate in rates]
    rates_to_save = [
        {'amount': rates[0], 'currency_type': mch.CURRENCY_TYPE_USD, 'type': mch.RATE_TYPE_SALE},
        {'amount': rates[1], 'currency_type': mch.CURRENCY_TYPE_USD, 'type': mch.RATE_TYPE_BUY},
        {'amount': rates[2], 'currency_type': mch.CURRENCY_TYPE_EUR, 'type': mch.RATE_TYPE_SALE},
        {'amount': rates[3], 'currency_type': mch.CURRENCY_TYPE_EUR, 'type': mch.RATE_TYPE_BUY},
    ]

    for rate in rates_to_save:
        amount = rate['amount']
        last = Rate.objects.filter(
            source=mch.SOURCE_AVAL,
            currency_type=rate['currency_type'],
            type=rate['type'],
        ).last()

        if last is None or last.amount != amount:
            Rate.objects.create(
                amount=amount,
                source=mch.SOURCE_AVAL,
                currency_type=rate['currency_type'],
                type=rate['type'],
            )