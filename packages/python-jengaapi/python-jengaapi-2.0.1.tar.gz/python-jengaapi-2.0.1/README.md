[![Pytest CI](https://github.com/MainaKamau92/JengaAPIPythonWrapper/actions/workflows/pytest.yml/badge.svg)](https://github.com/MainaKamau92/JengaAPIPythonWrapper/actions/workflows/pytest.yml) [![codecov](https://codecov.io/gh/MainaKamau92/JengaAPIPythonWrapper/branch/main/graph/badge.svg?token=cm9MaLo7Fc)](https://codecov.io/gh/MainaKamau92/JengaAPIPythonWrapper) [![Maintainability](https://api.codeclimate.com/v1/badges/883850b3a746cbc8f080/maintainability)](https://codeclimate.com/github/MainaKamau92/JengaAPIPythonWrapper/maintainability)

## JengaAPIPythonWrapper

A simple python wrapper around the JengaAPI from Equity Bank

## Setup

Installation

```
pip install python-jengaapi
```

A sample of the `.env` variables required include:
```
MERCHANT_CODE=1234567
CONSUMER_SECRET=XXXXXXXXXXXXX
API_KEY=123XXX222
ACCOUNT_NAME=John Doe
ACCOUNT_NUMBER=12345678
CURRENCY_CODE=KES
COUNTRY_CODE=KE
FOREIGN_CURRENCY_CODE=USD
PRIVATE_KEY_PATH=path_to_privatekey.pem
```

### Authorization Service
#### Fetch Authorization token
```pycon
# script.py
from jengaapi.configs.config import app_config
from jengaapi.services.authorization_service import AuthorizationService

uat_config = app_config.get('uat')

# Get the environment variables
MERCHANT_CODE = uat_config.MERCHANT_CODE
CONSUMER_SECRET = uat_config.CONSUMER_SECRET
COUNTRY_CODE = os.getenv('COUNTRY_CODE')
ACCOUNT_NUMBER = os.getenv('ACCOUNT_NUMBER')


auth = AuthorizationService(config=uat_config)
auth_token = auth.auth_token
print(auth_token)
```
```shell
$ python script.py
Bearer eexxxxx.xx.xxxxxx
```
## Account Service
#### Fetch Account Balance
```pycon
account_service = AccountServices(config=uat_config)
# Get account balance
signature = auth.signature((COUNTRY_CODE, ACCOUNT_NO))
account_balance = account_service.account_balance(signature, auth_token, COUNTRY_CODE, ACCOUNT_NO)
print(account_balance)
```
```shell
$ python script.py
{
   "status":true,
   "code":0,
   "message":"success",
   "data":{
      "balances":[
         {
            "amount":"485115080.54",
            "type":"Available"
         },
         {
            "amount":"485115080.54",
            "type":"Current"
         }
      ],
      "currency":"KES"
   }
}
```
#### Fetch Account Mini Statement
```pycon
account_service = AccountServices(config=uat_config)
signature = auth.signature((COUNTRY_CODE, ACCOUNT_NO))
account_mini_statement = account_service.account_mini_statement(signature, auth_token, COUNTRY_CODE, ACCOUNT_NO)
print(account_mini_statement)
```
```shell
{
   "status":true,
   "code":0,
   "message":"success",
   "data":{
      "balance":484837600.0,
      "currency":"KES",
      "accountNumber":"1450160649886",
      "transactions":[
         {
            "date":"2023-01-12T00:00:00.000",
            "amount":"1",
            "description":"JENGA CHARGE CREDIT 673579628084879",
            "chequeNumber":"None",
            "type":"Credit"
         },
         {
            "date":"2023-01-12T00:00:00.000",
            "amount":"1",
            "description":"JENGA CHARGE DEBIT 673579628084879",
            "chequeNumber":"None",
            "type":"Debit"
         },
         {
            "date":"2023-01-12T00:00:00.000",
            "amount":"1",
            "description":"JENGA CHARGE CREDIT 673579623845546",
            "chequeNumber":"None",
            "type":"Credit"
         },
         {
            "date":"2023-01-12T00:00:00.000",
            "amount":"1",
            "description":"REV-(673540528125447)JENGA CHARGE DEBIT 6735405275",
            "chequeNumber":"None",
            "type":"Debit"
         }
      ]
   }
}
```
#### Fetch Account Opening and Closing Balance
```pycon
ep_signature = auth.signature((ACCOUNT_NO, COUNTRY_CODE, "2023-01-01"))
payload = dict(
    countryCode=COUNTRY_CODE,
    accountId=ACCOUNT_NO,
    date="2023-01-01",
)
opening_closing = account_service.opening_closing_account_balance(ep_signature, auth_token, **payload)
print(opening_closing)
```
```shell
{
   "status":true,
   "code":0,
   "message":"success",
   "data":{
      "balances":[
         {
            "amount":"0",
            "type":"Closing Balance"
         },
         {
            "amount":"0",
            "type":"Opening Balance"
         }
      ]
   }
}
```
### Send Money Service
#### Send within Equity
```pycon
send_money_service = SendMoneyService(config=uat_config)
payload = {
    "source": {
        "countryCode": COUNTRY_CODE,
        "name": "CATHERINE MURANDITSI MUKABWA",
        "accountNumber": ACCOUNT_NO
    },
    "destination": {
        "type": "bank",
        "countryCode": "KE",
        "name": "Tom Doe",
        "accountNumber": "0250163591202"
    },
    "transfer": {
        "type": "InternalFundsTransfer",
        "amount": "1000.00",
        "currencyCode": "KES",
        "reference": "692494625798",
        "date": "2023-08-18",
        "description": "some remarks here"
    }
}
ep_signature = auth.signature((ACCOUNT_NO,"1000.00", "KES", "692494625798"))
send_money_within_equity = send_money_service.send_within_equity(ep_signature, auth_token, **payload)
print(send_money_within_equity)
```
```shell
{
  "status": true,
  "code": 0,
  "message": "success",
  "data": {
    "transactionId": "54154",
    "status": "SUCCESS"
  }
}
```
#### Send to mobile wallets
```pycon
payload = {
    "source": {
        "countryCode": "KE",
        "name": "CATHERINE MURANDITSI MUKABWA",
        "accountNumber": ACCOUNT_NO
    },
    "destination": {
        "type": "mobile",
        "countryCode": "KE",
        "name": "A N.Other",
        "mobileNumber": "0722123456",
        "walletName": "Mpesa"
    },
    "transfer": {
        "type": "MobileWallet",
        "amount": "1000",
        "currencyCode": "KES",
        "date": "2023-01-13",
        "description": "some remarks here"
    }
}
ep_signature = auth.signature(("1000", "KES", "692494625799", ACCOUNT_NO))
send_money_within_equity = send_money_service.send_to_mobile_wallets(ep_signature, auth_token, **payload)
print(send_money_within_equity)
```
```shell
{
    "status": true,
    "code": 0,
    "message": "success",
    "data": {
      "transactionId": "",
      "status": "SUCCESS"
    }
}
```

#### Jenga API docs
For official documentatio the Equity bank api refer [here](https://developer.jengaapi.io/reference/welcome)