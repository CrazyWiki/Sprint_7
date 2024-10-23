import allure
import requests
from fake_data_generator import CourierFakeDataGenerator as data_generator
from data import CouriersRegistred as data
from urls import Urls
from endpoint_handlers import Handle

class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Успешное создание')
    def test_create_courier(self):
        response = requests.post(f'{Urls.main_page}{Handle.create_courier}',data_generator.register_courier_full_data())
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Создание курьера')
    @allure.description('Попытка создания курьера с уже существующим логином')
    def test_create_courier_with_same_date(self):
        response = requests.post(f'{Urls.main_page}{Handle.create_courier}', data.data_positive)
        assert response.status_code == 409 and "Этот логин уже используется. Попробуйте другой." in response.text

    @allure.title('Попытка создание курьера без логина')
    @allure.description('Ошибка - Недостаточно данных для создания учетной записи')
    def test_create_courier_lost_login(self):
        response = requests.post(f'{Urls.main_page}{Handle.create_courier}',data_generator.register_courier_lost_login())
        assert response.status_code == 400 and "Недостаточно данных для создания учетной записи" in response.text


    @allure.title('Попытка создание курьера без пароля')
    @allure.description('Ошибка - Недостаточно данных для создания учетной записи')
    def test_create_courier_lost_password(self):
        response = requests.post(f'{Urls.main_page}{Handle.create_courier}', data_generator.register_courier_data_lost_password())
        assert response.status_code == 400 and "Недостаточно данных для создания учетной записи" in response.text

    @allure.title('Создание курьера')
    @allure.description('Успешное создание без данных об имени')
    def test_create_courier_lost_name(self):
        response = requests.post(f'{Urls.main_page}{Handle.create_courier}', data_generator.register_courier_data_lost_name())
        assert response.status_code == 201 and response.text == '{"ok":true}'
