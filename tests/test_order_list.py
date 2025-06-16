import pytest
import requests
import allure
from .data import API_PATHS

@allure.feature('Получение списка заказов')
class TestOrderList:
    @allure.title('Получение списка заказов')
    def test_get_order_list(self, base_url):
        response = requests.get(f"{base_url}{API_PATHS['orders']}")
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)

    @allure.title('Получение списка заказов с лимитом')
    def test_get_order_list_with_limit(self, base_url):
        params = {"limit": 5}
        response = requests.get(f"{base_url}{API_PATHS['orders']}", params=params)
        assert response.status_code == 200
        assert len(response.json()["orders"]) <= 5

    @allure.title('Получение списка заказов с пагинацией')
    def test_get_order_list_with_page(self, base_url):
        params = {"page": 1}
        response = requests.get(f"{base_url}{API_PATHS['orders']}", params=params)
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)

    @allure.title('Получение списка заказов с некорректными параметрами')
    def test_get_order_list_with_invalid_params(self, base_url):
        """Проверка получения списка заказов с некорректными параметрами"""
        response = requests.get(f"{base_url}{API_PATHS['orders']}", params={"limit": -1, "page": -1})
        assert response.status_code == 400
        assert response.json()["message"] == "Некорректные параметры запроса" 