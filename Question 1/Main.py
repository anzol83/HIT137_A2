from encryption import encrypt
from decryption import decrypt

while True:
    while True:
        choice = input("Enter 1 to encrypt, 2 to decrypt: ")
        if choice=="1" or choice=="2":
                break
        else:
            print("Please enter valid number: ")

    while True:
        try:
            shift_1=int(input("Enter shift 1 Key: "))
            shift_2=int(input("Enter shift 2 Key: "))
            break
        except ValueError:
            print("Please enter Integers")

    if choice == "1":
        process1 = encrypt(shift_1, shift_2)
        process1.start_encrypt()
        
    elif choice == "2":
        process2 = decrypt(shift_1, shift_2)
        text=process2.start_decrypt()
        print("Decrypted message is:")
        print(text)
      
    else:
        print("Please enter 1 or 2.")