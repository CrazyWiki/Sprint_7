import json
import pytest
import requests
import allure
from data import OrderData as data_order
from urls import Urls
from endpoint_handlers import Handle
class TestCreateOrder:
    @pytest.mark.parametrize('data_order_positive', [data_order.data_order_positive_1, data_order.data_order_positive_2, data_order.data_order_positive_3, data_order.data_order_positive_4])
    @allure.title("Тест создание заказа")
    @allure.description('Создание заказа с вариациями цветов')
    def test_create_order(self, data_order_positive):
        data_order_positive = json.dumps(data_order_positive)
        response = requests.post(f'{Urls.main_page}{Handle.create_order}', data=data_order_positive, headers = {'Content-Type': 'application/json'})
        assert response.status_code == 201 and ('track') in response.text
