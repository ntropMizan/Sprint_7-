import pytest
import requests
import random
import string

@pytest.fixture(scope="session")
def base_url():
    return "https://qa-scooter.praktikum-services.ru"

@pytest.fixture
def generate_courier_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }

@pytest.fixture
def create_courier(base_url, generate_courier_data):
    courier_data = generate_courier_data
    response = requests.post(f"{base_url}/api/v1/courier", data=courier_data)
    yield courier_data
    if response.status_code == 201:
        login_data = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        auth_response = requests.post(f"{base_url}/api/v1/courier/login", data=login_data)
        if auth_response.status_code == 200:
            courier_id = auth_response.json()["id"]
            requests.delete(f"{base_url}/api/v1/courier/{courier_id}")

@pytest.fixture
def create_order(base_url):
    order_data = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, ул. Пушкина, д. 1",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-03-20",
        "comment": "Тестовый заказ"
    }
    response = requests.post(f"{base_url}/api/v1/orders", json=order_data)
    return response.json()["track"] 