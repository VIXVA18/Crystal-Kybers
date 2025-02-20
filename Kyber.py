import os
import random

def keygen():
    sk = os.urandom(32)  
    pk = os.urandom(32)
    return pk, sk

def encrypt(pk, message):
    nonce = os.urandom(16)  
    ciphertext = bytes(a ^ b for a, b in zip(message.encode(), nonce))  
    return ciphertext, nonce

def decrypt(sk, ciphertext, nonce):
    decrypted_message = bytes(a ^ b for a, b in zip(ciphertext, nonce))
    return decrypted_message.decode()

def main():
    pk, sk = keygen()
    print("Public Key:", pk.hex())
    print("Secret Key:", sk.hex())

    message = input("Enter the message to encrypt: ")

    ciphertext, nonce = encrypt(pk, message)
    print("Ciphertext:", ciphertext.hex())
    print("Nonce:", nonce.hex())

    decrypted_message = decrypt(sk, ciphertext, nonce)
    print("Decrypted Message:", decrypted_message)

    if message == decrypted_message:
        print("Decryption successful! The messages match.")
    else:
        print("Decryption failed! The messages do not match.")

if __name__ == "__main__":
    main()
