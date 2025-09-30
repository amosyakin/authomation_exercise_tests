from authomationExercise.model.api import api
from authomationExercise.schemas.search_product import post_search_product
from authomationExercise.utils.assertions import assertion_status_code, validate_json_schema


def test_search_product(endpoint_url):
    response = api.post_search_product(endpoint_url)
    assertion_status_code(response, 200)
    validate_json_schema(response, post_search_product)
