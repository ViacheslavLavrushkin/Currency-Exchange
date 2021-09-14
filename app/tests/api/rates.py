from currency import choices
from currency.models import Rate


def test_rates_list(client_api_auth):
    response = client_api_auth.get('/api/v1/rates/')
    assert response.status_code == 200
    assert 'results' in response.json()


def test_rates_create_invalid(client_api_auth):
    rates_initial_count = Rate.objects.count()
    response = client_api_auth.post('/api/v1/rates/', data={})
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'cur_type': ['This field is required.'],
        'bank': ['This field is required.']
    }
    assert Rate.objects.count() == rates_initial_count


def test_rates_create_success(client_api_auth, bank):
    rates_initial_count = Rate.objects.count()
    data = {
        'buy': 20,
        'sale': 21,
        'type': choices.RATE_TYPE_USD,
        'bank': bank.id,
    }
    response = client_api_auth.post('/api/v1/rates/', data=data)
    assert response.status_code == 201
    assert response.json()['id'] == response.data['id']
    assert response.json()['type'] == data['type']
    assert response.json()['sale'] == str(data['sale'])
    assert response.json()['buy'] == str(data['buy'])
    assert response.json()['bank']['id'] == data['bank']
    assert Rate.objects.count() == rates_initial_count + 1


def test_rates_update_invalid(client_api_auth, rate):
    rates_initial_count = Rate.objects.count()
    response = client_api_auth.put(f'/api/v1/rates/{rate.id}/')

    assert response.status_code == 400
    assert response.json() == {
        'type': ['This field is required.'],
        'sale': ['This field is required.'],
        'buy': ['This field is required.'],
        'bank': ['This field is required.']
    }
    assert Rate.objects.count() == rates_initial_count


def test_rates_update_success(client_api_auth, rate, bank):
    rates_initial_count = Rate.objects.count()
    data = {
        'type': choices.RATE_TYPE_USD,
        'sale': rate.sale + 10,
        'buy': rate.buy + 10,
        'bank': bank.id
    }
    response = client_api_auth.put(f'/api/v1/rates/{rate.id}/', data=data)
    assert response.status_code == 200
    assert response.json()['id'] == rate.id
    rate.refresh_from_db()
    assert response.json()['type'] == rate.type
    assert response.json()['sale'] == str(rate.sale)
    assert response.json()['buy'] == str(rate.buy)
    assert response.json()['bank'] == bank.id
    assert Rate.objects.count() == rates_initial_count


def test_rates_delete(client_api_auth, rate):
    rates_initial_count = Rate.objects.count()
    response = client_api_auth.delete(f'/api/v1/rates/{rate.id}/')
    assert response.status_code == 204
    assert response.request['REQUEST_METHOD'] == 'DELETE'
    assert Rate.objects.count() == rates_initial_count - 1
