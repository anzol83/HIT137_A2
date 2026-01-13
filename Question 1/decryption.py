#Creating module for the decryption
#This code decrypts the encrypted file as per shift key provided by the user in main.py
#If the shift key doesn't match the encryption key Decryption gives totally different output
class decrypt():

    #Defining the function and paramaters
    def __init__(self, shift1, shift2):
        self.shift1 = shift1
        self.shift2 = shift2

    #Decryption function
    def start_decrypt(self):
        #This code checks the availability of encrypted file
        #If present, opens and reads the content in encrypted file and stores all values in variable "content"
        #If file is missing it returns the message 'file not found'
        try:
            file = open("encrypted_text.txt", "r")
            content = file.read()
            file.close()
        except FileNotFoundError:
            print("File Not Found!")
            return

        #As we are reversing the encryption process here we use the same alphabet mapping
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        lower_first_half="abcdefghijklm"
        lower_second_half="nopqrstuvwxyz"
        upper_first_half="ABCDEFGHIJKLM"
        upper_second_half="NOPQRSTUVWXYZ"

        #Same condition as in encryption but we are using it inversely to decrypt the content
        forward = self.shift1 * self.shift2
        backward = self.shift1 + self.shift2
        decrypted = ""

        #Process goes through each character of encyrpted text
        #Applies in the condition for upper and lowercase as well as 1st and 2nd halves
        #Inverse each of the encrypted text as per shift key skips the non aplpha characters
        for txt in content:
            if txt.isalpha() and txt.islower():
                index = lowercase.index(txt)
                if index <= 12:
                    index2=lower_first_half.index(txt)
                    new_index = (index2 - forward) % 13
                    decrypted+=lower_first_half[new_index]
                else:
                    index2=lower_second_half.index(txt)
                    new_index = (index2 + backward) % 13
                    decrypted += lower_second_half[new_index]

            elif txt.isalpha() and txt.isupper():
                index = uppercase.index(txt)
                if index <= 12:
                    index2=upper_first_half.index(txt)
                    new_index = (index2 + self.shift1) % 13
                    decrypted += upper_first_half[new_index]
                else:
                    index2=upper_second_half.index(txt)
                    new_index = (index2 - self.shift2**2) % 13
                    decrypted += upper_second_half[new_index]

            else:
                decrypted += txt  

        #Saves the decrypted text as a file
        #returns the decrypted text in variable
        file=open("decrypted_text.txt", 'w')
        file.write(decrypted)
        return decrypted