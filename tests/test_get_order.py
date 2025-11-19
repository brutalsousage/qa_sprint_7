import pytest
import requests
import allure
from urls import BASE_URL, ORDER_URL
from helpers import Help

class TestGetOrders:

    @allure.title("Получение списка заказов успешно")
    @pytest.mark.parametrize("params", [
        {},
        {"limit": 10, "page": 0},
    ])
    def test_get_orders_success(self, params):
        response = requests.get(BASE_URL + ORDER_URL, params=params)
        assert response.status_code == 200
        response_data = response.json()
        assert "orders" in response_data
        assert "pageInfo" in response_data
        assert "availableStations" in response_data
        assert isinstance(response_data["orders"], list)
        assert len(response_data["orders"]) > 0
        page_info = response_data["pageInfo"]
        assert "page" in page_info
        assert "total" in page_info
        assert "limit" in page_info
        assert isinstance(page_info["page"], int)
        assert isinstance(page_info["total"], int)
        assert isinstance(page_info["limit"], int)
        available_stations = response_data["availableStations"]
        assert isinstance(available_stations, list)
        if len(available_stations) > 0:
            for station in available_stations:
                assert "name" in station
                assert "number" in station
                assert "color" in station
        for order in response_data["orders"]:
            required_fields = ["id", "courierId", "firstName", "lastName", "address", "metroStation", "phone", "rentTime", "deliveryDate", "track", "color", "comment", "createdAt", "updatedAt", "status"]
            for field in required_fields:
                assert field in order
            assert isinstance(order["id"], int)
            if order["firstName"] is not None:
                assert isinstance(order["firstName"], str)
            if order["lastName"] is not None:
                assert isinstance(order["lastName"], str)
            if order["address"] is not None:
                assert isinstance(order["address"], str)
            if order["phone"] is not None:
                assert isinstance(order["phone"], str)
            if order["color"] is not None:
                assert isinstance(order["color"], list)

    @allure.title("Получение заказов с несуществующим courierId")
    def test_get_orders_with_courier_id_not_found(self):
        params = {"courierId": 999999}
        response = requests.get(BASE_URL + "/api/v1/orders", params=params)
        assert response.status_code == 404
        response_data = response.json()
        assert "message" in response_data
        assert "не найден" in response_data["message"]

    @allure.title("Получение заказов с существующим courierId")
    def test_get_orders_with_courier_id_success(self):
        courier = Help.register_new_courier_and_return_login_password()
        assert courier is not None
        pytest.skip("Тест с courierId требует логина курьера для получения ID — пропускаю, пока не реализовано")
