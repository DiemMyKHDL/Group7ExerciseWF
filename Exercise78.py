q=int(input('Enter a decimal (base 10) number: '))
binary_base2=''
while q>0:
    r=q%2
    r=str(r)
    binary_base2=r+binary_base2
    q=q//2
print(binary_base2)
