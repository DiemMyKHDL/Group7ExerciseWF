total_cost = 0.00
while True:
    age = input('Enter the age of a guest: ')
    if age== '':
        break
    age = int(age)
    if age <= 2:
        admission_price = 0.00
    elif 3<=age<=12 :
        admission_price = 14.00
    elif age >= 65:
        admission_price = 18.00
    else:
        admission_price = 23.00
    total_cost= total_cost + admission_price
print("The admission cost for the group is $", round(total_cost, 2), sep='')