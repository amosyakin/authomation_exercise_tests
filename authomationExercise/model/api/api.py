import allure

from authomationExercise.model.api.api_requests import api_request


def get_all_products_list(endpoint_url):
    url = endpoint_url + "/productsList"

    with allure.step("Вызов запроса на получение списка всех товаров"):
        response = api_request("GET", url)

    return response

def post_products_list(endpoint_url):
    url = endpoint_url + "/productsList"

    with allure.step("Вызов запроса на обновление списка всех товаров"):
        response = api_request("POST", url)

    return response

def get_all_brands_list(endpoint_url):
    url = endpoint_url + '/brandsList'

    with allure.step("Вызов запроса на получение списка всех брендов"):
        response = api_request("GET", url)

    return response

def put_brands_to_list(endpoint_url):
    url = endpoint_url + '/brandsList'

    with allure.step("Вызов запроса на получение списка всех брендов"):
        response = api_request("PUT", url)

    return response

def post_search_product(endpoint_url):
    url = endpoint_url + '/searchProduct'
    payload = {'search_product': 'top'}
    files = [

    ]
    headers = {}

    with allure.step("Вызов запроса на поиск по продукту"):
        response = api_request("POST", url, data=payload, headers=headers, files=files)

    return response
