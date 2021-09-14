def test_signup(client):
    response = client.get('/accounts/signup/')
    assert response.status_code == 200


def test_signup_empty_form_data(client):
    response = client.post('/accounts/signup/', data={})
    assert response.status_code == 200
    assert response.context['form'].errors == {
        'email': ['This field is required.'],
        'password1': ['This field is required.'],
        'password2': ['This field is required.'],
    }


def test_signup_invalid_form_data(client, fake):
    form_data = {
        'email': fake.email,
        'password1': '12345',
        'password2': '12345',
    }
    response = client.post('/accounts/signup/', data=form_data)
    assert response.status_code == 200
