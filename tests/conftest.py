import pytest
import requests

from data import Url, generate_courier_body


@pytest.fixture(scope='function')
def generate_courier_data():
    courier_data = generate_courier_body()
    response = requests.post(f'{Url.base_url}{Url.courier_url}', json=courier_data)
    response_status_code = response.status_code
    response_body = response.json()

    login_payload = {
        "login": courier_data['login'],
        "password": courier_data['password']
    }
    login_response = requests.post(f'{Url.base_url}{Url.login_url}', json=login_payload)
    login_response_status_code = login_response.status_code
    login_response_body = login_response.json()
    courier_id = login_response_body.get("id")

    yield {
        "create_status_code": response_status_code,
        "create_body": response_body,
        "id": courier_id,
        "login": courier_data['login'],
        "password": courier_data['password'],
        "first_name": courier_data['firstName'],
        "login_status_code": login_response_status_code,
        "login_body": login_response_body
    }

    requests.delete(f'{Url.base_url}{Url.delete_url}/{courier_id}')