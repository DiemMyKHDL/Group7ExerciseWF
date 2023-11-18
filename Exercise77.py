binary = input('Enter a binary number (base 2): ')
decimal = 0
for i in binary:
    decimal = int(i) + decimal * 2
print('The decimal equivalent of', binary, 'is', decimal)