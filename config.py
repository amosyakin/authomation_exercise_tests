import os

from dotenv import load_dotenv

load_dotenv()

domain_url = os.getenv('DOMAIN_URL')
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
