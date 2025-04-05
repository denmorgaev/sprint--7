import allure

from methods.courier_methods import CourierMethods


class OrderList:
    @allure.title('Успешное получение списка заказов')
    def test_get_order_list(self):
        response = CourierMethods.order_list()
        response_data = response.json()
        assert response.status_code == 200 and 'orders' in response_data