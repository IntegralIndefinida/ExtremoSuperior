import fractions as fr
total_cost = float(input("What's the total cost of the house?..."))
portion_down_payment = float(input("What portion of the total cost do you have to give as down payment? (in decimals)..."))
current_savings = float(input("How much did you already save?..."))
annual_salary = float(input("What's your annual salary?..."))
portion_saved_monthly = float(input("What portion of your monthly salary do you want to save? (in decimals)..."))
semmi_annual_raise = float(input("How much does your salary raise every six months? (in decimals). If you don't get a raise just write 0..."))
#Investment return (annual) = r
down_payment = total_cost*portion_down_payment
monthly_salary = (annual_salary)/12
r = 0.04

x = 0
y = 0
n = 0

while current_savings < down_payment:
    y = y+1
    
    money_saved_monthly = monthly_salary*portion_saved_monthly
    current_savings = current_savings +money_saved_monthly + (current_savings)*(r/12)
    n = n+fr.Fraction(1,6)
    if y/6 >= 1 and y/6 == int(n):
        monthly_salary = monthly_salary*(1+semmi_annual_raise)
        
    print(monthly_salary,y,n)
    if down_payment <= current_savings:
        print("You will have to save for",y,"months to make the down payment")