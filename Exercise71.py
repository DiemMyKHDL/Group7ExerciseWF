x = float(input('Enter x: ')) 
guess = x/ 2
while abs(guess**2 - x) >= 10**(-12):
        guess = (guess + x/ guess) / 2
print('The square root of', x, 'is', guess)