from encryption import encrypt
from decryption import decrypt

while True:
    while True:
        choice=input("Enter 1 to Encrypt, 2 to Decrypt or 3 to exit: ")
        if choice=="1" or choice=="2" or choice=="3":
            break
        else:
            print("Please enter valid number")

    if choice=="1":
        shift_1=int(input("Enter shift 1 key: "))
        shift_2=int(input("Enter shift 2 key: "))
        process1=encrypt(shift_1, shift_2)
        process1.start_encrypt()

    elif choice=="2":
        shift_1=int(input("Enter shift 1 key: "))
        shift_2=int(input("Enter shift 2 key: "))
        process2=decrypt(shift_1, shift_2)
        process2.start_decrypt()

    else:
        break