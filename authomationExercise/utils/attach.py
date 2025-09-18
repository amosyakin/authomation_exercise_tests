import json
import logging

import allure
from allure_commons.types import AttachmentType
from requests import Response


def response_log(response: Response):
    logging.info("Request URL: " + response.request.url)
    if response.request.body:
        request_body = response.request.body
        if isinstance(request_body, bytes):
            request_body = request_body.decode('utf-8')
        logging.info("Request body: " + request_body)

def add_api_attach(response: Response):
    allure.attach(
        body=f'{response.request.method} ' + response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        request_body = response.request.body
        if isinstance(request_body, bytes):
            request_body = request_body.decode('utf-8')
        allure.attach(
            body=json.dumps(json.loads(request_body), indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
    try:
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
    except json.JSONDecodeError:
        allure.attach(
            body=f'Response body is empty\n' + response.text,
            name="Response body",
            attachment_type=AttachmentType.TEXT,
        )
