pi = 3
sign = 1
print('Approximation 1 is', pi)
for i in range(1, 15): 
    denominator = 2 * i * (2 * i + 1) * (2 * i + 2)
    term = 4 / denominator
    pi = pi + term*sign
    sign = sign*(-1)
    print('Approximation', i+1, 'is', pi)