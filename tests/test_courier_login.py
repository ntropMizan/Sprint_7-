import pytest
import requests

class TestCourierLogin:
    def test_login_success(self, base_url, create_courier):
        login_data = {
            "login": create_courier["login"],
            "password": create_courier["password"]
        }
        response = requests.post(f"{base_url}/api/v1/courier/login", data=login_data)
        assert response.status_code == 200
        assert "id" in response.json()

    def test_login_without_required_fields(self, base_url):
        """Проверка входа без обязательных полей"""
        courier_data = {
            "login": "test_courier",
            # password отсутствует
        }
        response = requests.post(f"{base_url}/api/v1/courier/login", json=courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    def test_login_with_wrong_credentials(self, base_url):
        login_data = {
            "login": "nonexistent",
            "password": "wrong"
        }
        response = requests.post(f"{base_url}/api/v1/courier/login", data=login_data)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    def test_login_with_empty_fields(self, base_url):
        login_data = {"login": "", "password": ""}
        response = requests.post(f"{base_url}/api/v1/courier/login", data=login_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа" 