string = input("Enter a string: ")
cleaned_input = ''.join(char.lower() for char in string if char.isalnum())
is_palindrome = True
length = len(cleaned_input)
for i in range(length // 2):
    if cleaned_input[i] != cleaned_input[length - i - 1]:
        is_palindrome = False
        print(string, 'is not a palindrome')
        break
if is_palindrome:
    print(string, 'is a palindrome')