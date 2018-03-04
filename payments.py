import requests

ENDPOINT = 'https://dnbapistore.com/hackathon/payments/3.0'
TOKEN = '309d5490-8c52-3f86-9f99-6b912fa100b6'
headers = {'Authorization': 'Bearer {}'.format(TOKEN)}

def pay(debitAccountNumber, creditAccountNumber, amount, message=None):
    PATH = '/payment'
    data = {
      "debitAccountNumber": debitAccountNumber,
      "creditAccountNumber": creditAccountNumber,
      "message": message or 'Thank you',
      "amount": str(amount),
      "paymentDate": "2018-03-03"
    }
    resp = requests.put(ENDPOINT + PATH, json=data, headers=headers)
    if resp.ok:
        data = resp.json()
        return data
    else:
        print('opps', resp.content)


def payByVipps(debitAccountNumber, amount, message=None):
    PATH = '/payment/vipps'
    data = {
      "debitAccountNumber": debitAccountNumber,
      "message": message or 'Thank you',
      "amount": str(amount),
      "paymentDate": "2018-03-03"
    }
    resp = requests.put(ENDPOINT + PATH, json=data, headers=headers)
    if resp.ok:
        data = resp.json()
        print(data)
        return data
    else:
        print('opps', resp.content)
