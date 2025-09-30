import pytest

import config

domain_url = config.domain_url

@pytest.fixture
def endpoint_url():
    base_url = domain_url + '/api'
    return base_url
