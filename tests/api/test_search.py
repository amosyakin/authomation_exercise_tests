import allure
from allure_commons.types import Severity

from authomationExercise.model.api import api
from authomationExercise.schemas.general_schemas import not_supported_method
from authomationExercise.schemas.search_product import post_search_product
from authomationExercise.utils.assertions import assertion_status_code, validate_json_schema


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.feature("Поиск товаров")
class TestSearchProduct:

    @allure.title("Проверка поиска по товарам")
    def test_search_product(self, endpoint_url):
        payload = {'search_product': 'top'}
        response = api.post_search_product(endpoint_url, payload)
        assertion_status_code(response, 200)
        validate_json_schema(response, post_search_product)

        with allure.step("Проверка значений в теле ответа"):
            assert response.json()["responseCode"] == 200

    @allure.title("Проверка поиска по товарам без указания параметра search_product")
    def test_search_product_without_parameter(self, endpoint_url):
        response = api.post_search_product(endpoint_url)
        assertion_status_code(response, 200)
        validate_json_schema(response, not_supported_method)

        with allure.step("Проверка значений в теле ответа"):
            assert response.json()["responseCode"] == 400
