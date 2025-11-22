import pytest
from helpers import Help

@pytest.fixture
def create_courier():
    credentials = Help.register_new_courier_and_return_login_password()
    if credentials:
        return credentials
    else:
        pytest.fail("Не удалось создать курьера для фикстуры")

@pytest.fixture
def courier_credentials(create_courier):
    return {
        "login": create_courier["login"],
        "password": create_courier["password"]
    }
