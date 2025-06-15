import pytest
import requests

class TestCourierCreation:
    def test_create_courier_success(self, base_url, generate_courier_data):
        response = requests.post(f"{base_url}/api/v1/courier", data=generate_courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    def test_create_duplicate_courier(self, base_url, create_courier):
        response = requests.post(f"{base_url}/api/v1/courier", data=create_courier)
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json()["message"]

    def test_create_courier_without_required_fields(self, base_url):
        courier_data = {"login": "test"}
        response = requests.post(f"{base_url}/api/v1/courier", data=courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    def test_create_courier_with_empty_fields(self, base_url):
        courier_data = {"login": "", "password": "", "firstName": ""}
        response = requests.post(f"{base_url}/api/v1/courier", data=courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи" 