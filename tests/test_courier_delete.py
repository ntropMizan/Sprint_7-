import pytest
import requests
import allure
from .data import API_PATHS, ERROR_MESSAGES

@allure.feature('Удаление курьера')
class TestCourierDelete:
    @allure.title('Успешное удаление курьера')
    def test_delete_courier_success(self, base_url, create_courier):
        login_data = {
            "login": create_courier["login"],
            "password": create_courier["password"]
        }
        auth_response = requests.post(f"{base_url}{API_PATHS['courier_login']}", data=login_data)
        courier_id = auth_response.json()["id"]
        
        response = requests.delete(f"{base_url}{API_PATHS['courier']}/{courier_id}")
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Удаление курьера без указания id')
    def test_delete_courier_without_id(self, base_url):
        response = requests.delete(f"{base_url}{API_PATHS['courier']}/")
        assert response.status_code == 404

    @allure.title('Удаление несуществующего курьера')
    def test_delete_nonexistent_courier(self, base_url):
        response = requests.delete(f"{base_url}{API_PATHS['courier']}/999999")
        assert response.status_code == 404
        assert ERROR_MESSAGES['courier_not_found'] in response.json()["message"] 