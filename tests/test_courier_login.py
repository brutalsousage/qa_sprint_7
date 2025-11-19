import pytest
import requests
import allure
from helpers import Help
from urls import BASE_URL, LOGIN_URL

@allure.title("Успешный логин курьера")
def test_login_success(courier_credentials):
    payload = courier_credentials
    
    response = requests.post(BASE_URL + LOGIN_URL, json=payload)
    
    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
    assert isinstance(response_data["id"], int) and response_data["id"] > 0

# @allure.title("Логин без поля login")
# def test_login_without_login():
#     payload = {
#         "password": "somepassword"
#     }
    
#     response = requests.post(BASE_URL + LOGIN_URL, json=payload)
    
#     if response.status_code == 504:
#         assert response.text == "Service unavailable"
#     else:
#         assert response.status_code == 400
#         assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"}

# @allure.title("Логин без поля password")
# def test_login_without_password():
#     payload = {
#         "login": "somelogin"
#     }
    
#     response = requests.post(BASE_URL + LOGIN_URL, json=payload)
    
#     if response.status_code == 504:
#         assert response.text == "Service unavailable"
#     else:
#         assert response.status_code == 400
#         assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"}

# @allure.title("Логин с неправильным логином")
# def test_login_wrong_login():
#     payload = {
#         "login": "wronglogin",
#         "password": "somepassword"
#     }
    
#     response = requests.post(BASE_URL + LOGIN_URL, json=payload)
    
#     assert response.status_code == 404
#     assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

# @allure.title("Логин с неправильным паролем")
# def test_login_wrong_password():
#     payload = {
#         "login": "somelogin",
#         "password": "wrongpassword"
#     }
    
#     response = requests.post(BASE_URL + LOGIN_URL, json=payload)
    
#     assert response.status_code == 404
#     assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

# @allure.title("Логин под несуществующим пользователем")
# def test_login_nonexistent_user():
#     payload = {
#         "login": Help.generate_random_string(20),
#         "password": Help.generate_random_string(20)
#     }
    
#     response = requests.post(BASE_URL + LOGIN_URL, json=payload)
    
#     assert response.status_code == 404
#     assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}
