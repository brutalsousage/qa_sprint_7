import pytest
import requests
import allure
from helpers import Help
from urls import BASE_URL, COURIER_URL

def test_create_courier_success():
    login = Help.generate_random_string(15)
    password = Help.generate_random_string(15)
    first_name = Help.generate_random_string(15)
    
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    response = requests.post(BASE_URL + COURIER_URL, json=payload)
    
    assert response.status_code == 201
    assert response.json() == {"ok": True}

@allure.title("Создание курьера без firstName")
def test_create_courier_without_firstname():
    login = Help.generate_random_string(15)
    password = Help.generate_random_string(15)
    
    payload = {
        "login": login,
        "password": password
    }
    
    response = requests.post(BASE_URL + COURIER_URL, json=payload)
    
    assert response.status_code == 201
    assert response.json() == {"ok": True}

@allure.title("Создание курьера с дубликатом логина")
def test_create_duplicate_courier(create_courier):
    login, _, _ = create_courier
    password = Help.generate_random_string(15)
    first_name = Help.generate_random_string(15)
    
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    response = requests.post(BASE_URL + COURIER_URL, json=payload)
    
    assert response.status_code == 409
    assert response.json() == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}

@allure.title("Создание курьера без login")
def test_create_courier_without_login():
    payload = {
        "password": "testpass",
        "firstName": "testname"
    }
    
    response = requests.post(BASE_URL + COURIER_URL, json=payload)
    
    assert response.status_code == 400
    assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}

@allure.title("Создание курьера без password")
def test_create_courier_without_password():
    payload = {
        "login": "testlogin",
        "firstName": "testname"
    }
    
    response = requests.post(BASE_URL + COURIER_URL, json=payload)
    
    assert response.status_code == 400
    assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}

@allure.title("Создание курьера без нескольких полей")
def test_create_courier_missing_multiple_fields():
    payload = {
        "firstName": "testname"
    }
    
    response = requests.post(BASE_URL + COURIER_URL, json=payload)
    
    assert response.status_code == 400
    assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
