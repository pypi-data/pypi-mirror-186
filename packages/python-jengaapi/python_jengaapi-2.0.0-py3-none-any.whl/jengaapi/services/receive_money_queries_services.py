from .utils import prepare_request_header, send_get_request
from ..configs.config import Config


class ReceiveMoneyQueriesService:

    def __init__(self, config: Config):
        self.service_url = f'{config.BASE_URL}v3-apis/transaction-api/v3.0/'

    def get_all_eazzy_pay_merchants(self, api_token: str, page: int = 1, per_page: int = 1):
        headers = prepare_request_header(None, api_token)
        url = f"{self.service_url}merchants?page={page}&per_page={per_page}"
        return send_get_request(headers=headers, url=url)

    def query_transaction_details(self, api_token: str, ref: str):
        headers = prepare_request_header(None, api_token)
        url = f"{self.service_url}payments/details/{ref}"
        return send_get_request(headers=headers, url=url)

    def get_all_billers(self, api_token: str, page: int = 1, per_page: int = 1, category: str = None):
        headers = prepare_request_header(None, api_token)
        url = f"{self.service_url}billers?page={page}&per_page={per_page}&category={category}"
        return send_get_request(headers=headers, url=url)
