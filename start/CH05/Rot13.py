#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Ray G Peckham

def caesar_encrypt(message: str, shift: int) -> str:
    """
    Encrypt a message by shifting each letter a shift amount
    A-Z
    a-z

    """

    result = []

    for char in message:
        if char.isupper():
            shifted = (ord(char) - ord("A") + shift) % 26 + ord("A")
            result.append(chr(shifted))
        elif char.islower():
            shifted = (ord(char) - ord("a") + shift) % 26 + ord("a")
            result.append(chr(shifted))
        else:
            result.append(char)

    return "".join(result)


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """
    Decrypt a caesar cipher message by shifting letters backwards
    """
    return caesar_encrypt(ciphertext, -shift)
    
def get_shift_value() -> int:
    """
    Prompt user for an amount of shifts to take
    """
    while True:
        try:
            shift = int(input("Enter a value between 1-25: "))
            if 1 <= shift <= 25:
                return shift
            print(" Please enter a valid shift")
        except ValueError:
            print("That is not a valid number or integer")

def main():
    print("Caesar Cipher Encrypt and Decrypt")
    message = input("Enter a message: ").strip()
    if not message:
        print("No message entered. Exiting")
        return
    
    #get the shift value
    shift = get_shift_value()

    #Encrypt
    encrypted = caesar_encrypt(message, shift)
    print(F"Encrypted message: {encrypted}")

    #Decrypted if user even wants to?
    answer = input("decrypt the message? (yes/no): ").strip().lower()

    if answer in ("yes", "y"):
        decrypted = caesar_decrypt(encrypted, shift)
        print(F"decrypted message: {decrypted}")

        #confirm
        match = decrypted == message
        print("validation of match")
    else:
        print("Decryption skipped")
    print()
if __name__ == "__main__":
    main()