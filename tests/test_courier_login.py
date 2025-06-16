import pytest
import requests
import allure
from .data import API_PATHS, ERROR_MESSAGES

@allure.feature('Авторизация курьера')
class TestCourierLogin:
    @allure.title('Успешная авторизация курьера')
    def test_login_success(self, base_url, create_courier):
        login_data = {
            "login": create_courier["login"],
            "password": create_courier["password"]
        }
        response = requests.post(f"{base_url}{API_PATHS['courier_login']}", data=login_data)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title('Авторизация без обязательных полей')
    def test_login_without_required_fields(self, base_url):
        courier_data = {
            "login": "test_courier",
            # password отсутствует
        }
        response = requests.post(f"{base_url}{API_PATHS['courier_login']}", json=courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == ERROR_MESSAGES['insufficient_data']

    @allure.title('Авторизация с неверными учетными данными')
    def test_login_with_wrong_credentials(self, base_url):
        login_data = {
            "login": "nonexistent",
            "password": "wrong"
        }
        response = requests.post(f"{base_url}{API_PATHS['courier_login']}", data=login_data)
        assert response.status_code == 404
        assert response.json()["message"] == ERROR_MESSAGES['courier_not_found']

    @allure.title('Авторизация с пустыми полями')
    def test_login_with_empty_fields(self, base_url):
        login_data = {"login": "", "password": ""}
        response = requests.post(f"{base_url}{API_PATHS['courier_login']}", data=login_data)
        assert response.status_code == 400
        assert response.json()["message"] == ERROR_MESSAGES['insufficient_data'] 