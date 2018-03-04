import payments

N=5

accounts = ["50000000102", "50000000103","50000000104","50000000105","50000000106"]
accounts_dummy = ["50000000108","50000000109","50000000110","50000000111","50000000112"]

acc_distr = [1500/2000,1000/2000,2000/2000,600/2000,500/2000]

amount = 500

customer = "01011900123"
customer_dummy = "01011900124"




for i in range(0,N):
    payments.pay(accounts_dummy[i], accounts[i], amount*acc_distr[i], message=None)
