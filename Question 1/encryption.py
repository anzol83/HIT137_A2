#Creating class for the encryption
#This code encrypts the file as per shift key provided by the user in main.py
class encrypt():

    #Defining the function and paramaters
    def __init__(self, shift1, shift2):
        self.shift1 = shift1
        self.shift2 = shift2

    #Encryption function
    def start_encrypt(self):
        #This code opens and reads the content in original file and stores all values in variable "content"
        file = open("raw_text.txt", "r")
        content = file.read()
        file.close()

        #Here we create the custom mapping of alphabets where a=0, b=2 and so on.
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        #Dividing both uppercase and lowercase alphabets in 2 halves
        #This makes the code more easier as the condition of programs is to encrypt the content in 2 halves of alphabets
        lower_first_half="abcdefghijklm"
        lower_second_half="nopqrstuvwxyz"
        upper_first_half="ABCDEFGHIJKLM"
        upper_second_half="NOPQRSTUVWXYZ"

        #Given condition on how to encrypt each letter as per the halves
        #and Creating another variable that can contain the encrypted text
        forward = self.shift1 * self.shift2
        backward = self.shift1 + self.shift2
        encrypted = ""

        #This part goes through each charcters in original content
        #Checks for the lowercase or uppercase or others.
        #Compares the position of letter (if it's in 1st half or 2nd half)
        #Encrypts each letter as per condition, skips all non alpha characters
        #Stores each encrypted text in 'encrypted' variable
        for txt in content:
            if txt.isalpha() and txt.islower():
                index = lowercase.index(txt)
                if index <= 12:
                    index2=lower_first_half.index(txt)
                    new_index = (index2 + forward) % 13
                    encrypted+=lower_first_half[new_index]
                else:
                    index2=lower_second_half.index(txt)
                    new_index = (index2 - backward) % 13
                    encrypted += lower_second_half[new_index]

            elif txt.isalpha() and txt.isupper():
                index = uppercase.index(txt)
                if index <= 12:
                    index2=upper_first_half.index(txt)
                    new_index = (index2 - self.shift1) % 13
                    encrypted += upper_first_half[new_index]
                else:
                    index2=upper_second_half.index(txt)
                    new_index = (index2 + self.shift2**2) % 13
                    encrypted += upper_second_half[new_index]

            else:
                # leave numbers, spaces, symbols unchanged
                encrypted += txt

        #finally saves the encrypted content in a file
        with open("encrypted_text.txt", "w") as file:
            file.write(encrypted)

        print("Encrypted text saved to encrypted_text.txt")
