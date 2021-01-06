from cryptography.fernet import Fernet
import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import tkinter as tk
from tkinter import filedialog, Text
from tkmacosx import Button
from PIL import ImageTk, Image
from tkfilebrowser import askopenfilenames, askopendirnames, asksaveasfilename
from tkinter.messagebox import askyesno
import tkinter.ttk as ttk

#---initialising window---
root = tk.Tk()

#---defining default window size---
root.geometry("1400x1600")

#---giving title to window---
root.title("CRYPT")
#----------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------Defining Variables----------------------------------------------------------

global password
global result
password = tk.StringVar()
mode = tk.StringVar()
result = tk.StringVar()

#----------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------Adding Encryption Algorithm----------------------------------------------------

password_bytes = (password.get()).encode()
salt = b'w\x8a\x0b\x93f}\xd7u\xecD/3\xda\x1e\x05\xbd'
kdf = PBKDF2HMAC (
    algorithm = hashes.SHA256(),
    length = 32,
    salt = salt,
    iterations = 100000,
    backend = default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password_bytes))  #can only use KDF(key derivation function) once
f = Fernet(key)

#----------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------Adding Functions---------------------------------------------------------------

#---Function for file dialog---
def add_file():
    input_file = filedialog.askopenfilename(initialdir = "/", title = 'select file', filetypes = (("all files", "*.*"),("PNG", "*.png"),("JPG","*.jpg")))
    #---for printing selected file's name---
    label1 = tk.Label(frame_left, text = input_file, bg = "grey")
    label1.grid(row=1, column=2)

#---Function to quit software---
def quit_program():
    root.destroy()

#---Function to Reset the fields---
def reset(label1):
    password.set("")
    mode.set("")
    result.set("")
    label1.destroy()

#---Function to encrypt---
def encrypt(input_file):
    with open(input_file, 'rb') as ef:               #we will open a file with read byte
        e_file = ef.read()
    encrypted_file = f.encrypt(e_file)
    with open("encrypted_file", 'wb') as ef:         #we will create new file with encrypted data in it with write byte
        ef.write(encrypted_file)

#---Function to decrypt---
def decrypt(input_file):
    with open(input_file, 'rb') as df:                #we will open a file with read byte
        encrypted_data = df.read()
    decrypted_file = f.decrypt(encrypted_data)
    with open('decrypted_file', 'wb') as ddf:         #we will create new file with decrypted data in it with write byte
        ddf.write(decrypted_file)

#---Function to select mode and show result---
def results(input_file):
    results_mode = mode.get()
    results_input_file = input_file.get()
    if results_mode.lower() == 'e':
        encrypt(results_input_file)
        result.set('File is Encrypted! ')

    elif results_mode.lower() == 'd':
        decrypt(results_input_file)
        result.set('File is decrypted! ')

    else:
        result.set('Input a Valid character in \'Mode\' entry field')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------Designing UI-----------------------------------------------------------------

#---defining a frames---
frame_top = tk.Frame(root, width=1600, relief=tk.FLAT)
frame_top.pack(side=tk.TOP)

frame_left = tk.Frame(root, width=800, relief=tk.FLAT)
frame_left.pack(side=tk.LEFT)

#---giving heading for program---
heading = tk.Label(frame_top,font=('helvetica', 50, 'bold'), text = "Encryption and Decryption\nusing Vendz cipher", fg = "black", bd=10, anchor='w')
heading.grid(row=0, column=0)

#---label for file---
file_label = tk.Label(frame_left, font=('ariel', 16, 'bold'), text='Select a File:', fg='black', anchor='w')
file_label.grid(row=1, column=0)

#---asking for file---
file_button = Button(frame_left, text = "open file", padx = 10, pady = 5, bg = "#263D42", fg = "white", activebackground = "#263D32", command = add_file)
file_button.grid(row=1, column=1)

#---label for password---
label_password = tk.Label(frame_left, font=('ariel', 16, 'bold'), text='Enter the Password', bd=16, anchor='w')
label_password.grid(row=2, column=0)

#---asking for password---
password_input = tk.Entry(frame_left, font=('ariel', 16, 'bold'), textvariable=password, bd=10, insertwidth=4, bg='powder blue', justify='right', relief=tk.FLAT)
password_input.grid(row=2, column=1)

#---label for mode selection---
mode_label = tk.Label(frame_left, font=('ariel', 16, 'bold'),padx=20, text='Do you want to Encrypt(\'e\') or Decrypt(\'d\')', bd=16, anchor='w')
mode_label.grid(row=3, column=0)

#---asking for mode input---
mode_input = tk.Entry(frame_left, font=('ariel', 16, 'bold'), textvariable=mode, bd=10, insertwidth=4, bg='powder blue', justify='right', relief=tk.FLAT)
mode_input.grid(row=3, column=1)

#---result label---
label_result = tk.Label(frame_left, font=('ariel', 16, 'bold'), pady=20, padx=20, bd=16, text='Result', anchor='w')
label_result.grid(row=2, column=2)

#---result messagebox---
result_display = tk.Entry(frame_left, font=('ariel', 16, 'bold'), textvariable=result, bd=10, insertwidth=4, bg='powder blue', justify='right', relief=tk.FLAT)
result_display.grid(row=2, column=3)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------Buttons-------------------------------------------------------------------

#---Result Button---
result_button = Button(frame_left, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=50, text="Result", bg="powder blue", command=results).grid(row=7, column=1)

#---Reset Button---
reset_button = Button(frame_left, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=50, text="Reset", bg="green", command=reset).grid(row=7, column=2)

#---Exit Button---
exit_button = Button(frame_left, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=50, text="Exit", bg="red", command=quit_program).grid(row=7, column=3)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
root.mainloop()
