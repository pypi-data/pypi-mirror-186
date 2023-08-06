from .utils import prepare_request_header, send_post_request
from ..configs.config import Config


class SendMoneyService:

    def __init__(self, config: Config):
        self.service_url = f'{config.BASE_URL}v3-apis/transaction-api/v3.0/remittance/'

    def send_within_equity(self, signature: str, api_token: str, **payload: dict) -> dict:
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}internalBankTransfer"
        return send_post_request(headers=headers, payload=payload, url=url)

    def send_to_mobile_wallets(self, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}sendmobile"
        return send_post_request(headers=headers, payload=payload, url=url)

    def send_rtgs(self, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}rtgs"
        return send_post_request(headers=headers, payload=payload, url=url)

    def send_swift(self, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}swift"
        return send_post_request(headers=headers, payload=payload, url=url)

    def send_pesa_link_to_bank_account(self, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}pesalinkacc"
        return send_post_request(headers=headers, payload=payload, url=url)

    def send_pesa_link_to_mobile_number(self, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}pesalinkMobile"
        return send_post_request(headers=headers, payload=payload, url=url)


