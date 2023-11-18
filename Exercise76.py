n=int(input('Enter an integer: '))
i=2
while i<=n:
    if n%i==0:
        print(i)
        n=n//i
    else:
        i=i+1