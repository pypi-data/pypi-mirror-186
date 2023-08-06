"""
Awattar Energy Price module, documentation:
https://www.awattar.de/services/api
"""


import requests

from .validations import validate_empty_string


# pylint: disable=too-few-public-methods
class GreenEnergyApi:
    """
    Class providing methods for getting CO2 forecast for a zone.
    """

    def __init__(self, host: str, timeout: int = 5) -> None:
        validate_empty_string(host, "host")
        self.host: str = host
        self.timeout: int = timeout

    def __query_avattar_api(self, path: str) -> dict:
        try:
            url = f"{self.host}/{path}"

            status_request = requests.get(url, timeout=self.timeout)
            status = status_request.json()
            return status
        except (
            requests.exceptions.ConnectTimeout,
            requests.exceptions.ConnectionError,
        ):
            return {"success": False, "msg": "Request couldn't connect or timed out"}

    def get_electricity_price(self) -> dict:
        """Get the energy prices from a public api"""
        response = self.__query_avattar_api("v1/marketdata")

        if response is None or response.get("success") is False:
            raise RuntimeError(f"Request failed with: {response}")

        return response
