import allure
from allure_commons.types import Severity

from authomationExercise.model.api import api
from authomationExercise.schemas.general_schemas import not_supported_method
from authomationExercise.schemas.products_list import get_all_products_list
from authomationExercise.utils.assertions import assertion_status_code, validate_json_schema


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.feature("Товары")
class TestProductsList:

    @allure.title("Проверка получения списка всех товаров")
    def test_get_all_products_list(self, endpoint_url):
        response = api.get_all_products_list(endpoint_url)
        assertion_status_code(response, 200)
        validate_json_schema(response, get_all_products_list)

        with allure.step("Проверка значений в теле ответа"):
            assert response.json()["responseCode"] == 200

    @allure.title("Проверка получения ошибки при вызове запроса на обновление списка всех товаров")
    def test_post_all_products_list(self, endpoint_url):
        response = api.post_products_list(endpoint_url)
        assertion_status_code(response, 200)
        validate_json_schema(response, not_supported_method)

        with allure.step("Проверка значений в теле ответа"):
            assert response.json()["responseCode"] == 405
            assert response.json()["message"] == "This request method is not supported."
