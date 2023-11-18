S=0
i=0
print('Enter letter grade: ', end='')
n=input()
while n!='':
    if n=='A+' or n=='A':
        S= S + 4.0
    elif n=='A-':
        S= S +3.7
    elif n=='B+':
        S= S +3.3
    elif n=='B':
        S= S +3.0
    elif n=='B-':
        S= S +2.7
    elif n=='C+':
        S= S +2.3
    elif n=='C':
        S= S +2.0
    elif n=='C-':
        S= S +1.7
    elif n=='D+':
        S= S +1.3
    elif n=='D':
        S= S +1
    elif n=='F':
        S= S +0
    i=i+1
    print('Enter letter grade: ', end='')
    n=input()
PointAverage=S/i
print('Point Average =',PointAverage)
