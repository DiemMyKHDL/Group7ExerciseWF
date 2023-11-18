total_cost=0
while True:
    P=input('Price of item: ')
    if P=='': break
    else:
        P=float(P)
    total_cost=total_cost+P
    pennies=round(total_cost*100)
    remainder=pennies%5
    if remainder==0: the_pennis_payment_amout=pennies
    elif remainder <2.5:
        sodongxuphaitra=pennies - remainder
    else:
        sodongxuphaitra=pennies + (5-remainder)
print('The total cost of all the entered items is: $', total_cost, sep='')
print('The cash payment amount: $',the_pennis_payment_amout/100, sep='')
