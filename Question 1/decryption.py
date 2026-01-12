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

        forward = self.shift1 * self.shift2
        backward = self.shift1 + self.shift2
        decrypted = ""


        for txt in content:
            if txt.isalpha() and txt.islower():
                index = lowercase.index(txt)
                if index <= 12:
                    index2=lower_first_half.index(txt)
                    new_index = index2-forward
                    decrypted+=lower_first_half[new_index]
                else:
                    index2=lower_second_half.index(txt)
                    new_index = index2 + backward
                    decrypted += lower_second_half[new_index]

            elif txt.isalpha() and txt.isupper():
                index = uppercase.index(txt)
                if index <= 12:
                    index2=upper_first_half.index(txt)
                    new_index = index2 + self.shift1
                    decrypted += upper_first_half[new_index]
                else:
                    index2=upper_second_half.index(txt)
                    new_index = index2 - self.shift2**2
                    decrypted += upper_second_half[new_index]

            else:
                decrypted += txt  

        file=open("decrypted_text.txt", 'w')
        file.write(decrypted)