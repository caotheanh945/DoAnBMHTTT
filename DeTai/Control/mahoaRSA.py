import math
#==============================
e=65537; n=4255903; d=2480777

class CRSA:
    def MaHoa(self,p,e,n):
        ci = []
        for c in p:
            m = ord(c)
            kq = pow(m,e,n)
            ci.append(kq)
        return ci
    #===============================
    def GiaiMa(self,ci,d,n):
        s = ''
        for c in ci:
            kq = pow(c,d,n) 
            s+=chr(kq)
        return s
    #===============================
def Run():
    p = input('Mời nhập chuỗi cần mã hoá: ')
    cRSA = CRSA()
    ci = cRSA.MaHoa(p,e,n)
    print('Sau khi mã hoá: ',end='')
    for i in ci:
        print("%X" % i,end=' ')
    print('\n')
    s = cRSA.GiaiMa(ci,d,n)
    print('Sau khi giải mã: %s'%s)

    
#===============================
if __name__ == '__main__':
    Run()
