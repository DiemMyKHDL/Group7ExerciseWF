message = input("Enter the message to encrypt/decrypt: ")
shift = int(input("Enter the shift value: "))
message = message.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
translated_message = ''
for char in message:
    if char in alphabet:
        index = alphabet.find(char)
        shifted_index = (index + shift) % 26
        translated_message = translated_message + shifted_alphabet[shifted_index]
    else:
        translated_message = translated_message + char
print("Encrypted/Decrypted message:", translated_message)