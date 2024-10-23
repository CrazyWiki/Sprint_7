import allure
import pytest
import requests
from data import CouriersRegistred as data
from urls import Urls
from endpoint_handlers import Handle

class TestLoginCourier:
    @allure.title("Тест логин курьера")
    @allure.description("Позитивный тест")
    def test_login_courier(self):
        response = requests.post(f'{Urls.main_page}{Handle.login_courier}', data.data_positive)
        assert response.status_code == 200 and "id" in response.text

    @allure.title("Тест логин курьера")
    @allure.description("Негативный тест при отсутствии учетной записи")
    def test_login_courier_negative(self):
        response = requests.post(f'{Urls.main_page}{Handle.login_courier}', data.data_negative_courier_not_exist)
        assert response.status_code == 404 and "Учетная запись не найдена" in response.text

    @pytest.mark.parametrize('data_lost_parametr',[data.data_negative_lost_login,data.data_negative_lost_password])
    @allure.title("Тест логин курьера")
    @allure.description("Негативный тест при отсутствии данных")
    def test_login_courier_lost_data(self,data_lost_parametr):
        response = requests.post(f'{Urls.main_page}{Handle.login_courier}',data_lost_parametr)
        assert response.status_code == 400 and "Недостаточно данных для входа" in response.text


