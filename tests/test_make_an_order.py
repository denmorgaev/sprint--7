import pytest
import allure

from data import credentials_1, credentials_2, credentials_3, credentials_4
from methods.courier_methods import CourierMethods



class TestMakeAnOrder:
    @allure.title('Успешное создание заказа')
    @pytest.mark.parametrize('credentials', [credentials_1, credentials_2, credentials_3, credentials_4])
    def test_make_an_successful_order(self, credentials):
        response = CourierMethods.make_an_order(credentials)
        response_data = response.json()
        assert response.status_code == 201 and 'track' in response_data



