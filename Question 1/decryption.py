class decrypt():
    def __init__(self, shift1, shift2):
        self.shift1=shift1
        self.shift2=shift2

    def start_decrypt(self):
        file=open("encrypted_text.txt", "r")
        content=file.read()
        file.close()

        lowercase="abcdefghijklmnopqrstuvwxyz"
        uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_first_half="abcdefghijklm"
        lower_second_half="nopqrstuvwxyz"
        upper_first_half="ABCDEFGHIJKLM"
        upper_second_half="NOPQRSTUVWXYZ"

        decrypted=""

        for txt in content:
            if txt.isalpha and txt.islower:
                letter=lowercase
                if letter<="m":
                    txt=lower_first_half.letter(txt)
                    decrypted=letter-self.shift1*self.shift2
                else:
                    txt=lower_second_half.letter(txt)
                    decrypted=letter-self.shift1+self.shift2

            elif txt.isalpha and txt.isupper:
                letter=uppercase
                if letter<="M":
                    txt=upper_first_half.letter(txt)
                    decrypted=letter+self.shift1
                else:
                    txt=upper_second_half.letter(txt)
                    decrypted=letter-self.shift2**2
            else:
                decrypted=txt
            
        file=open("decrypted_text.txt", "a")
        file.write(decrypted)