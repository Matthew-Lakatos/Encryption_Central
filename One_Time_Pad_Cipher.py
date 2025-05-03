import os
import base64

class Solution:
    def __init__(self):
        self.plaintext = input("Enter the text you would like to encrypt:\n").encode('utf-8')
        self.key = os.urandom(len(self.plaintext))  # truly random key, same length as plaintext

    def encode(self):
        ciphertext = bytes([p ^ k for p, k in zip(self.plaintext, self.key)])
        print("\nEncrypted (base64):")
        print(base64.b64encode(ciphertext).decode('utf-8'))
        print("\nKey (base64):")
        print(base64.b64encode(self.key).decode('utf-8'))
        print(''' ____________________________
                  WARNING - ONLY EVER USE ONCE 
                  ____________________________''')
        return ciphertext

    def decode(self, ciphertext: bytes, key: bytes):
        decrypted = bytes([c ^ k for c, k in zip(ciphertext, key)])
        print("\nDecrypted Text:")
        print(decrypted.decode('utf-8'))
        return decrypted
