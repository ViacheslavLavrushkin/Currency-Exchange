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
#     url = 'http://vkurse.dp.ua/course.json'
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
#

# parse_vkurse()


    # print(rates)
    # mydivs = soup.findAll("div", {"class": "pokupka-section"})
    # rates = mydivs[0].findAll('p', {'class': 'pokupka-value'})

    # rates = mydivs[0].findAll('p', {'class': 'pokupka-value'})


    # for curr in rates:
    #     currency_type = curr['currencyCodeA']
    #     if currency_type in available_currency_types:
    #         print(curr)

    # rates = [to_decimal(rate.text.replace(',', '.')) for rate in rates]



    # rates_to_save = [
    #     {'amount': rates[0], 'currency_type': CURRENCY_TYPE_USD, 'type': mch.RATE_TYPE_SALE},
    #     {'amount': rates[1], 'currency_type': CURRENCY_TYPE_USD, 'type': mch.RATE_TYPE_BUY},
    #     {'amount': rates[2], 'currency_type': CURRENCY_TYPE_EUR, 'type': mch.RATE_TYPE_SALE},
    #     {'amount': rates[3], 'currency_type': CURRENCY_TYPE_EUR, 'type': mch.RATE_TYPE_BUY},
    # ]


    # for rate in rates_to_save:
    #     amount = rate['amount']
    #     last = Rate.objects.filter(
    #         source=mch.SOURCE_AVAL,
    #         currency_type=rate['currency_type'],
    #         type=rate['type'],
    #     ).last()
    #
    #     if last is None or last.amount != amount:
    #         Rate.objects.create(
    #             amount=amount,
    #             source=mch.SOURCE_AVAL,
    #             currency_type=rate['currency_type'],
    #             type=rate['type'],
    #         )

#  navbar.html lesson16

# {% if request.user.is_authenticated %}
#     <a href="{% url 'logout' %}">Logout</a>
#     <a href="{% url 'account:my-profile' %}">My Profile</a>
# {% else %}
#     <a href="{% url 'login' %}">Login</a>
#     <a href="#">SignUp</a>
# {% endif %}



# sudo apt install uwsgi-core                   # version 2.0.18-11ubuntu1, or
# sudo apt install uwsgi-plugin-alarm-curl      # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-alarm-xmpp      # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-curl-cron       # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-emperor-pg      # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-gccgo           # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-geoip           # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-glusterfs       # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-graylog2        # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-jvm-openjdk-11  # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-ldap            # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-lua5.1          # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-lua5.2          # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-luajit          # version 2.0.17.1+2+0.0.3build1
# sudo apt install uwsgi-plugin-mono            # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-php             # version 2.0.18+5ubuntu7+0.0.4ubuntu1
# sudo apt install uwsgi-plugin-psgi            # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-python3         # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-rack-ruby2.7    # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-rados           # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-router-access   # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-sqlite3         # version 2.0.18-11ubuntu1
# sudo apt install uwsgi-plugin-xslt            # version 2.0.18-11ubuntu1

# uWSGI==2.0.19.1


# DATABASES = {
#
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'database-name',
#         'USER': 'example-user',
#         'PASSWORD': '1155771',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
#
# }