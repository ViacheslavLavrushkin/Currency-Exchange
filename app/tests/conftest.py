from django.core.management import call_command

import pytest


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


@pytest.fixture(autouse=True, scope="session")
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'app/tests/fixtures/banks.json')


@pytest.fixture(scope="function", autouse=True)
def fake():
    from faker import Faker
    faker = Faker()
    yield faker


@pytest.fixture(scope='function')
def client_api_auth(django_user_model):
    from rest_framework.test import APIClient
    client = APIClient()

    email = "drftestauthuser@example.com"
    password = "password"
    user = django_user_model.objects.create(email=email, password=password)
    user.set_password(password)
    user.save()

    response = client.post('/api/v1/token/', data={'email': email, 'password': password})
    assert response.status_code == 200

    client.credentials(HTTP_AUTHORIZATION='JWT ' + response.json()['access'])

    yield client

    user.delete()


@pytest.fixture(scope='function')
def bank(enable_db_access_for_all_tests):
    from currency.models import Bank

    yield Bank.objects.last()


@pytest.fixture(scope='function')
def rate(enable_db_access_for_all_tests):
    from currency.models import Rate

    yield Rate.objects.last()
