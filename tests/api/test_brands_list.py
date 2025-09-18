import allure
from allure_commons.types import Severity

from authomationExercise.model.api import api
from authomationExercise.schemas.brands_list import get_all_brands_list
from authomationExercise.schemas.general_schemas import not_supported_method
from authomationExercise.utils.assertions import assertion_status_code, validate_json_schema

@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.feature("Бренды")
class TestBrandsList:

    @allure.title("Проверка получения списка всех брендов")
    def test_get_brands_list(self, endpoint_url):
        response = api.get_all_brands_list(endpoint_url)
        assertion_status_code(response, 200)
        validate_json_schema(response, get_all_brands_list)

        with allure.step("Проверка значений в теле ответа"):
            assert response.json()["responseCode"] == 200

    @allure.title("Проверка получения ошибки при вызове запроса на обновление списка всех бренод")
    def test_put_brand_to_list(self, endpoint_url):
        response = api.put_brands_to_list(endpoint_url)
        assertion_status_code(response, 200)
        validate_json_schema(response, not_supported_method)
