from data import generate_courier_body
from methods.courier_methods import CourierMethods
import allure

from tests.conftest import generate_courier_data


class TestCreateCourier:
    @allure.title('Успешное создание нового курьера с передачей всех обязательных полей')
    def test_create_new_courier(self, generate_courier_data):
        expected_response = {
            "ok": True
        }
        assert generate_courier_data['create_status_code'] == 201 and generate_courier_data['create_body'] == expected_response

    @allure.title('Проверка невозможности создания двух курьеров с одинаковым логином, паролем и именем')
    def test_create_courier_twice(self, generate_courier_data):
        response_first_status_code = generate_courier_data['create_status_code']
        response_first_data = generate_courier_data['create_body']
        response_second = CourierMethods.create_courier({
            "login": generate_courier_data['login'],
            "password": generate_courier_data['password'],
            "first_name": generate_courier_data['first_name']
        })
        response_second_data = response_second.json()
        expected_first_response = {
            "ok": True
        }
        expected_second_response = {
            'code': 409,
            'message': 'Этот логин уже используется. Попробуйте другой.'
        }
        assert response_first_status_code == 201 and response_first_data == expected_first_response
        assert response_second.status_code == 409 and response_second_data == expected_second_response

    @allure.title('Проверка невозможности создания курьера без заполненного поля логин')
    def test_create_courier_without_name(self):
        courier_data = generate_courier_body()
        del courier_data["login"]
        response = CourierMethods.create_courier(courier_data)
        response_data = response.json()
        expected_response = {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
        assert response.status_code == 400 and response_data == expected_response

    @allure.title('Проверка невозможности создания курьера без заполненного поля пароль')
    def test_create_courier_without_password(self):
        courier_data = generate_courier_body()
        del courier_data["password"]
        response = CourierMethods.create_courier(courier_data)
        response_data = response.json()
        expected_response = {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
        assert response.status_code == 400 and response_data == expected_response

    @allure.title('Проверка невозможности создания курьера с одинаковым логином')
    def test_create_courier_with_the_same_login(self, generate_courier_data):
        response_first_status_code = generate_courier_data['create_status_code']
        response_first_data = generate_courier_data['create_body']
        second_courier_data = generate_courier_body()
        response_second = CourierMethods.create_courier({
            "login": generate_courier_data['login'],
            "password": second_courier_data['password'],
            "first_name": second_courier_data['firstName']
        })
        response_second_data = response_second.json()
        expected_first_response = {
            "ok": True
        }
        expected_second_response = {
            'code': 409,
            'message': 'Этот логин уже используется. Попробуйте другой.'
        }
        assert response_first_status_code == 201 and response_first_data == expected_first_response
        assert response_second.status_code == 409 and response_second_data == expected_second_response