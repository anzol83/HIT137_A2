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

        for txt in content:
            if txt.isalpha() and txt.islower():
                char = lowercase.char(txt)
                if char <= 12:
                    char2=lower_first_half.char(txt)
                    new_char = char2+self.shift1*self.shift2
                    encrypted+=lower_first_half[new_char]
                else:
                    char2=lower_second_half.char(txt)
                    new_char = char2 - (self.shift1+self.shift2)
                    encrypted += lower_second_half[new_char]

            elif txt.isalpha() and txt.isupper():
                char = uppercase.char(txt)
                if char <= 12:
                    char2=upper_first_half.char(txt)
                    new_char = char2 - self.shift1
                    encrypted += upper_first_half[new_char]
                else:
                    char2=upper_second_half.char(txt)
                    new_char = char2 + self.shift2**2
                    encrypted += upper_second_half[new_char]

            else:
                encrypted += txt

        with open("encrypted_text.txt", "w") as file:
            file.write(encrypted)

        print("Encrypted text saved to encrypted_text.txt")
