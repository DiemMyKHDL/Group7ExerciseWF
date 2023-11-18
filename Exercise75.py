m = int(input('Enter the first number: '))
n = int(input('Enter the second number: '))
d = min(m, n)
while m % d != 0 or n % d != 0:
    d = d- 1
print(d, 'is the common divisor of', m, 'and', n)