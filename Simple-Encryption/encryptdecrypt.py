from simplecrypt import encrypt, decrypt
import os, sys
ciphertext = ""
plaintext = ""

MODE = sys.argv[1]
FILENAME = sys.argv[2]
KEY = sys.argv[3]

def encrypt_file():
    with open(FILENAME, 'rb') as file:
        plaintext = file.read()
    encrypted = encrypt(KEY, plaintext)
    with open(FILENAME, 'wb') as file:
        file.write(encrypted)

def decrypt_file():
    with open(FILENAME, 'rb') as file:
        ciphertext = file.read()
    deccrypted = decrypt(KEY, ciphertext)
    with open(FILENAME, 'wb') as file:
        file.write(deccrypted)

if MODE == 'encrypt':
    encrypt_file()

elif MODE == 'decrypt':
    decrypt_file()
