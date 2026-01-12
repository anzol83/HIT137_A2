class encrypt():
    def __init__(self, shift1, shift2):
        self.shift1 = shift1
        self.shift2 = shift2

    def start_encrypt(self):
        file = open("raw_text.txt", "r")
        content = file.read()
        file.close()

        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        lower_first_half="abcdefghijklm"
        lower_second_half="nopqrstuvwxyz"
        upper_first_half="ABCDEFGHIJKLM"
        upper_second_half="NOPQRSTUVWXYZ"

        forward = self.shift1 * self.shift2
        backward = self.shift1 + self.shift2
        encrypted = ""

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
                encrypted += txt 

        with open("encrypted_text.txt", "w") as file:
            file.write(encrypted)

        print("Encrypted text saved to encrypted_text.txt")
