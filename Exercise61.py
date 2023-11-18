n=int(input('Enter value: '))
i=1
S=0
if n==0:
    print('The first value can not 0')
    n=int(input('Enter value again: '))
while n!=0:
    S=S+n
    n=int(input('Enter value: '))
    i=i+1
    if n==0:
        i=i-1
A=S/i
print('Average value is:', A)