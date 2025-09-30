import requests

from authomationExercise.utils.attach import response_log, add_api_attach


def api_request(method, url, json=None, params=None, data=None, headers=None, cookie=None, files=None):
    response = requests.request(method, url, json=json, params=params, data=data, headers=headers, cookies=cookie, files=files)
    response_log(response)
    add_api_attach(response)

    return response