from cryptography.fernet import Fernet
import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = input("enter your password: ")  #this is input in form of a string
password = password_provided.encode()  # convert to typr bytes

salt = b'w\x8a\x0b\x93f}\xd7u\xecD/3\xda\x1e\x05\xbd'
kdf = PBKDF2HMAC (
    algorithm = hashes.SHA256(),
    length = 32,
    salt = salt,
    iterations = 100000,
    backend = default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))  #can only use KDF(key derivation function) once
f = Fernet(key)

message = input('enter a message you want to encrypt: ')
byte_message = bytes(message, 'utf-8')
encrypted_message = f.encrypt(byte_message)
print(encrypted_message)

decrypt_message = f.decrypt(encrypted_message)
print(decrypt_message)
