import account
import payments


def initialize(accounts, accounts_dummy,customer, customer_dummy):


    # Initial values
    account_balance = [1600*0.6,1000*0.5,2000*0.6,600*0.7,400*0.7]
    # Initialize account values.
    for i in range(0,5):
        diff = account.getBalance(customer,accounts[i]) - account_balance[i]
        if diff > 0:
            payments.pay(accounts[i], accounts_dummy[i], diff, message=None)
        elif diff < 0:
            payments.pay(accounts_dummy[i],accounts[i], diff*-1, message=None)
