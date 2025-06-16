import pytest
import requests
import allure
from .data import API_PATHS, ERROR_MESSAGES

@allure.feature('Создание курьера')
class TestCourierCreation:
    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self, base_url, generate_courier_data):
        response = requests.post(f"{base_url}{API_PATHS['courier']}", data=generate_courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Создание курьера с существующим логином')
    def test_create_duplicate_courier(self, base_url, create_courier):
        response = requests.post(f"{base_url}{API_PATHS['courier']}", data=create_courier)
        assert response.status_code == 409
        assert ERROR_MESSAGES['duplicate_login'] in response.json()["message"]

    @allure.title('Создание курьера без обязательных полей')
    def test_create_courier_without_required_fields(self, base_url):
        courier_data = {"login": "test"}
        response = requests.post(f"{base_url}{API_PATHS['courier']}", data=courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == ERROR_MESSAGES['insufficient_data']

    @allure.title('Создание курьера с пустыми полями')
    def test_create_courier_with_empty_fields(self, base_url):
        courier_data = {"login": "", "password": "", "firstName": ""}
        response = requests.post(f"{base_url}{API_PATHS['courier']}", data=courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == ERROR_MESSAGES['insufficient_data'] 