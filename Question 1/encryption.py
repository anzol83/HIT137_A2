class encrypt():
    def __init__(self, shift1, shift2):
        self.shift1=shift1
        self.shift2=shift2

    def start_encrypt(self):
        file=open("raw_text.txt", "r")
        content=file.read()
        file.close()

        lowercase="abcdefghijklmnopqrstuvwxyz"
        uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for txt in content:
            if txt.isalpha and txt.islower:
                letter=lowercase
                if letter<="m":
                    txt=lowercase.letter(txt)
                    encrypt_letter=letter+self.shift1*self.shift2
                else:
                    txt=lowercase.letter(txt)
                    encrypt_letter=letter+self.shift1+self.shift2

            elif txt.isalpha and txt.isupper:
                letter=uppercase
                if letter<="M":
                    txt=uppercase.letter(txt)
                    encrypt_letter=letter-self.shift1
                else:
                    txt=uppercase.letter(txt)
                    encrypt_letter=letter+self.shift2**2
            else:
                encrypt_letter=txt
            
        file=open("encrypted_text.txt", "a")
        file.write(encrypt_letter)