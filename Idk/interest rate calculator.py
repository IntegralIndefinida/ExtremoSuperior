
Initial_deposit = float(input("initial deposit:"))
t = 3*12
total_cost = 800000
down_payment = total_cost*0.25
amount_saved = Initial_deposit
s = 1
i = 0
r = (s+i)/2
n =0
if Initial_deposit >= down_payment-100:
    r=0
while not down_payment+100 > amount_saved > down_payment-100:
    amount_saved = Initial_deposit * (1+ r/12)**t
    if amount_saved > down_payment+100:
        s = r
        n =n+ 1
    elif amount_saved < down_payment-100:
        i = r
        n =n+1
    r = (s+i)/2
print(r,n)
