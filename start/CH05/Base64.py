#!/usr/bin/env python3
# Script that "encrypts"/"decrypts" text using base64 encoding
# By Ray G Peckham

"""
This script is to take an input and encode and decode BASE64
"""

#imported libraries
import base64



def encode_to_base64(plaintext: str) -> str:
    """
encoding plain text to base64
we will do the following steps
1.) Convert the string using UTF-8
2.) Pass the bytes ijnto a function called b64,encode
3.) Resulted bytes in a return
    """
    text_as_bytes = plaintext.encode("utf-8")
    encoded_bytes = base64.b64encode(text_as_bytes)
    return encoded_bytes.decode("utf-8")

def decode_to_base_64(encoded_text: str) -> str:
    """
1.) Taking base64 string back to original plaintext
2.) Convert base64 string to get original bytes
3.) decode those bytes back to utf-8 string
    """
    encoded_as_bytes = encoded_text.encode("utf-8")
    decoded_bytes = base64.b64decode(encoded_as_bytes)
    return decoded_bytes.decode("utf-8")

#define main what we want to call and how

def main():
    print("Base 64 Encoder / Decoder")
    print(" THIS IS NOT ENCRYPTION")
    #user input of what ot encode
    message = input("Enter your message to encode: ").strip()
    #Step encode
    if not message:
        print("No message entered. Exiting")
        return
    #Encode
    encoded = encode_to_base64(message)
    print(f"Base64 : {encoded}")

    #decode
    decoded = decode_to_base_64(encoded)

    #vailidation
    match = decoded ==message
    print("Confirmation matched")
    print()



if __name__ == "__main__":
    main()