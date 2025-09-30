import allure
from allure_commons.types import Severity

import config
from authomationExercise.model.api import api
from authomationExercise.schemas.verify_login import success_verify_login
from authomationExercise.utils.assertions import assertion_status_code, \
    validate_json_schema


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.feature("Верификация пользователя")
class TestVerifyLogin:
    email = config.email
    password = config.password


    @allure.title("Проверка верификации пользователя")
    def test_valid_verify_login(self, endpoint_url):
        creds = {
            "email": self.email,
            "password": self.password
        }
        response = api.post_verify_login(endpoint_url, creds)

        assertion_status_code(response, 200)

        validate_json_schema(response, success_verify_login)

        with allure.step("Проверка значений в теле ответа"):
            assert response.json()["responseCode"] == 200
            assert response.json()["message"] == 'User exists!'
