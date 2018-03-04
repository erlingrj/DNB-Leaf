
import requests

ENDPOINT = 'https://dnbapistore.com/hackathon/accounts/3.0'
TOKEN = '309d5490-8c52-3f86-9f99-6b912fa100b6'
headers = {'Authorization': 'Bearer {}'.format(TOKEN)}
customer_a = '01011900123'
customer_b = '01011900124'

def createSavingsAccount(customerId):
    data = {
      "customerId": customerId,
      "accountName": "Regular account",
      "accountType": "Savings",
      "currency": "NOK"
    }
    PATH = '/account'
    resp = requests.post(ENDPOINT + PATH, json=data, headers=headers)
    if resp.ok:
        account_a = resp.json()
        return account_a
    else:
        print('opps', resp.content)


def getBalance(customerID, accountNumber):
    PATH = '/account/balance'
    p = {'customerId': customerID, 'accountNumber': accountNumber}
    resp = requests.get(ENDPOINT + PATH, headers=headers, params=p)
    if resp.ok:
        data = resp.json()
        return int(data['availableBalance'].split('.')[0])
    else:
        print('opps', resp.content)
