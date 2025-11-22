import pytest
import requests
import allure
from helpers import Help
from urls import COURIER_URL
from data import (
    SUCCESS_CREATE_RESPONSE,
    DUPLICATE_CREATE_RESPONSE,
    MISSING_DATA_CREATE_RESPONSE,
    WITHOUT_LOGIN_PAYLOAD,
    WITHOUT_PASSWORD_PAYLOAD,
    MISSING_MULTIPLE_FIELDS_PAYLOAD
)

class TestCreateCourier:

    @allure.title("Создание курьера успешно")
    def test_create_courier_success(self):
        login = Help.generate_random_string(15)
        password = Help.generate_random_string(15)
        first_name = Help.generate_random_string(15)
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        
        with allure.step("Выполнить POST-запрос на создание курьера с полными данными"):
            response = requests.post(COURIER_URL, json=payload)
        
        assert response.status_code == 201
        assert response.json() == SUCCESS_CREATE_RESPONSE

    @allure.title("Создание курьера без firstName")
    def test_create_courier_without_firstname(self):
        login = Help.generate_random_string(15)
        password = Help.generate_random_string(15)
        
        payload = {
            "login": login,
            "password": password
        }
        
        with allure.step("Выполнить POST-запрос на создание курьера без firstName"):
            response = requests.post(COURIER_URL, json=payload)
        assert response.status_code == 201
        assert response.json() == SUCCESS_CREATE_RESPONSE

    @allure.title("Создание курьера с дубликатом логина")
    def test_create_duplicate_courier(self, create_courier):
        login, _, _ = create_courier
        password = Help.generate_random_string(15)
        first_name = Help.generate_random_string(15)
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        
        with allure.step("Выполнить POST-запрос на создание курьера с дубликатом логина"):
            response = requests.post(COURIER_URL, json=payload)
        assert response.status_code == 409
        assert response.json() == DUPLICATE_CREATE_RESPONSE

    @allure.title("Создание курьера без обязательных полей")
    @pytest.mark.parametrize("payload", [
        WITHOUT_LOGIN_PAYLOAD,
        WITHOUT_PASSWORD_PAYLOAD,
        MISSING_MULTIPLE_FIELDS_PAYLOAD,
    ])
    def test_create_courier_missing_fields(self, payload):
        with allure.step("Выполнить POST-запрос на создание курьера без обязательных полей"):
            response = requests.post(COURIER_URL, json=payload) 
        assert response.status_code == 400
        assert response.json() == MISSING_DATA_CREATE_RESPONSE
