class CouriersRegistred:
    data_positive = {"login": "mike123", "password": "1234"}
    data_negative_courier_not_exist = {"login": "Stop345", "password": "1234"}
    data_negative_lost_login = {"login": "", "password": "123456"}
    data_negative_lost_password = {"login": "mike123", "password": ""}


class OrderData:
    data_order_positive_1 = {
        "firstName": "Mike",
        "lastName": "Nike",
        "address": "Konoha, 142 apt.",
        "metroStation": 10,
        "phone": "+7 911 888 77 66",
        "rentTime": 4,
        "deliveryDate": "2024-11-01",
        "comment": "For my wife",
        "color": [
            "BLACK"
        ]
    }
    data_order_positive_2 = {
        "firstName": "Stan",
        "lastName": "Swan",
        "address": "Leninsky pr, 52, 62",
        "metroStation": 2,
        "phone": "+7 905 111 65 65",
        "rentTime": 2,
        "deliveryDate": "2024-12-01",
        "comment": "No comments",
        "color": [
            "GREY"
        ]
    }
    data_order_positive_3 = {
        "firstName": "First",
        "lastName": "One",
        "address": "Teganskaya, 143/2, 5",
        "metroStation": 5,
        "phone": "+7 911 888 77 66",
        "rentTime": 6,
        "deliveryDate": "2025-01-01",
        "comment": "Any color",
        "color": [
            "BLACK", "GREY"
        ]
    }
    data_order_positive_4 = {
        "firstName": "First",
        "lastName": "One",
        "address": "Teganskaya, 143/2, 5",
        "metroStation": 5,
        "phone": "+7 911 888 77 66",
        "rentTime": 6,
        "deliveryDate": "2025-01-01",
        "comment": "Any color"
    }