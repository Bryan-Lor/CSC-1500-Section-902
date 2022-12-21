# Bryan Lor 
# Project 3 - Problem Two
# Vigenere Cipher

def VigenereCipher(msg, keyword, decrypt = False):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    keywordLength = len(keyword) - 1
    keyIndex = 0

    for char in msg:
        if(keyIndex > keywordLength):
            keyIndex = 0
        if decrypt:
            cipherIndex = alphabet.find(char) - alphabet.find(keyword[keyIndex])
        else:
            cipherIndex = alphabet.find(char) + alphabet.find(keyword[keyIndex])
        if cipherIndex > len(alphabet):
            cipherIndex -= len(alphabet)
        cipher += alphabet[cipherIndex]
        keyIndex += 1
    return cipher

def main():    
    print("Vigenere Cipher - Problem Two")
    message = input("Enter The Message: ")
    keyword = input("Enter A Keyword: ")
    print("-------------------------------------------\n")

    # Encryption
    encryptedMessage = VigenereCipher(message, keyword)
    print("Encrypted Message:", encryptedMessage)

    # Decryption
    decryptedMessage = VigenereCipher(encryptedMessage, keyword, True)
    print("Decrypted Message:", decryptedMessage)

main()