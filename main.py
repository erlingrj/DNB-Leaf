import account
import initialize
import time
import nanoleaf2
import sys


from initialize import initialize
from account import getBalance
from nanoleaf2 import setPanel




N = 5

lims = [0.75, 0.50, 0.25, 0.0]
budget = [1600, 1000, 2000, 600, 400]
monthly_assets = [1600,1000,2000,600,400]
color_tier = [(43,201,27),(113,214,20),(184,228,13),(255,242,7),(248,181,16),(242,121,25),(235,60,34),(229,0,43)]
account_categories = ['Food and beverage','General','Housing','Transportation','Leisure']

def updatePanel(spent,budget,i):
    if spent < budget*0.125:
        setPanel(i,color_tier[0])
    elif spent >= budget*0.125 and spent < budget*0.25:
        setPanel(i,color_tier[1])
    elif spent >= budget*0.25 and spent < budget*0.375:
        setPanel(i,color_tier[2])
    elif spent >= budget*0.375 and spent < budget*0.5:
        setPanel(i,color_tier[3])
    elif spent >= budget*0.5 and spent < budget*0.625:
        setPanel(i,color_tier[4])
    elif spent >= budget*0.625 and spent < budget*0.75:
        setPanel(i,color_tier[5])
    elif spent >= budget*0.75 and spent < budget*0.875:
        setPanel(i,color_tier[6])
    elif spent >= budget*0.875:
        setPanel(i,color_tier[7])

def final():

    setPanel(0,color_tier[7])
    setPanel(1,color_tier[7])
    setPanel(2,color_tier[0])
    setPanel(3,color_tier[7])
    setPanel(4,color_tier[0])

    wait = input('Slide 3')

    setPanel(0,(0,0,0))
    setPanel(1,(0,0,0))
    setPanel(2,(255,255,255))
    setPanel(3,(0,0,0))
    setPanel(4,(0,0,0))

    wait = input('Slide 4')

    setPanel(0,(0,0,0))
    setPanel(1,(0,0,0))
    setPanel(2,(0,0,0))
    setPanel(3,(255,255,255))
    setPanel(4,(0,0,0))

    wait = input('Slide 5')

    setPanel(0,(0,0,0))
    setPanel(1,(0,0,0))
    setPanel(2,(0,0,0))
    setPanel(3,(0,0,0))
    setPanel(4,(255,255,255))

    wait = input('End of presentation')

    setPanel(0,(0,0,0))
    setPanel(1,(0,0,0))
    setPanel(2,(0,0,0))
    setPanel(3,(0,0,0))
    setPanel(4,(0,0,0))



# Already created savings-accounts.
# <Food and beverage> <Living costs> <Housing> <Transportation> <Leisure time>
accounts = ["50000000102", "50000000103","50000000104","50000000105","50000000106"]
#
accounts_dummy = ["50000000108","50000000109","50000000110","50000000111","50000000112"]


customer = "01011900123"
customer_dummy = "01011900124"

initialize(accounts, accounts_dummy, customer, customer_dummy)

last_balance = [1,1,1,1,1]
current_balance = [0,0,0,0,0]

print("The Matrix is now initialized.")
print("Welcome.")
print([getBalance(customer, acc) for acc in accounts])

while True:
    try:
        #Poll account balances
        current_balance = [getBalance(customer, acc) for acc in accounts]
        for i in range(0,N):
            if current_balance[i] != last_balance[i]:
                print('Account balance update for Account:',i, account_categories[i])
                print('New balance: ', current_balance[i], "NOK")
                spent = monthly_assets[i]-current_balance[i]
                updatePanel(spent,budget[i],i)
                last_balance[i] = current_balance[i]


        time.sleep(0.5)

    except KeyboardInterrupt:
        print('Example: Unpayed bills: ')
        final()
        sys.exit()
