import pytest
import requests

class TestOrderList:
    def test_get_order_list(self, base_url):
        response = requests.get(f"{base_url}/api/v1/orders")
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)

    def test_get_order_list_with_limit(self, base_url):
        params = {"limit": 5}
        response = requests.get(f"{base_url}/api/v1/orders", params=params)
        assert response.status_code == 200
        assert len(response.json()["orders"]) <= 5

    def test_get_order_list_with_page(self, base_url):
        params = {"page": 1}
        response = requests.get(f"{base_url}/api/v1/orders", params=params)
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)

    def test_get_order_list_with_invalid_params(self, base_url):
        """Проверка получения списка заказов с некорректными параметрами"""
        response = requests.get(f"{base_url}/api/v1/orders", params={"limit": -1, "page": -1})
        assert response.status_code == 400
        assert response.json()["message"] == "Некорректные параметры запроса" 