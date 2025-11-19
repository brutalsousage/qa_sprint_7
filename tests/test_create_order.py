import pytest
import requests
import allure
from helpers import Help
from urls import BASE_URL, ORDER_URL

@pytest.mark.parametrize("test_case, color", [
    ("one_color_black", ["BLACK"]),
    ("one_color_grey", ["GREY"]),
    ("both_colors", ["BLACK", "GREY"]),
    ("no_color", None)
])
@allure.title("Создание заказа с цветом")
def test_create_order_with_colors(test_case, color):
    payload = Help.generate_order_payload(color=color)
    
    response = requests.post(BASE_URL + ORDER_URL, json=payload)
    
    assert response.status_code == 201, "Expected 201, got " + str(response.status_code) + ". Response: " + response.text
    response_data = response.json()
    assert "track" in response_data, "Track not found in response: " + str(response_data)
    assert isinstance(response_data["track"], int), "Track should be int, got " + str(type(response_data["track"]))
