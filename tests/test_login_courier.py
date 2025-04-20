import allure

from data import generate_courier_body
from methods.courier_methods import CourierMethods


class TestLoginCourier:
    @allure.title('Успешная авторизация созданного курьера c передачей всех обязательных полей')
    def test_successful_login_courier(self, generate_courier_data):
        login_data = {
            "login": generate_courier_data['login'],
            "password": generate_courier_data['password']
        }

        with allure.step("Авторизуемся как курьер"):
            response = CourierMethods.login_courier(login_data)
            response_data = response.json()

        assert response.status_code == 200 and "id" in response_data

    @allure.title('Получение ошибки при вводе некорректного логина')
    def test_login_with_wrong_login(self, generate_courier_data):
        second_courier_data = generate_courier_body()
        wrong_courier_data = {
            "login": second_courier_data['login'],
            "password": generate_courier_data['password']
        }
        response = CourierMethods.login_courier(wrong_courier_data)
        response_data = response.json()
        expected_response = {
            'code': 404,
            'message': 'Учетная запись не найдена'
        }
        assert response.status_code == 404 and response_data == expected_response

    @allure.title('Получение ошибки при вводе некорректного пароля')
    def test_login_with_wrong_password(self, generate_courier_data):
        second_courier_data = generate_courier_body()
        wrong_courier_data = {
            "login": generate_courier_data['login'],
            "password": second_courier_data['password']
        }
        response = CourierMethods.login_courier(wrong_courier_data)
        response_data = response.json()
        expected_response = {
            'code': 404,
            'message': 'Учетная запись не найдена'
        }
        assert response.status_code == 404 and response_data == expected_response

    @allure.title('Получение ошибки при отправке запроса без обязательного поля логин')
    def test_login_without_login(self, generate_courier_data):
        second_courier_data = generate_courier_body()
        wrong_courier_data = {
            "password": second_courier_data['password']
        }
        response = CourierMethods.login_courier(wrong_courier_data)
        response_data = response.json()
        expected_response = {
            'code': 400,
            'message': 'Недостаточно данных для входа'
        }
        assert response.status_code == 400 and response_data == expected_response

    @allure.title('Получение ошибки при отправке запроса без обязательного поля пароль')
    def test_login_without_password(self, generate_courier_data):
        second_courier_data = generate_courier_body()
        wrong_courier_data = {
            "login": second_courier_data['login']
        }
        response = CourierMethods.login_courier(wrong_courier_data)
        response_data = response.json()
        expected_response = {
            'code': 400,
            'message': 'Недостаточно данных для входа'
        }
        assert response.status_code == 400 and response_data == expected_response

    @allure.title('Получение ошибки при авторизации с несуществующим логином')
    def test_login_with_wrong_password(self, generate_courier_data):
        second_courier_data = generate_courier_body()
        wrong_courier_data = {
            "login": second_courier_data['login'],
            "password": generate_courier_data['password']
        }
        response = CourierMethods.login_courier(wrong_courier_data)
        response_data = response.json()
        expected_response = {
            'code': 404,
            'message': 'Учетная запись не найдена'
        }
        assert response.status_code == 404 and response_data == expected_response