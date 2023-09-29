# url_checker.py

import requests
from config import Config

class URLChecker:
    def __init__(self):
        self.config = Config()

    def check_url(self):
        url_to_check = self.config.url_to_check

        try:
            response = requests.get(url_to_check)
            response.raise_for_status()  # Raises an exception for 4xx and 5xx status codes

            if response.status_code == 200:
                return f"The URL '{url_to_check}' is returning a '200 OK' status code."
            else:
                return f"The URL '{url_to_check}' is returning a '{response.status_code}' status code."
        except requests.exceptions.RequestException as e:
            return f"Error checking URL: {e}"
