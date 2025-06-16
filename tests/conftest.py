import pytest
import requests
import random
import string
from .data import BASE_URL, ORDER_DATA

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

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
    response = requests.post(f"{base_url}/api/v1/orders", json=ORDER_DATA)
    return response.json()["track"] 