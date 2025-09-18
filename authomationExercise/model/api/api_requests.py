import requests

from authomationExercise.utils.attach import response_log, add_api_attach


def api_request(method, url, json=None, params=None, cookie=None):
    response = requests.request(method, url, json=json, params=params, cookies=cookie)
    response_log(response)
    add_api_attach(response)

    return response