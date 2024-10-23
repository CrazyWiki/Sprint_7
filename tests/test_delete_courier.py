import allure
import requests
import methods_api
from urls import Urls
from endpoint_handlers import Handle
class TestDeleteCourier:
    @allure.title('Удаление курьера')
    @allure.description('Создание курьера, получение id, удаление курьера ')
    def test_delete_courier(self):
        courier_id=methods_api.get_courier_id()
        load = {"id": courier_id}
        response_delete = requests.delete(f'{Urls.main_page}{Handle.create_courier}/{courier_id}',json=load)
        assert response_delete.status_code == 200 and "ok" in response_delete.text

    @allure.title('Удаление курьера негативный сценарий')
    @allure.description('Удаление курьера с несуществующим id')
    def test_delete_courier_id_not_exist(self):
        numbers = 12345
        load = {"id": 12345}
        response_delete = requests.delete(f'{Urls.main_page}{Handle.create_courier}/{numbers}',json=load)
        assert response_delete.status_code == 404 and "Курьера с таким id нет" in response_delete.text


    @allure.title('Удаление курьера негативный сценарий')
    @allure.description('Удаление курьера без id')
    def test_delete_courier_without_id(self):
        numbers = ""
        load = {"id":"numbers" }
        response_delete = requests.delete(f'{Urls.main_page}{Handle.create_courier}/{numbers}', json=load)
        assert response_delete.status_code == 404

