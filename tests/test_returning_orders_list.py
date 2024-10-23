import requests
import allure
from urls import Urls
from endpoint_handlers import Handle
import methods_api
class TestReturningOrdersList:
    @allure.title('Список заказов')
    @allure.description('Получение списка из последних 30 заказов')
    def test_order_list(self):
        response = methods_api.return_order_list(15)
        assert response.status_code == 200