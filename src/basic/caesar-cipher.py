import sys

def encrypt(message, shift):
    encMessage = ""

    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            encMessage += chr((ord(char) + shift-65) % 26 + 65)
        else:
            encMessage += chr((ord(char) + shift - 97) % 26 + 97)

    return encMessage

def decrypt(message, shift):
    decMessage = ""

    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            decMessage += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            decMessage += chr((ord(char) - shift - 97) % 26 + 97)
        
    return decMessage

def bruteforce(message):

    return message


while True:
    message = input("Original Message:")
    shift = input("Shift:")
    shift = int(shift)
    encMessage = encrypt(message, shift)
    print("Encrypted Message:{}".format(encMessage))
    decMessage = decrypt(encMessage, shift)
    print("Decrypted Message:{}".format(decMessage))
