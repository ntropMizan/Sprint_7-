import pytest
import requests
import allure
from .data import API_PATHS, ERROR_MESSAGES

@allure.feature('Получение заказа по треку')
class TestOrderByTrack:
    @allure.title('Успешное получение заказа по треку')
    def test_get_order_by_track_success(self, base_url, create_order):
        response = requests.get(f"{base_url}{API_PATHS['order_by_track']}?t={create_order}")
        assert response.status_code == 200
        assert "order" in response.json()

    @allure.title('Получение заказа без указания трека')
    def test_get_order_without_track(self, base_url):
        response = requests.get(f"{base_url}{API_PATHS['order_by_track']}")
        assert response.status_code == 400
        assert response.json()["message"] == ERROR_MESSAGES['insufficient_data']

    @allure.title('Получение заказа по несуществующему треку')
    def test_get_order_with_nonexistent_track(self, base_url):
        response = requests.get(f"{base_url}{API_PATHS['order_by_track']}?t=999999")
        assert response.status_code == 404
        assert response.json()["message"] == ERROR_MESSAGES['order_not_found'] 