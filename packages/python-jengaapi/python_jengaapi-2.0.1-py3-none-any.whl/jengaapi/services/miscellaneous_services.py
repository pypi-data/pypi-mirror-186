from typing import Union

from .utils import prepare_request_header, send_post_request
from ..configs.config import Config


class MiscellaneousServices:

    def __init__(self, config: Config):
        self.service_url = f'{config.BASE_URL}v3-apis/'

    def purchase_airtime(self, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}transaction-api/v3.0/airtime"
        return send_post_request(headers=headers, payload=payload, url=url)

    def get_forex_rates(self, signature: Union[None, str], api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}transaction-api/v3.0/foreignExchangeRates"
        return send_post_request(headers=headers, payload=payload, url=url)

    def kyc(self, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}v3.0/validate/identity"
        return send_post_request(headers=headers, payload=payload, url=url)

