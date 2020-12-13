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

ef_df = input("do you want to work with files or text (F or T): ")   #asking client if he/she wan't to work with file or message 
if ef_df.upper() == 'F':
    ask_input_f = input('do you want to encrypt or decrypt the file (E or D): ')
    if ask_input_f.upper() == 'E':
        filename = input("copy the file you want to encrypt to this folder and enter it's name(also use the extension): ")
        with open(filename, 'rb') as s:    #we will open a file with read byte
            e_file = s.read()
        encrypted_file = f.encrypt(e_file)
        with open(filename + 'encrypted', 'wb') as ef:    #we will create new file with encrypted data in it with write byte
            ef.write(encrypted_file)

    elif ask_input_f.upper() == 'D':
        d_filename = input("copy the file you want to encrypt to this folder and enter it's name (also use the extension): ")
        with open(d_filename, 'rb') as df:      #we will open a file with read byte
            encrypted_data = df.read()
        decrypted_file = f.decrypt(encrypted_data)
        with open(d_filename + 'decrypted', 'wb') as ddf:    #we will create new file with decrypted data in it with write byte
            ddf.write(decrypted_file)

    else :
        print("please enter a valid character.")

elif ef_df.upper() == 'T':

    ask_input = input('do you want to encrypt or decrypt (E or D): ')
    if ask_input.upper() == 'E':
        message = input('enter a message you want to encrypt: ')
        byte_message = bytes(message, 'utf-8')     #converting user input to byte array
        encrypted_message = f.encrypt(byte_message)  
        print(encrypted_message)

    elif ask_input.upper() == 'D':
        en_message = input('enter the encrypted message: ') #copy the encrypted key and paste it here(copy without the b' ')
        byte_en_message = bytes(en_message, 'utf-8')  #converting the message to byte array
        decrypt_message = f.decrypt(byte_en_message)
        original_message = decrypt_message.decode()  #converting byte array to string
        print(original_message)

    else :
        print("please enter a valid character.")

else :
    print("please enter a valid character.")