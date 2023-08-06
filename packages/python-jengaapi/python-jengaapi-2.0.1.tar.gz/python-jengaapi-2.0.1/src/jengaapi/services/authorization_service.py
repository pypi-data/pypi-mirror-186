from base64 import b64encode

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from .utils import send_post_request
from ..configs.config import Config


class AuthorizationService:
    def __init__(self, config: Config):
        self._merchant_code = config.MERCHANT_CODE
        self._consumer_secret = config.CONSUMER_SECRET
        self.private_key = config.PRIVATE_KEY_PATH
        self.api_key = config.API_KEY
        self.base_url = config.BASE_URL

    @property
    def auth_token(self):
        url = f"{self.base_url}authentication/api/v3/authenticate/merchant"
        payload = {
            "merchantCode": self._merchant_code,
            "consumerSecret": self._consumer_secret
        }
        headers = {
            "Content-Type": "application/json",
            "Api-Key": self.api_key
        }
        response = send_post_request(headers, payload, url)
        return "Bearer " + response.get("accessToken")

    def signature(self, request_hash_fields: tuple):
        message = "".join(request_hash_fields).encode(
            "utf-8")  # See separate instruction on how to create this concatenation
        digest = SHA256.new()
        digest.update(message)
        with open(self.private_key, "r") as my_file:
            private_key = RSA.importKey(my_file.read())
        signer = PKCS1_v1_5.new(private_key)
        sigBytes = signer.sign(digest)
        return b64encode(sigBytes)
