string = input('Enter a string: ')
left = 0
right = len(string) - 1
while left < right:
        if string[left] != string[right]:
            print(string, 'is not a palindrome')
            break
        else: 
            print(string, 'is a palindrome')
            break