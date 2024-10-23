import allure
import pytest
import requests
import methods_api
from urls import Urls
from endpoint_handlers import Handle

@pytest.fixture(scope='session')
def get_id_order():
    return methods_api.get_last_order_id()

@pytest.fixture(scope='session')
def get_id_courier():
    return methods_api.get_courier_id()
class TestAcceptOrder:
    @allure.title("Тест принятия заказа курьером")
    @allure.description('Проверка назначения на полученный id заказа курьера  ')
    def test_accept_order_positive(self, get_id_order, get_id_courier):
        id_order = get_id_order
        id_courier = get_id_courier
        response_accept_order = requests.put(f'{Urls.main_page}{Handle.accept_order}{id_order}?courierId={id_courier}')
        assert response_accept_order.status_code == 200 and '"ok":true' in response_accept_order.text

    @pytest.mark.parametrize("id_order",["", 373])
    @allure.title("Негативный ест приятия заказа курьером")
    @allure.description('id заказа неверный и пустой ')
    def test_accept_order_negative_data_id_order(self,get_id_courier,id_order):
        id_order=""
        id_courier = get_id_courier
        response_accept_order = requests.put(f'{Urls.main_page}{Handle.accept_order}{id_order}?courierId={id_courier}')
        assert response_accept_order.status_code in (400,404) and '"ok":true' not in response_accept_order.text

    @pytest.mark.parametrize("id_courier", ["", 373])
    @allure.title("Негативный ест приятия заказа курьером")
    @allure.description('id курьера неверный и пустой ')
    def test_accept_order_negative_data_id_courier(self, get_id_order,id_courier):
        id_order = get_id_order
        response_accept_order = requests.put(f'{Urls.main_page}{Handle.accept_order}{id_order}?courierId={id_courier}')
        assert response_accept_order.status_code in (400,404) and '"ok":true' not in response_accept_order.text
