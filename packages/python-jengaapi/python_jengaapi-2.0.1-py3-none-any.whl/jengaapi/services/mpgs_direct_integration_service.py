from typing import Union

from ..configs.config import Config
from .utils import prepare_request_header, send_post_request


class MPGSDirectIntegration:

    def __init__(self, config: Config):
        self.service_url = f'{config.BASE_URL}mpgs-direct-integration/api/v3.1/'

    def mpgs_validate_payment(self, signature: Union[None, str], api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}validatePayment"
        return send_post_request(headers=headers, payload=payload, url=url)

    def mpgs_authenticate_payment(self, signature: Union[None, str], api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}authenticatePayment"
        return send_post_request(headers=headers, payload=payload, url=url)

    def mpgs_authorize_payment(self, signature: Union[None, str], api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}authorizePayment"
        return send_post_request(headers=headers, payload=payload, url=url)

    def mpgs_query_payment(self, signature: Union[None, str], api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}transactionStatus"
        return send_post_request(headers=headers, payload=payload, url=url)

    def mpgs_refund_payment(self, signature: Union[None, str], api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}refundPayment"
        return send_post_request(headers=headers, payload=payload, url=url)
