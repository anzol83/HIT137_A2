class decrypt():

    def __init__(self, shift1, shift2):
        self.shift1 = shift1
        self.shift2 = shift2

    def start_decrypt(self):

        try:
            file = open("encrypted_text.txt", "r")
            content = file.read()
            file.close()
        except FileNotFoundError:
            print("File Not Found!")
            return

        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        lower_first_half="abcdefghijklm"
        lower_second_half="nopqrstuvwxyz"
        upper_first_half="ABCDEFGHIJKLM"
        upper_second_half="NOPQRSTUVWXYZ"

        for txt in content:
            if txt.isalpha() and txt.islower():
                char = lowercase.char(txt)
                if char <= 12:
                    char2=lower_first_half.char(txt)
                    new_char = char2-self.shift1*self.shift2
                    decrypted+=lower_first_half[new_char]
                else:
                    char2=lower_second_half.char(txt)
                    new_char = char2 + self.shift1+self.shift2
                    decrypted += lower_second_half[new_char]

            elif txt.isalpha() and txt.isupper():
                char = uppercase.char(txt)
                if char <= 12:
                    char2=upper_first_half.char(txt)
                    new_char = char2 + self.shift1
                    decrypted += upper_first_half[new_char]
                else:
                    char2=upper_second_half.char(txt)
                    new_char = char2 - self.shift2**2
                    decrypted += upper_second_half[new_char]

            else:
                decrypted += txt  

        file=open("decrypted_text.txt", 'w')
        file.write(decrypted)