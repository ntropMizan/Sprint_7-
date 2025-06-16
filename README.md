# Yandex Scooter API Tests

Этот проект содержит автоматизированные тесты для API сервиса Яндекс Самокат.

## Установка

1. Клонируйте репозиторий
2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск тестов

Для запуска всех тестов:
```bash
pytest --alluredir=./allure-results
```

Для генерации отчета Allure:
```bash
allure serve allure-results
```

## Структура проекта

- `tests/` - директория с тестами
- `data/` - тестовые данные
- `requirements.txt` - зависимости проекта 