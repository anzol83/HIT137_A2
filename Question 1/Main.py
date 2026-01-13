from encryption import encrypt
from decryption import decrypt

while True:
    choice = input("Enter 1 to encrypt, 2 to decrypt or 3 to exit: ")
    if choice=="1" or choice=="2":
        while True:
            try:
                shift_1=int(input("Enter shift 1 Key: "))
                shift_2=int(input("Enter shift 2 Key: "))
                break
            except ValueError:
                print("Please enter Integers")

    elif choice=="3":
        pass
    else:
        print("Please enter valid number: ")

    if choice == "1":
        process1 = encrypt(shift_1, shift_2)
        process1.start_encrypt()
        
    elif choice == "2":
        process2 = decrypt(shift_1, shift_2)
        decrypted_text = process2.start_decrypt()

        file1=open("raw_text.txt", "r")
        raw_content=file1.read()

        if raw_content==decrypted_text:
            print("File Decrypted Secussfully.")
            print("Verification Successful. Content matches original data")
        else:
            print("Error Decryption!")
            print("Content doesn't match original data.")
        
    elif choice=="3":
        break
      
    else:
        print("Please enter valid number.")
