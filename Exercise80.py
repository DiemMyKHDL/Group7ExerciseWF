from random import randrange
total_flips = 0
for _ in range(10):
    i = 0
    consecutive = 0
    again_result = None
    while consecutive < 3:
        result = randrange(2)
        i = i + 1
        if i > 1:
            if result == again_result:
                consecutive = consecutive + 1
            else:
                consecutive = 1
        print('H ' if result == 0 else 'T ', end='')
        again_result = result
    print('(',i, ' flips)', sep='')
    total_flips = total_flips + i
average_flips = total_flips / 10
print('On average, %.2f flips were needed' % average_flips)