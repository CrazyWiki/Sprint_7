import requests
from fake_data_generator import CourierFakeDataGenerator as data_generator
from urls import Urls
from endpoint_handlers import Handle
def return_order_list(entries_number):
    response = requests.get(f'{Urls.main_page}{Handle.create_order}/?limit={entries_number}')
    return response
def get_last_order_id():
    response = return_order_list(1)
    data = response.json()
    first_id = data['orders'][0]['id']
    return first_id

def get_courier_id():
    data_example = data_generator.register_courier_full_data()
    response_create_courier = requests.post(f'{Urls.main_page}{Handle.create_courier}', data_example)
    assert response_create_courier.status_code == 201
    response_login = requests.post(f'{Urls.main_page}{Handle.login_courier}', data_example)
    assert response_login.status_code == 200
    id = int(response_login.text.split(':')[1].rstrip('}'))
    return id
def get_order_track():
    response = return_order_list(1)
    data = response.json()
    first_track = data['orders'][0]['track']
    return first_track


