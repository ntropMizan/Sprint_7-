import pytest
import requests

class TestCourierDelete:
    def test_delete_courier_success(self, base_url, create_courier):
        login_data = {
            "login": create_courier["login"],
            "password": create_courier["password"]
        }
        auth_response = requests.post(f"{base_url}/api/v1/courier/login", data=login_data)
        courier_id = auth_response.json()["id"]
        
        response = requests.delete(f"{base_url}/api/v1/courier/{courier_id}")
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    def test_delete_courier_without_id(self, base_url):
        response = requests.delete(f"{base_url}/api/v1/courier/")
        assert response.status_code == 404

    def test_delete_nonexistent_courier(self, base_url):
        response = requests.delete(f"{base_url}/api/v1/courier/999999")
        assert response.status_code == 404
        assert "Курьера с таким id нет" in response.json()["message"] 