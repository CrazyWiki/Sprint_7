import allure
import requests
import methods_api
from urls import Urls
from endpoint_handlers import Handle

class TestGetOrderByTrack:
    @allure.title("Получение заказа по номеру")
    @allure.description('Позитивный тест получения заказа по его номеру ')
    def test_get_order_by_track_positive(self):
        track=methods_api.get_order_track()
        response= requests.get(f'{Urls.main_page}{Handle.get_order}?t={track}')
        response_json_track = response.json()['order']['track']
        assert response.status_code == 200 and response_json_track == track

    @allure.title("Получение заказа по номеру негативный сценарий")
    @allure.description('Негативный тест получения заказа по его номеру - пустой номер ')
    def test_get_order_by_track_negative_empty_track(self):
        track=""
        response = requests.get(f'{Urls.main_page}{Handle.get_order}?t={track}')
        assert response.status_code == 400 and "Недостаточно данных для поиска" in response.text

    @allure.title("Получение заказа по номеру негативный сценарий")
    @allure.description('Негативный тест получения заказа по его номеру -  несуществующий номер ')
    def test_get_order_by_track_positive(self):
        track = 1322
        response = requests.get(f'{Urls.main_page}{Handle.get_order}?t={track}')
        assert response.status_code == 404 and "Заказ не найден" in response.text