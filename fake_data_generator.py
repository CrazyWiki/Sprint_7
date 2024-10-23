from faker import Faker


class CourierFakeDataGenerator:
    @staticmethod
    def register_courier_full_data():
        fake = Faker()
        login = fake.user_name()
        password = fake.password()
        firstName = fake.first_name()
        fake_registration_data = {"login": f'{login}', "password": f'{password}', "firstName": f'{firstName}'}
        return fake_registration_data

    @staticmethod
    def register_courier_lost_login():
        fake = Faker()
        password = fake.password()
        firstName = fake.first_name()
        fake_registration_data = {"password": f'{password}', "firstName": f'{firstName}'}
        return fake_registration_data
    @staticmethod
    def register_courier_data_lost_name():
        fake = Faker()
        login = fake.user_name()
        password = fake.password()
        fake_registration_data = {"login": login, "password": password}
        return fake_registration_data

    @staticmethod
    def register_courier_data_lost_password():
        fake = Faker()
        login = fake.user_name()
        firstName = fake.first_name()
        fake_registration_data = {"login": login, "firstName": firstName}
        return fake_registration_data

