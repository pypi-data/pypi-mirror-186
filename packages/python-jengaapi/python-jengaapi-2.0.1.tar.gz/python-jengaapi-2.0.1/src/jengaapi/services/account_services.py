from .utils import prepare_request_header, send_get_request, send_post_request
from ..configs.config import Config


class AccountServices:

    def __init__(self, config: Config):
        self.service_url = f'{config.BASE_URL}v3-apis/account-api/v3.0/accounts/'

    def account_balance(self, signature: str, api_token: str, country_code: str, account_id: str):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}balances/{country_code}/{account_id}"
        return send_get_request(headers, url)

    def account_mini_statement(self, signature: str, api_token: str, country_code: str, account_no: str):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}miniStatement/{country_code}/{account_no}"
        return send_get_request(headers, url)

    def account_inquiry_bank_accounts(self, signature: str, api_token: str, country_code: str, account_no: str):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}search/{country_code}/{account_no}"
        return send_get_request(headers, url)

    def opening_closing_account_balance(self, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}accountBalance/query"
        return send_post_request(headers=headers, payload=payload, url=url)

    def account_full_statement(self, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{self.service_url}fullStatement"
        return send_post_request(headers=headers, payload=payload, url=url)
