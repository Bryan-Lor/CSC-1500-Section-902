# Bryan Lor 
# Project 3 - Problem Three
# Lor Cipher

def LorCipher(msg, keycode, decrypt = False):
    cipher = ""
    keycodeLength = len(keycode) - 1
    keyIndex = 0
    for char in msg:
        if(keyIndex > keycodeLength):
            keyIndex = 0
        
        if decrypt:
            cipher += chr(ord(char) - int(keycode[keyIndex]))
        else:
            cipher += chr(ord(char) + int(keycode[keyIndex]))

        keyIndex += 1
    return cipher

def main():
    print("Lor Cipher - Problem Three")
    message = input("Enter The Message: ")
    keycode = ""
    while not keycode.isdigit():
        keycode = input("Enter A Numerical Keycode: ")
    print("-------------------------------------------\n")

    # Encryption
    encryptedMessage = LorCipher(message, keycode)
    print("Encrypted Message:", encryptedMessage)

    # Decryption
    decryptedMessage = LorCipher(encryptedMessage, keycode, True)
    print("Decrypted Message:", decryptedMessage)

main()