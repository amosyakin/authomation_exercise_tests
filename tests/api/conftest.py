import os

import pytest
from dotenv import load_dotenv

load_dotenv()

domain_url = os.getenv('DOMAIN_URL')

@pytest.fixture
def endpoint_url():
    base_url = domain_url + '/api'
    return base_url