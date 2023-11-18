x1 = float(input('Enter the x part of the coordinate: '))
y1 = float(input('Enter the y part of the coordinate: '))
x_last=x1
y_last=y1
perimeter = 0
while True:
    X2= input('Enter the x part of the coordinate (blank to quit): ')
    if X2 == '':
        break
    x2 = float(X2)
    y2 = float(input('Enter the y part of the coordinate: '))
    dx= x2-x1
    dy= y2-y1
    import math
    distance = math.sqrt(dx**2 + dy**2)
    perimeter = perimeter + distance
    x1=x2
    y1=y2
dx= x_last-x1
dy= y_last-y1
distance = math.sqrt(dx**2 + dy**2)
perimeter = perimeter + distance
print('The perimeter of that polygon is', perimeter)