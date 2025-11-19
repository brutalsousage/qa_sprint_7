import requests
import random
import string
from datetime import datetime, timedelta
from urls import BASE_URL, COURIER_URL

class Help:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    
    @staticmethod
    def register_new_courier_and_return_login_password():
        login = Help.generate_random_string(10)
        password = Help.generate_random_string(10)
        first_name = Help.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(BASE_URL + COURIER_URL, json=payload)

        if response.status_code == 201:
            return {
                "login": login,
                "password": password,
                "first_name": first_name
            }
        else:
            return None
        
    @staticmethod
    def generate_order_payload(color=None):
        first_name = Help.generate_random_string(8)
        last_name = Help.generate_random_string(8)
        address = f"{Help.generate_random_string(10)}, {random.randint(1, 100)} apt."
        metro_station = random.randint(1, 237)
        phone = f"+7 {random.randint(800, 999)} {random.randint(100, 999)} {random.randint(10, 99)} {random.randint(10, 99)}"
        rent_time = random.randint(1, 30)
        delivery_date = (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
        comment = Help.generate_random_string(20)
        
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment
        }
        if color is not None:
            payload["color"] = color
        return payload
