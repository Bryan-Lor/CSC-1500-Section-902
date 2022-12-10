# Bryan Lor 
# Project 3 - Problem One Method One
# Caesar Cipher

def CaesarCipher(shift, msg, decrypt = False):
    cipher = ""
    for char in msg:
        if decrypt:
            cipher += chr(ord(char) - shift)
        else:
            cipher += chr(ord(char) + shift)
    return cipher

def main():
    shift = 3
    print("Caesar Cipher - Problem One")
    message = input("Enter The Message: ")
    print("-------------------------------------------\n")

    # Encryption
    encryptedMessage = CaesarCipher(shift, message)
    print("Encrypted Message:", encryptedMessage)

    # Decryption
    decryptedMessage = CaesarCipher(shift, encryptedMessage, True)
    print("Decrypted Message:", decryptedMessage)

main()