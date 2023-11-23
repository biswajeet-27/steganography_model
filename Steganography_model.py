import cv2
import os
import string
import tkinter as tk

img=cv2.imread("D:/ocean.jpg")

password = ""
msg = ""
c={}

def encrypt_img():
    global password, img, msg, c
    msg = entry_msg.get()
    password = entry_password.get()  
    d={}
    
    for i in range(255):
        d[chr(i)]=i
        c[i]=chr(i)

        m=0
        n=0
        z=0
    
    for i in range(len(msg)):
        img[n, m, z]=d[msg[i]]
        n=n+1
        m=m+1
        z=(z+1)%3

    cv2.imwrite("Encryptedmsg.jpg", img)
    os.system("start Encryptedmsg.jpg")

def decrypt_img():
    global password, img, msg, c
    message=""
    n=0
    m=0
    z=0
    
    pas = entry_passcode.get()
    
    if password == pas:
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n=n+1
            m=m+1
            z=(z+1) % 3
        result_label.config(text="Decryption message: " + message)
            
    else:
        result_label.config(text="Not a valid key")


root = tk.Tk()
root.title("Image Encryption and Decryption")

frame_encrypt = tk.Frame(root)
frame_encrypt.pack(padx=10, pady=10)

label_msg = tk.Label(frame_encrypt, text="Enter secret message:")
label_msg.grid(row=0, column=0, sticky="e")

entry_msg = tk.Entry(frame_encrypt)
entry_msg.grid(row=0, column=1)

label_password = tk.Label(frame_encrypt, text="Enter password:")
label_password.grid(row=1, column=0, sticky="e")

entry_password = tk.Entry(frame_encrypt, show="*")
entry_password.grid(row=1, column=1)

encrypt_button = tk.Button(frame_encrypt, text="Encrypt Image", command=encrypt_img)
encrypt_button.grid(row=2, columnspan=2)


frame_decrypt = tk.Frame(root)
frame_decrypt.pack(padx=10, pady=10)

label_passcode = tk.Label(frame_decrypt, text="Enter passcode for Decryption:")
label_passcode.grid(row=0, column=0, sticky="e")

entry_passcode = tk.Entry(frame_decrypt, show="*")
entry_passcode.grid(row=0, column=1)

decrypt_button = tk.Button(frame_decrypt, text="Decrypt Image", command=decrypt_img)
decrypt_button.grid(row=1, columnspan=2)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
