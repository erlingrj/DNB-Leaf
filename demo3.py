import payments

accounts = ["50000000102", "50000000103","50000000104","50000000105","50000000106"]
accounts_dummy = ["50000000108","50000000109","50000000110","50000000111","50000000112"]


customer = "01011900123"
customer_dummy = "01011900124"


amount = 500

payments.pay(accounts[0], accounts_dummy[0], amount, message=None)
