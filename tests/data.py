# Базовый URL API
BASE_URL = "https://qa-scooter.praktikum-services.ru"

# Тестовые данные для заказа
ORDER_DATA = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "Москва, ул. Пушкина, д. 1",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-03-20",
    "comment": "Тестовый заказ"
}

# Сообщения об ошибках
ERROR_MESSAGES = {
    "duplicate_login": "Этот логин уже используется",
    "courier_not_found": "Курьер не найден",
    "order_not_found": "Заказ не найден",
    "insufficient_data": "Недостаточно данных для создания учетной записи"
}

# Пути API
API_PATHS = {
    "courier": "/api/v1/courier",
    "courier_login": "/api/v1/courier/login",
    "orders": "/api/v1/orders",
    "accept_order": "/api/v1/orders/accept/",
    "order_by_track": "/api/v1/orders/track"
} 