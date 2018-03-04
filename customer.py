import json
import random

import requests

ENDPOINT = 'https://dnbapistore.com/hackathon/customers/3.0'
TOKEN = '309d5490-8c52-3f86-9f99-6b912fa100b6'
headers = {'Authorization': 'Bearer {}'.format(TOKEN), 'Accept': 'application/json'}

data1 = {
  "personalNumber": "01011900124",
  "firstName": "Erling",
  "lastName": "Jellum",
  "dateOfBirth": "1999-08-07T00:00:00.000Z",
  "gender": "Male",
  "nationality": "Spain",
  "address": {
    "street": "Majostuvein",
    "postalCode": 3405,
    "city": "Gotham city",
    "country": "US"
  },
  "phoneNumber": "+4791791692",
  "email": "batman@rescue.me",
  "idNumber": 800009,
  "idType": "passport"
}
data2 = {
    "personalNumber": "01011900124",
    "firstName": "Janet",
    "lastName": "Jackson",
    "dateOfBirth": "1999-08-07T03:00:00.000Z",
    "gender": "Female",
    "nationality": "Portugal",
    "address": {
        "street": "Majostuvein",
        "postalCode": 3405,
        "city": "Gotham city",
        "country": "US"
        },
        "phoneNumber": "+4791791692",
        "email": "batman@rescue.me",
        "idNumber": 800009,
        "idType": "passport"
}
r = requests.post(ENDPOINT + '/customer', json=data1, headers=headers)
if r.ok:
    customer = r.json()
    print(customer)
else:
    print(r.content)

customerId = customer['customerId']

r.request.path_url

r = requests.get(ENDPOINT + '/customer/{}'.format(customerId), headers=headers)
if r.ok:
    print(r.json())
else:
    print(r.content)

prev = customer['phoneNumber']
customer['phoneNumber'] = customer['phoneNumber'][:3] + ''.join(str(random.randint(0, 9)) for x in range(len(customer['phoneNumber']) - 3))
print(prev, customer['phoneNumber'])

customerId = customer['customerId']
r = requests.patch(ENDPOINT + '/customer'.format(customerId), json=customer, headers=headers)
if r.ok:
    customer = r.json()
    r = requests.get(ENDPOINT + '/customer/{}'.format(customerId), headers=headers)
    if r.ok:
        print(r.json())
    else:
        print(r.content)
else:
    print(r.content)
