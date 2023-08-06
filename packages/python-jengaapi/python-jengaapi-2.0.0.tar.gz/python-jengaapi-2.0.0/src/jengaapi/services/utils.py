import datetime
from json import JSONDecodeError
from typing import Union

import requests
from requests import Response


def handle_response(response: Response) -> Union[dict, JSONDecodeError]:
    """
    Handles Responses From the JengaHQ API and Raises Exceptions appropriately
    as errors occur and returns a `dict` object from the `json` response
    """
    try:
        return response.json()
    except JSONDecodeError as e:
        raise ("An error occurred decoding the JSON response" + str(e))


def prepare_request_header(signature: Union[None, str], token: str) -> dict:
    if signature:
        return {
            "Authorization": token,
            "Content-Type": "application/json",
            "signature": signature
        }
    else:
        return {
            "Authorization": token,
            "Content-Type": "application/json"
        }


def send_post_request(headers: dict, payload: dict, url: str) -> Union[dict, JSONDecodeError]:
    response = requests.post(url, json=payload, headers=headers)
    return handle_response(response)


def send_get_request(headers: dict, url: str) -> Union[dict, JSONDecodeError]:
    response = requests.get(url, headers=headers)
    return handle_response(response)


def generate_reference() -> str:
    """
    Generate a transaction reference
    Should always be a 12 digit String
    """
    a = datetime.datetime.now()
    return "".join(str(a).replace(" ", "").replace("-", "").split(":")[0:2])
