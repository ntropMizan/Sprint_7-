import pytest
import requests

class TestOrderCreation:
    @pytest.mark.parametrize('color', [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, base_url, color):
        order_data = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "Москва, ул. Пушкина, д. 1",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-03-20",
            "comment": "Тестовый заказ",
            "color": color
        }
        response = requests.post(f"{base_url}/api/v1/orders", json=order_data)
        assert response.status_code == 201
        assert "track" in response.json()

    def test_create_order_without_required_fields(self, base_url):
        """Проверка создания заказа без обязательных полей"""
        order_data = {
            "firstName": "John",
            "lastName": "Doe",
            "address": "123 Main St",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-03-20",
            "comment": "Test order"
            # color отсутствует
        }
        response = requests.post(f"{base_url}/api/v1/orders", json=order_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания заказа"

    def test_create_order_with_empty_fields(self, base_url):
        """Проверка создания заказа с пустыми полями"""
        order_data = {
            "firstName": "",
            "lastName": "",
            "address": "",
            "metroStation": 4,
            "phone": "",
            "rentTime": 5,
            "deliveryDate": "2024-03-20",
            "comment": "",
            "color": []
        }
        response = requests.post(f"{base_url}/api/v1/orders", json=order_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания заказа" 