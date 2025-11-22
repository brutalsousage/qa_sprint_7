import pytest
import requests
import allure
from urls import ORDER_URL
from helpers import Help
from data import (
    EXPECTED_GET_ORDERS_STATUS_SUCCESS,
    EXPECTED_GET_ORDERS_RESPONSE_KEYS,
    EXPECTED_PAGE_INFO_KEYS,
    EXPECTED_AVAILABLE_STATIONS_KEYS,
    REQUIRED_ORDER_FIELDS,
    EXPECTED_GET_ORDERS_STATUS_NOT_FOUND,
    EXPECTED_NOT_FOUND_MESSAGE_KEYWORD,
    GET_ORDERS_PARAMS_DEFAULT,
    GET_ORDERS_PARAMS_WITH_LIMIT
)

class TestGetOrders:

    @allure.title("Получение списка заказов успешно")
    @pytest.mark.parametrize("params", [
        GET_ORDERS_PARAMS_DEFAULT,
        GET_ORDERS_PARAMS_WITH_LIMIT,
    ])
    def test_get_orders_success(self, params):
        with allure.step(f"Выполнить GET-запрос на получение списка заказов с параметрами {params}"):
            response = requests.get(ORDER_URL, params=params)
        assert response.status_code == EXPECTED_GET_ORDERS_STATUS_SUCCESS
        response_data = response.json()
        for key in EXPECTED_GET_ORDERS_RESPONSE_KEYS:
            assert key in response_data
        assert isinstance(response_data["orders"], list)
        assert len(response_data["orders"]) > 0
        page_info = response_data["pageInfo"]
        for key in EXPECTED_PAGE_INFO_KEYS:
            assert key in page_info
            assert isinstance(page_info[key], int)
        available_stations = response_data["availableStations"]
        assert isinstance(available_stations, list)
        for station in available_stations:
            for key in EXPECTED_AVAILABLE_STATIONS_KEYS:
                assert key in station
        for order in response_data["orders"]:
            for field in REQUIRED_ORDER_FIELDS:
                assert field in order
            assert isinstance(order["id"], int)
            assert order["firstName"] is None or isinstance(order["firstName"], str)
            assert order["lastName"] is None or isinstance(order["lastName"], str)
            assert order["address"] is None or isinstance(order["address"], str)
            assert order["phone"] is None or isinstance(order["phone"], str)
            assert order["color"] is None or isinstance(order["color"], list)

    @allure.title("Получение заказов с несуществующим courierId")
    def test_get_orders_with_courier_id_not_found(self):
        params = {"courierId": 999999}
        with allure.step("Выполнить GET-запрос на получение заказов с несуществующим courierId"):
            response = requests.get(ORDER_URL, params=params)
        assert response.status_code == EXPECTED_GET_ORDERS_STATUS_NOT_FOUND
        response_data = response.json()
        assert "message" in response_data
        assert EXPECTED_NOT_FOUND_MESSAGE_KEYWORD in response_data["message"]

    @allure.title("Получение заказов с существующим courierId")
    def test_get_orders_with_courier_id_success(self):
        courier = Help.register_new_courier_and_return_login_password()
        assert courier is not None
        pytest.skip("Тест с courierId требует логина курьера для получения ID — пропускаю, пока не реализовано")
