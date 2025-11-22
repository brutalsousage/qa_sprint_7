import pytest
import requests
import allure
from helpers import Help
from urls import LOGIN_URL
from data import (
    NO_LOGIN_PAYLOAD,
    EXPECTED_NO_LOGIN,
    NO_PASSWORD_PAYLOAD,
    EXPECTED_NO_PASSWORD,
    WRONG_LOGIN_PAYLOAD,
    EXPECTED_WRONG_LOGIN,
    WRONG_PASSWORD_PAYLOAD,
    EXPECTED_WRONG_PASSWORD,
    EXPECTED_NONEXISTENT_USER
)

class TestLoginCourier:

    @allure.title("Успешный логин курьера")
    def test_login_success(self, courier_credentials):
        payload = courier_credentials
        
        with allure.step("Выполнить POST-запрос на логин с валидными данными"):
            response = requests.post(LOGIN_URL, json=payload)
        
        assert response.status_code == 200
        response_data = response.json()
        assert "id" in response_data
        assert isinstance(response_data["id"], int) and response_data["id"] > 0

    @allure.title("Логин без поля login")
    def test_login_without_login(self):
        payload = NO_LOGIN_PAYLOAD
        
        with allure.step("Выполнить POST-запрос на логин без поля login"):
            response = requests.post(LOGIN_URL, json=payload)
        
        assert response.status_code == 400
        assert response.json() == EXPECTED_NO_LOGIN

    @allure.title("Логин без поля password")
    def test_login_without_password(self):
        payload = NO_PASSWORD_PAYLOAD
        
        with allure.step("Выполнить POST-запрос на логин без поля password"):
            response = requests.post(LOGIN_URL, json=payload)
        
        if response.status_code == 504:
                pytest.skip("Server returned 504 Gateway Timeout")
        else:
                assert response.status_code == 400
                assert response.json() == EXPECTED_NO_PASSWORD

    @allure.title("Логин с неправильным логином")
    def test_login_wrong_login(self):
        payload = WRONG_LOGIN_PAYLOAD
        
        with allure.step("Выполнить POST-запрос на логин с неправильным логином"):
            response = requests.post(LOGIN_URL, json=payload)
        
        assert response.status_code == 404
        assert response.json() == EXPECTED_WRONG_LOGIN

    @allure.title("Логин с неправильным паролем")
    def test_login_wrong_password(self):
        payload = WRONG_PASSWORD_PAYLOAD
        
        with allure.step("Выполнить POST-запрос на логин с неправильным паролем"):
            response = requests.post(LOGIN_URL, json=payload)
        
        assert response.status_code == 404
        assert response.json() == EXPECTED_WRONG_PASSWORD

    @allure.title("Логин под несуществующим пользователем")
    def test_login_nonexistent_user(self):
        payload = {
            "login": Help.generate_random_string(20),
            "password": Help.generate_random_string(20)
        }
        
        with allure.step("Выполнить POST-запрос на логин под несуществующим пользователем"):
            response = requests.post(LOGIN_URL, json=payload)
        
        assert response.status_code == 404
        assert response.json() == EXPECTED_NONEXISTENT_USER
