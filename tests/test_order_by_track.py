import pytest
import requests

class TestOrderByTrack:
    def test_get_order_by_track_success(self, base_url, create_order):
        response = requests.get(f"{base_url}/api/v1/orders/track?t={create_order}")
        assert response.status_code == 200
        assert "order" in response.json()

    def test_get_order_without_track(self, base_url):
        response = requests.get(f"{base_url}/api/v1/orders/track")
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    def test_get_order_with_nonexistent_track(self, base_url):
        response = requests.get(f"{base_url}/api/v1/orders/track?t=999999")
        assert response.status_code == 404
        assert response.json()["message"] == "Заказ не найден" 