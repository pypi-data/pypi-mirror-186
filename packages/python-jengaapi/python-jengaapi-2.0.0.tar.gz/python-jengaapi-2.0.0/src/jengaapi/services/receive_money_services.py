from ..configs.config import Config
from .utils import prepare_request_header, send_post_request


class ReceiveMoneyService:
    def __init__(self, config: Config):
        self.service_url = f'{config.BASE_URL}v3-apis/transaction-api/v3.0/'

    def receive_payments_bill_payments(self, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}bills/pay"
        return send_post_request(headers=headers, payload=payload, url=url)

    def receive_payments_merchant_payments(self, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}tills/pay"
        return send_post_request(headers=headers, payload=payload, url=url)

    def bill_validation(self, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}bills/validation"
        return send_post_request(headers=headers, payload=payload, url=url)


