import requests
from data import Url


class CourierMethods:
    @staticmethod
    def create_courier(body):
        return requests.post(f'{Url.base_url}{Url.courier_url}', json=body)

    @staticmethod
    def login_courier(body):
        return requests.post(f'{Url.base_url}{Url.login_url}', json=body)

    @staticmethod
    def make_an_order(body):
        return requests.post(f'{Url.base_url}{Url.order_url}', json=body)

    @staticmethod
    def order_list():
        return requests.get(f'{Url.base_url}{Url.order_url}')





