class CVignere:
    def __init__(self, plaintext="",key="",ciphertext=""):
        self.plaintext=plaintext
        self.key=key
        self.ciphertext=ciphertext
    #========================================
    def MaHoa(self):
        self.ciphertext=""
        for i in range(len(self.plaintext)):
            c = self.plaintext[i]
            vt_key=i% len(self.key)
            if c!=' ' and c!= '\n':
                so = ord(c) - 33;
                so_key=ord(self.key[vt_key])-33+1 #????
                so = (so+so_key) % 65500
                self.ciphertext = self.ciphertext+ chr(so+ 33)
            elif c == '\n':
                self.ciphertext=self.ciphertext + '\n'
            else:
                self.ciphertext=self.ciphertext+self.key[vt_key]
        return self.ciphertext
    #========================================
    def GiaiMa(self):
        self.plaintext = ""
        for i in range(len(self.ciphertext)):
            c=self.ciphertext[i]
            vt_key=i%len(self.key)
            if c != self.key[vt_key] and c!= '\n':
                so = ord(c)- 33
                so_key=ord(self.key[vt_key])-33+1 #?????
                so = (so - so_key + 65500) % 65500
                self.plaintext = self.plaintext+ chr(so+33)
            elif c == '\n':
                self.plaintext = self.plaintext+ '\n'
            else:
                self.plaintext = self.plaintext+' '
        return self.plaintext
#========================================
def main():
    p =  input("Mời nhập chuỗi cẫn mã hóa: ")
    key= input("Mời nhập chuỗi key: ")
    cVignere= CVignere(p,key) 
    c = cVignere.MaHoa()
    print("Sau khi mã hóa= ", c)
    s= cVignere.GiaiMa()
    print("Sau khi giải mã= ",s)
#========================================
if __name__=="__main__": #entry point
    main()
