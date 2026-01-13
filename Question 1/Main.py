from encryption import encrypt #Module that we created for ecnryption process
from decryption import decrypt #Module that we created for decryption process

while True:
    #User Intraction in program for the process
    #the option is kept as chr to avoid value error when str is entered
    choice = input("Enter 1 to encrypt, 2 to decrypt or 3 to exit: ")
    if choice=="1" or choice=="2":
        #Asks for the shift inputs from the user for encryption or decryption
        #Process continues until user inputs the valid numbers
        while True:
            try:
                shift_1=int(input("Enter shift 1 Key: "))
                shift_2=int(input("Enter shift 2 Key: "))
                break
            except ValueError:
                print("Please enter Integers")
    
    elif choice=="3":
        break
        #breaks the loop and program ends here
    else:
        pass
        #this allows the program to continue if user didn't exit the program
    
    if choice == "1":
        #Calls the encryption process from the module with (shift_1 & shift_2) attributes
        #encryption.py module does the rest of process
        process1 = encrypt(shift_1, shift_2)
        process1.start_encrypt()
        
    elif choice == "2":
        #Calls the decryption process from the module with shift attributes
        #decryption.py module works for the process
        #Gets return value of decrypted text and compares with the original file
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
        #here "decrypted_text" is return value of decrypted text from the module and "raw_content" is the original data
        #this process verifies the decrypted text and the original text
              
    else:
        #program repeats until user inputs valid option
        print("Please enter valid number.")
