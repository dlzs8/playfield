#!/usr/bin/env python3
import simplecrypt

with open('encrypted.bin', 'rb') as inp:
    encrypted = inp.read()

with open('passwords.txt', 'r') as inp:
    passwords = inp.read().split()

output = None

for password in passwords:
    try:
        output = simplecrypt.decrypt(password, encrypted)
    except simplecrypt.DecryptionException:
        print("Wrong password", password, "skipping...")
    if output is not None: 
        print("Decrypted! Right password is", password)
        break

print(output)
