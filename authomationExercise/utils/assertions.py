import allure
from jsonschema import validate
from requests import Response


def assertion_status_code(response: Response, expected_status_code: int = 200):
    with allure.step("Проверка статус кода"):
        assert response.status_code == expected_status_code

def validate_json_schema(response: Response, schema: dict):
    with allure.step("Валидация JSON-схемы"):
        response_json_body = response.json()
        validate(response_json_body, schema)