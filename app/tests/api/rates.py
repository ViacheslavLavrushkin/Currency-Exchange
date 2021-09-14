from currency import choices


def test_rates_list(client_api_auth):
    response = client_api_auth.get('/api/v1/rates/')
    assert response.status_code == 200
    # assert 'results' in response.json()


def test_rates_create_invalid(client_api_auth):
    data = {}
    response = client_api_auth.post('/api/v1/rates/', data=data)
    assert response.status_code == 200
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'type': ['This field is required.'],
        'bank': ['This field is required.']
    }


def test_rates_create_success(client_api_auth, bank):
    data = {
        'buy': 20,
        'sale': 21,
        'type': choices.RATE_TYPE_USD,
        'bank': bank.id,
    }
    response = client_api_auth.post('/api/v1/rates/', data=data)
    assert response.status_code == 201
    assert response.json()
