print('original price | discount |new price')
n=(4.95, 9.95, 14.95, 19.95, 24.95)
for i in n:
    reduced_price=i*0.6
    new_price=i-reduced_price
    print('$',i,'------','$',round(reduced_price,2),'------','$',round(new_price,2),sep="")