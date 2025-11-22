NO_LOGIN_PAYLOAD = {
    "password": "somepassword"
}

EXPECTED_NO_LOGIN = {
    "code": 400,
    "message": "Недостаточно данных для входа"
}

NO_PASSWORD_PAYLOAD = {
    "login": "somelogin"
}

EXPECTED_NO_PASSWORD = {
    "code": 400,
    "message": "Недостаточно данных для входа"
}

WRONG_LOGIN_PAYLOAD = {
    "login": "wronglogin",
    "password": "somepassword"
}

EXPECTED_WRONG_LOGIN = {
    "code": 404,
    "message": "Учетная запись не найдена"
}

WRONG_PASSWORD_PAYLOAD = {
    "login": "somelogin",
    "password": "wrongpassword"
}

EXPECTED_WRONG_PASSWORD = {
    "code": 404,
    "message": "Учетная запись не найдена"
}

EXPECTED_NONEXISTENT_USER = {
    "code": 404,
    "message": "Учетная запись не найдена"
}

SUCCESS_CREATE_RESPONSE = {
    "ok": True
}

DUPLICATE_CREATE_RESPONSE = {
    "code": 409,
    "message": "Этот логин уже используется. Попробуйте другой."
}

MISSING_DATA_CREATE_RESPONSE = {
    "code": 400,
    "message": "Недостаточно данных для создания учетной записи"
}

WITHOUT_LOGIN_PAYLOAD = {
    "password": "testpass",
    "firstName": "testname"
}

WITHOUT_PASSWORD_PAYLOAD = {
    "login": "testlogin",
    "firstName": "testname"
}

MISSING_MULTIPLE_FIELDS_PAYLOAD = {
    "firstName": "testname"
}

ORDER_COLORS = {
    "one_color_black": ["BLACK"],
    "one_color_grey": ["GREY"],
    "both_colors": ["BLACK", "GREY"],
    "no_color": None
}

EXPECTED_ORDER_STATUS = 201
EXPECTED_ORDER_TRACK_KEY = "track"

EXPECTED_GET_ORDERS_STATUS_SUCCESS = 200
EXPECTED_GET_ORDERS_RESPONSE_KEYS = ["orders", "pageInfo", "availableStations"]
EXPECTED_PAGE_INFO_KEYS = ["page", "total", "limit"]
EXPECTED_AVAILABLE_STATIONS_KEYS = ["name", "number", "color"]
REQUIRED_ORDER_FIELDS = ["id", "courierId", "firstName", "lastName", "address", "metroStation", "phone", "rentTime", "deliveryDate", "track", "color", "comment", "createdAt", "updatedAt", "status"]
EXPECTED_GET_ORDERS_STATUS_NOT_FOUND = 404
EXPECTED_NOT_FOUND_MESSAGE_KEYWORD = "не найден"
GET_ORDERS_PARAMS_DEFAULT = {}
GET_ORDERS_PARAMS_WITH_LIMIT = {"limit": 10, "page": 0}
