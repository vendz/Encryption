from cryptography.fernet import Fernet
import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

print('\nthe password that you will Enter below will generate a unique key to Encrypt or Decrypt your Data')
print('Also use the same password to Encrypt and Decrypt your data')
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

print("""\n      :::::::: ::::::::: :::   ::::::::::::::::::::::: 
    :+:    :+::+:    :+::+:   :+::+:    :+:   :+:      
   +:+       +:+    +:+ +:+ +:+ +:+    +:+   +:+       
  +#+       +#++:++#:   +#++:  +#++:++#+    +#+        
 +#+       +#+    +#+   +#+   +#+          +#+         
#+#    #+##+#    #+#   #+#   #+#          #+#          
######## ###    ###   ###   ###          ###                   \n\n""")


while True:
    ef_df = input("do you want to work with files or text (F or T): ")   #asking client if he/she wan't to work with file or message 
    if ef_df.lower() not in ('f', 't'):
        print("plaese enter valid character!")
        continue

    else:
        if ef_df.upper() == 'F':
            while True:
                ask_input_f = input('do you want to encrypt or decrypt the file (E or D): ')
                if ask_input_f.lower() not in ('e', 'd'): 
                    print("please enter a valid character!")
                    continue
                else:
                    if ask_input_f.upper() == 'E':
                        while True:
                            try:
                                filename = input("copy the file path with it's name and extension and paste it here to Encrypt: ")
                                filename_replace = filename.replace('\\ ', " ")
                                with open(filename_replace, 'rb') as ef:    #we will open a file with read byte
                                    e_file = ef.read()
                            except FileNotFoundError:
                                print("Pleaase enter a valid file name or enter full file path!\n")
                                continue
                            else:
                                encrypted_file = f.encrypt(e_file)
                                user_filename_en = input("what would you like to name the encrypted file (with extension): ")    #we ask the user to name the encrypted file
                                with open(user_filename_en, 'wb') as ef:    #we will create new file with encrypted data in it with write byte
                                    ef.write(encrypted_file)
                                break

                    elif ask_input_f.upper() == 'D':
                        while True:
                            try:
                                d_filename = input("copy the file path with it's name and extension and paste it here to Decrypt: ")
                                d_filename_replace = d_filename.replace('\\ ', ' ')
                                with open(d_filename_replace, 'rb') as df:      #we will open a file with read byte
                                    encrypted_data = df.read()
                            except FileNotFoundError:
                                print("Please enter a valid name or enter full file path!\n")
                                continue
                            else:
                                decrypted_file = f.decrypt(encrypted_data)
                                user_filename_de = input("what would you like to name the decrypted file (with extension): ")
                                with open(user_filename_de, 'wb') as ddf:    #we will create new file with decrypted data in it with write byte
                                    ddf.write(decrypted_file)
                                break
                    break

        elif ef_df.upper() == 'T':
            while True:
                ask_input = input('do you want to encrypt or decrypt (E or D): ')
                if ask_input.lower() not in ('e', 'd'):
                    print("Please enter a valid character!")
                    continue

                else:
                    if ask_input.upper() == 'E':
                        message = input('enter a message you want to encrypt: ')
                        byte_message = bytes(message, 'utf-8')     #converting user input to byte array
                        byte_encrypted_message = f.encrypt(byte_message)  
                        encrypted_message = byte_encrypted_message.decode('utf-8')
                        print(encrypted_message)

                    elif ask_input.upper() == 'D':
                        en_message = input('enter the encrypted message: ') #copy the encrypted key and paste it here(copy without the b' ')
                        byte_en_message = bytes(en_message, 'utf-8')  #converting the message to byte array
                        decrypt_message = f.decrypt(byte_en_message)
                        original_message = decrypt_message.decode()  #converting byte array to string
                        print("----------------------------------------------------------Decrypted Message-------------------------------------------------------------------------")
                        print(original_message + '\n')
                        print('----------------------------------------------------------------------------------------------------------------------------------------------------')
                    break
                
        else :
            print("please enter a valid character.")
        break