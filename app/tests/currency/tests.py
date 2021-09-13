from currency import choices
from currency.models import Bank, Rate

# import pytest
#
#
# @pytest.mark.skip('TODO does not work')


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert [t.name for t in response.templates] == [
        'index.html',
        'base.html',
        'includes/navbar.html',
    ]


def test_rate_list(client):
    response = client.get('/currency/rate/list/')
    assert response.status_code == 200


def test_create_rate_get_form(client):
    response = client.get('/currency/rate/create/')
    assert response.status_code == 200


def test_create_rate_empty_form_data(client):
    response = client.post('/currency/rate/create/')
    assert response.status_code == 200
    assert response.context['form'].errors == {
        'type': ['This field is required.'],
        'sale': ['This field is required.'],
        'buy': ['This field is required.'],
        'bank': ['This field is required.'],
    }


def test_create_rate_invalid_form_data(client):
    rates_initial_count = Rate.objects.count()
    form_data = {
        'type': choices.RATE_TYPE_USD,
        'sale': 20,
        'buy': 30,
        'bank': 99999,
    }
    response = client.post('/currency/rate/create/', data=form_data)
    assert response.status_code == 200
    assert response.context['form'].errors == {
        'bank': ['Select a valid choice. That choice is not one of the available choices.'],
    }
    # assert Rate.objects.count() == 1  -- WRONG
    assert Rate.objects.count() == rates_initial_count


def test_create_rate_success(client):
    rates_initial_count = Rate.objects.count()
    bank = Bank.objects.last()
    form_data = {
        'type': choices.RATE_TYPE_USD,
        'sale': 20,
        'buy': 30,
        'bank': bank.id,
    }
    response = client.post('/currency/rate/create/', data=form_data)
    assert response.status_code == 302
    assert response.url == '/currency/rate/list/'
    assert Rate.objects.count() == rates_initial_count + 1
