import pytest
import requests
import allure
from helpers import Help
from urls import ORDER_URL
from data import (
    ORDER_COLORS,
    EXPECTED_ORDER_STATUS,
    EXPECTED_ORDER_TRACK_KEY
)

class TestCreateOrder:

    @pytest.mark.parametrize("test_case, color", ORDER_COLORS.items())
    @allure.title("Создание заказа с цветом")
    def test_create_order_with_colors(self, test_case, color):
        payload = Help.generate_order_payload(color=color)
        
        with allure.step(f"Выполнить POST-запрос на создание заказа с цветом {color}"):
            response = requests.post(ORDER_URL, json=payload)
        
        assert response.status_code == EXPECTED_ORDER_STATUS, "Expected " + str(EXPECTED_ORDER_STATUS) + ", got " + str(response.status_code) + ". Response: " + response.text
        response_data = response.json()
        assert EXPECTED_ORDER_TRACK_KEY in response_data, "Track not found in response: " + str(response_data)
        assert isinstance(response_data[EXPECTED_ORDER_TRACK_KEY], int), "Track should be int, got " + str(type(response_data[EXPECTED_ORDER_TRACK_KEY]))
