import sys
sys.path.insert(0,"D:\\403_17_MaHoaVanBan\\DeTai\\Control") #Chèn đường dẫn để import các file mã hóa trong folder control
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QWidget, QMessageBox, QFileDialog, QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from mahoaceasar_class import CCeasar
from mahoavgnere_class import CVignere
from mahoabelasco_class import CBelasco
from mahoatrithemius_class import CTrithemius
from mahoachuyenvihaidong_class import CChuyenViHaiDong
from mahoachuyenvinhieudong_class import CChuyenViNhieuDong
from mahoaXorCeasar_class import CXORCeasar
from mahoaXorvignere_class import CXORVignere
from mahoaXortrithemius_class import CXORTrithemius
from mahoaXorbelasco_class import CXORBelasco
from mahoaRSA import CRSA
import mahoaSDES 
import mahoamd5
import mahoasha256
import mahoasha3
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sqlite3


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Demo.ui', self)


        #Kết nối với database
        self.conn = sqlite3.connect("ChuongTrinhMaHoa.db")
        #Tạo con trỏ
        self.cursor = self.conn.cursor()

        #Gọi sự kiện nút bấm đăng ký
        self.registerButton.clicked.connect(self.register)

        #Gọi sự kiện nút bấm đăng nhập
        self.loginButton.clicked.connect(self.login)

        #Gọi sự kiện nút hiển thị mật khẩu
        self.visible.clicked.connect(self.showPassword)
        self.visible_2.clicked.connect(self.showPassword2)
        self.visible_3.clicked.connect(self.showPassword3)


        #Gọi sự kiện nút đăng xuất
        self.logout.clicked.connect(self.showLoginPage)


        #Gọi sự kiện nút hiển thị trang đăng nhập
        self.buttonStart.clicked.connect(self.showLoginPage)

        #Gọi sự kiện nút hiển thị trang đăng ký
        self.signupButton.clicked.connect(self.ShowSignUpPage)
        
        #Gọi sự kiện nút mã hóa bằng phương pháp thay thế
        self.subEnc.clicked.connect(self.showSubEncPage)

        #Gọi sự kiện nút giải mã bằng phương pháp thay thế
        self.subDec.clicked.connect(self.showSubDecPage)

        #Gọi sự kiện nút mã hóa bằng phương pháp chuyển vị 
        self.transEnc.clicked.connect(self.showTransEncPage)

        #Gọi sự kiện nút giải mã bằng phương pháp thay thế
        self.transDec.clicked.connect(self.showTransDecPage)

        #Gọi sự kiện nút mã hóa bằng phương pháp XOR
        self.xorEnc.clicked.connect(self.showXorEncPage)

         #Gọi sự kiện nút giải mã bằng phương pháp XOR
        self.xorDec.clicked.connect(self.showXorDecPage)

      
        #Gọi sự kiện nút trở về màn hình login
        self.backlogin.clicked.connect(self.showLoginPage)
        

        #---------------------------------------------------- Caesar
        #Gọi sự kiện nút chạy phương pháp mã hóa Caesar
        self.caesarButton.clicked.connect(self.caesarEnc)
        self.encrypt_3.clicked.connect(self.execEnc3)
        self.openFile_3.clicked.connect(self.execOpen3)
        self.saveFile_3.clicked.connect(self.execSave3)




        #Gọi sự kiện nút chạy phương pháp giải mã Caesar
        self.caesarButton_6.clicked.connect(self.caesarDec)
        self.decrypt_13.clicked.connect(self.execDec13)
        self.openFile_13.clicked.connect(self.execOpen13)
        self.saveFile_13.clicked.connect(self.execSave13)

        

        #--------------------------------------------------- Vgnere
        #Gọi sự kiện nút chạy phương pháp mã hóa Vgnere
        self.vignereButton.clicked.connect(self.vignereEnc)
        self.encrypt_2.clicked.connect(self.execEnc2)
        self.openFile_2.clicked.connect(self.execOpen2)
        self.saveFile_2.clicked.connect(self.execSave2)

        #Gọi sự kiện nút chạy phương pháp giải mã Vgnere
        self.vignere_6.clicked.connect(self.vignereDec)
        self.decrypt_14.clicked.connect(self.execDec14)
        self.openFile_14.clicked.connect(self.execOpen14)
        self.saveFile_14.clicked.connect(self.execSave14)


        #--------------------------------------------------- Belasco
        self.belascoButton.clicked.connect(self.belascoEnc)
        self.encrypt_4.clicked.connect(self.execEnc4)
        self.openFile_4.clicked.connect(self.execOpen4)
        self.saveFile_4.clicked.connect(self.execSave4)

        #Gọi sự kiện nút chạy phương pháp giải mã Belasco  
        self.belascoButton_6.clicked.connect(self.belascoDec) 
        self.decrypt_15.clicked.connect(self.execDec15)
        self.openFile_15.clicked.connect(self.execOpen15)
        self.saveFile_15.clicked.connect(self.execSave15)


        #----------------------------------------------------Trithemius
        self.trithemiusButton.clicked.connect(self.trithemiusEnc)
        self.encrypt_5.clicked.connect(self.execEnc5)
        self.openFile_5.clicked.connect(self.execOpen5)
        self.saveFile_5.clicked.connect(self.execSave5)

        # Gọi sự kiện nút chạy phương pháp giải mã Trithemius
        self.trithemiusButton_6.clicked.connect(self.trithemiusDec)
        self.decrypt_16.clicked.connect(self.execDec28)
        self.openFile_16.clicked.connect(self.execOpen28)
        self.saveFile_16.clicked.connect(self.execSave28)


        #----------------------------------------------------- Mã hóa với chuyển vị hai dòng
        self.transTwoRowsEncButton.clicked.connect(self.twoRowsEnc)
        self.encrypt_6.clicked.connect(self.execEnc6)
        self.openFile_6.clicked.connect(self.execOpen6)
        self.saveFile_6.clicked.connect(self.execSave6)

        #----------------------------------------------------- Giải mã với chuyển vị hai dòng
        self.transTwoRowsDecButton.clicked.connect(self.twoRowsDec)
        self.decTransTwoRows.clicked.connect(self.execDec7)
        self.openFile_TransTwoRows.clicked.connect(self.execOpen7)
        self.saveFile_TransTwoRows.clicked.connect(self.execSave7)


        #----------------------------------------------------- Mã hóa với chuyển vị nhiều dòng
        self.transMultiRowsEncButton.clicked.connect(self.multiRowsEnc)
        self.encrypt_8.clicked.connect(self.execEnc8)
        self.openFile_8.clicked.connect(self.execOpen8)
        self.saveFile_8.clicked.connect(self.execSave8)


        #----------------------------------------------------- Giải mã với chuyển vị nhiều dòng
        self.transMultiRowsDecButton.clicked.connect(self.multiRowsDec)
        self.decTransMultiRows.clicked.connect(self.execDec9)
        self.openFile_TransMultiRows.clicked.connect(self.execOpen9)
        self.saveFile_TransMultiRows.clicked.connect(self.execSave9)



        #--------------------------------------------------------- Mã hóa với XOR Ceasar
        self.xorCeasarButton.clicked.connect(self.xorCeasarEnc)
        self.encrypt_XORCeasar.clicked.connect(self.execEnc10)
        self.openFile_XORCeasar.clicked.connect(self.execOpen10)
        self.saveFile_XORCeasar.clicked.connect(self.execSave10)


        #--------------------------------------------------------- Giải mã với XOR Ceasar
        self.xorCeasarButtonDec.clicked.connect(self.xorCeasarDec)
        self.decrypt_XORCeasar_Dec.clicked.connect(self.execDec11)
        self.openFile_XORCeasar_Dec.clicked.connect(self.execOpen11)
        self.saveFile_XORCeasar_Dec.clicked.connect(self.execSave11)


        #--------------------------------------------------------- Mã hóa với XOR Vignere
        self.xorVignereButton.clicked.connect(self.xorVignereEnc)
        self.encrypt_XORVignere.clicked.connect(self.execEnc12)
        self.openFile_XORVignere.clicked.connect(self.execOpen12)
        self.saveFile_XORVignere.clicked.connect(self.execSave12)

        #--------------------------------------------------------- giải mã với XOR Vignere
        self.xorVignereButtonDec.clicked.connect(self.xorVignereDec)
        self.decrypt_XORVignere_Dec.clicked.connect(self.execDec16)
        self.openFile_XORVignere_Dec.clicked.connect(self.execOpen16)
        self.saveFile_XORVignere_Dec.clicked.connect(self.execSave16)
        
        #--------------------------------------------------------- Mã hóa với XOR Belasco
        self.xorBelascoButton.clicked.connect(self.xorBelascoEnc)
        self.encrypt_XORBelasco.clicked.connect(self.execEnc26)
        self.openFile_XORBelasco.clicked.connect(self.execOpen26)
        self.saveFile_XORBelasco.clicked.connect(self.execSave26)

        #--------------------------------------------------------- Giải mã với XOR Belasco
        self.xorBelascoButtonDec.clicked.connect(self.xorBelascoDec)
        self.decrypt_XORBelasco_Dec.clicked.connect(self.execDec27)
        self.openFile_XORBelasco_Dec.clicked.connect(self.execOpen27)
        self.saveFile_XORBelasco_Dec.clicked.connect(self.execSave27)
        

        #--------------------------------------------------------- Mã hóa với XOR Trithemius
        self.xorTrithemiusButton.clicked.connect(self.xorTrithemiusEnc)
        self.encrypt_XORTrithemius.clicked.connect(self.execEnc17)
        self.openFile_XORTrithemius.clicked.connect(self.execOpen17)
        self.saveFile_XORTrithemius.clicked.connect(self.execSave17)


        #--------------------------------------------------------- Giải mã với XOR Trithemius
        self.xorTrithemiusButtonDec.clicked.connect(self.xorTrithemiusDec)
        self.decrypt_XORTrithemius_Dec.clicked.connect(self.execDec18)
        self.openFile_XORTrithemius_Dec.clicked.connect(self.execOpen18)
        self.saveFile_XORTrithemius_Dec.clicked.connect(self.execSave18)


        #------------------------------------------------------- Mã hóa với RSA
        self.rsaEnc.clicked.connect(self.showRSAEncpage)
        self.encrypt_RSA_2.clicked.connect(self.execEnc19)
        self.openFile_RSA_2.clicked.connect(self.execOpen19)
        self.saveFile_RSA_2.clicked.connect(self.execSave19)


        #------------------------------------------------------- giải mã với RSA
        self.rsaDec.clicked.connect(self.showRSADecpage)
        self.decrypt_RSA_Dec.clicked.connect(self.execDec20)
        self.openFile_RSA_Dec.clicked.connect(self.execOpen20)
        self.saveFile_RSA_Dec.clicked.connect(self.execSave20)


        #------------------------------------------------------- Mã hóa với DES
        self.desEnc.clicked.connect(self.showDesEncpage)
        self.encrypt_DES.clicked.connect(self.execEnc21)
        self.openFile_DES.clicked.connect(self.execOpen21)
        self.saveFile_DES.clicked.connect(self.execSave21)


        #------------------------------------------------------- giải mã với DES
        self.desDec.clicked.connect(self.showDesDecPage)
        self.decrypt_DES_2.clicked.connect(self.execDec22)
        self.openFile_DES_2.clicked.connect(self.execOpen22)
        self.saveFile_DES_2.clicked.connect(self.execSave22)


        #------------------------------------------------------- Mã hóa với MD5
        self.md5Enc.clicked.connect(self.showMD5EncPage)
        self.encrypt_MD5.clicked.connect(self.execEnc23)
        self.openFile_MD5.clicked.connect(self.execOpen23)
        self.saveFile_MD5.clicked.connect(self.execSave23)


        #------------------------------------------------------- Mã hóa với SHA-256
        self.sha256Enc.clicked.connect(self.showSHA256EncPage)
        self.encrypt_SHA_256.clicked.connect(self.execEnc24)
        self.openFile_SHA_256.clicked.connect(self.execOpen24)
        self.saveFile_SHA_256.clicked.connect(self.execSave24)



        #------------------------------------------------------- Mã hóa với SHA-3
        self.sha3Enc.clicked.connect(self.showSHA3EncPage)
        self.encrypt_SHA_3.clicked.connect(self.execEnc25)
        self.openFile_SHA_3.clicked.connect(self.execOpen25)
        self.saveFile_SHA_3.clicked.connect(self.execSave25)


        #---------------------------------------------------- Thông báo chưa chọn phương pháp mã hóa hoặc giải mã
        #Thông báo cho mã hóa thay thế
        self.encrypt_Empty.clicked.connect(self.notify)
        self.openFile_Empty.clicked.connect(self.notify)
        self.saveFile_Empty.clicked.connect(self.notify)
        #Thông báo cho mã hóa chuyển vị
        self.encrypt_Empty1.clicked.connect(self.notify)
        self.openFile_Empty1.clicked.connect(self.notify)
        self.saveFile_Empty1.clicked.connect(self.notify)
        #Thông báo cho mã hóa Xor
        self.encrypt_Empty2.clicked.connect(self.notify)
        self.openFile_Empty2.clicked.connect(self.notify)
        self.saveFile_Empty2.clicked.connect(self.notify)
        #Thông báo cho giải mã Xor
        self.decrypt_Empty3.clicked.connect(self.notify1)
        self.openFile_Empty3.clicked.connect(self.notify1)
        self.saveFile_Empty3.clicked.connect(self.notify1)
        #Thông báo cho mã hóa thay thế
        self.decrypt_Empty4.clicked.connect(self.notify1)
        self.openFile_Empty4.clicked.connect(self.notify1)
        self.saveFile_Empty4.clicked.connect(self.notify1)
        #Thông báo cho mã hóa chuyển vị
        self.decrypt_Empty5.clicked.connect(self.notify1)
        self.openFile_Empty5.clicked.connect(self.notify1)
        self.saveFile_Empty5.clicked.connect(self.notify1)

        #Gọi sự kiện nút trở về Options Page
        self.backOptions.clicked.connect(self.backOptionsPage)
        self.backOptions_2.clicked.connect(self.backOptionsPage)
        self.backOptions_3.clicked.connect(self.backOptionsPage)
        self.backOptions_4.clicked.connect(self.backOptionsPage)
        self.backOptions_5.clicked.connect(self.backOptionsPage)
        self.backOptions_6.clicked.connect(self.backOptionsPage)
        self.backOptions_7.clicked.connect(self.backOptionsPage)
        self.backOptions_8.clicked.connect(self.backOptionsPage)
        self.backOptions_9.clicked.connect(self.backOptionsPage)
        self.backOptions_10.clicked.connect(self.backOptionsPage)
        self.backOptions_11.clicked.connect(self.backOptionsPage)
        self.backOptions_12.clicked.connect(self.backOptionsPage)
        self.backOptions_13.clicked.connect(self.backOptionsPage)
        self.backOptions_14.clicked.connect(self.backOptionsPage)
        self.backOptions_15.clicked.connect(self.backOptionsPage)
        self.backOptions_16.clicked.connect(self.backOptionsPage)
        self.backOptions_17.clicked.connect(self.backOptionsPage)
        self.backOptions_18.clicked.connect(self.backOptionsPage)
        self.backOptions_19.clicked.connect(self.backOptionsPage)
        self.backOptions_20.clicked.connect(self.backOptionsPage)
        self.backOptions_21.clicked.connect(self.backOptionsPage)
        self.backOptions_22.clicked.connect(self.backOptionsPage)
        self.backOptions_23.clicked.connect(self.backOptionsPage)
        self.backOptions_24.clicked.connect(self.backOptionsPage)
        self.backOptions_25.clicked.connect(self.backOptionsPage)
        self.backOptions_26.clicked.connect(self.backOptionsPage)
        self.backOptions_27.clicked.connect(self.backOptionsPage)
        self.backOptions_28.clicked.connect(self.backOptionsPage)
        self.backOptions_29.clicked.connect(self.backOptionsPage)
        self.backOptions_30.clicked.connect(self.backOptionsPage)
        self.backOptions_31.clicked.connect(self.backOptionsPage)
        self.backOptions_32.clicked.connect(self.backOptionsPage)
        self.backOptions_33.clicked.connect(self.backOptionsPage)




        # Gọi sự kiện mở các chức năng mã hóa
        #-----------------Mã hóa Ceasar
        self.caesarButton_2.clicked.connect(self.caesarEnc)
        self.caesarButton_3.clicked.connect(self.caesarEnc)
        self.caesarButton_4.clicked.connect(self.caesarEnc)
        self.caesarButton_5.clicked.connect(self.caesarEnc)
        #----------------- Mã hóa Vignere
        self.vignere_2.clicked.connect(self.vignereEnc)
        self.vignere_3.clicked.connect(self.vignereEnc)
        self.vignere_4.clicked.connect(self.vignereEnc)
        self.vignere_5.clicked.connect(self.vignereEnc)
        #----------------- Mã hóa Belasco
        self.belascoButton_2.clicked.connect(self.belascoEnc)
        self.belascoButton_3.clicked.connect(self.belascoEnc)
        self.belascoButton_4.clicked.connect(self.belascoEnc)
        self.belascoButton_5.clicked.connect(self.belascoEnc)
        #----------------- Mã hóa Trithemius
        self.trithemiusButton_2.clicked.connect(self.trithemiusEnc)
        self.trithemiusButton_3.clicked.connect(self.trithemiusEnc)
        self.trithemiusButton_4.clicked.connect(self.trithemiusEnc)
        self.trithemiusButton_5.clicked.connect(self.trithemiusEnc)

        #---------------- Mã hóa hai dòng
        self.transTwoRowsEncButton_3.clicked.connect(self.twoRowsEnc)
        #---------------- Mã hóa nhiều dòng
        self.transMultiRowsEncButton_2.clicked.connect(self.multiRowsEnc)

        #---------------- Mã hóa XOR Ceasar
        self.xorCeasarButtonEnc_3.clicked.connect(self.xorCeasarEnc)
        self.xorCeasarButtonEnc_4.clicked.connect(self.xorCeasarEnc)

        #---------------- Mã hóa với XOR Vignere
        self.xorVignereButtonEnc_2.clicked.connect(self.xorVignereEnc)
        self.xorVignereButtonEnc_3.clicked.connect(self.xorVignereEnc)
        self.xorVignereButtonEnc_4.clicked.connect(self.xorVignereEnc)

        #---------------- Mã hóa với XOR Belasco
        self.xorBelascoButtonEnc_2.clicked.connect(self.xorBelascoEnc)
        self.xorBelascoButtonEnc_3.clicked.connect(self.xorBelascoEnc)
        self.xorBelascoButtonEnc_4.clicked.connect(self.xorBelascoEnc)

        #---------------- Mã hóa với XOR Trithemius
        self.xorTrithemiusButtonEnc_2.clicked.connect(self.xorTrithemiusEnc)
        self.xorTrithemiusButtonEnc_3.clicked.connect(self.xorTrithemiusEnc)
        self.xorTrithemiusButtonEnc_4.clicked.connect(self.xorTrithemiusEnc)


        
        # Gọi sự kiện mở các chức năng mã hóa và giải mã chung
        #----------------- giải mã Caesar
        self.caesarButton_7.clicked.connect(self.caesarDec)
        self.caesarButton_8.clicked.connect(self.caesarDec)
        self.caesarButton_9.clicked.connect(self.caesarDec)
        self.caesarButton_10.clicked.connect(self.caesarDec)

        #----------------- giải mã vignere
        self.vignere_7.clicked.connect(self.vignereDec)
        self.vignere_8.clicked.connect(self.vignereDec)
        self.vignere_9.clicked.connect(self.vignereDec)
        self.vignere_10.clicked.connect(self.vignereDec)

        #----------------- giải mã belasco
        self.belascoButton_7.clicked.connect(self.belascoDec)
        self.belascoButton_8.clicked.connect(self.belascoDec)
        self.belascoButton_9.clicked.connect(self.belascoDec)
        self.belascoButton_10.clicked.connect(self.belascoDec)

        #----------------- giải mã belasco
        self.trithemiusButton_7.clicked.connect(self.trithemiusDec)
        self.trithemiusButton_8.clicked.connect(self.trithemiusDec)
        self.trithemiusButton_9.clicked.connect(self.trithemiusDec)
        self.trithemiusButton_10.clicked.connect(self.trithemiusDec)

        # giải mã chuyển vị nhiều dòng
        self.transMultiRowsDecButton_4.clicked.connect(self.multiRowsDec)

        #giải mã với chuyển vị 2 dòng
        self.transTwoRowsDecButton_5.clicked.connect(self.twoRowsDec)


        #----------------- Giải mã XOR Ceasar
        self.xorCeasarButtonDec_2.clicked.connect(self.xorCeasarDec)
        self.xorCeasarButtonDec_3.clicked.connect(self.xorCeasarDec)
        self.xorCeasarButtonDec_4.clicked.connect(self.xorCeasarDec)
        self.xorCeasarButtonDec_5.clicked.connect(self.xorCeasarDec)


        #----------------- Giải mã XOR Vignere
        self.xorVignereButtonDec_2.clicked.connect(self.xorVignereDec)
        self.xorVignereButtonDec_3.clicked.connect(self.xorVignereDec)
        self.xorVignereButtonDec_4.clicked.connect(self.xorVignereDec)
        self.xorVignereButtonDec_5.clicked.connect(self.xorVignereDec)



        #---------------- Giải mã XOR Belasco
        self.xorBelascoButtonDec_2.clicked.connect(self.xorBelascoDec)
        self.xorBelascoButtonDec_3.clicked.connect(self.xorBelascoDec)
        self.xorBelascoButtonDec_4.clicked.connect(self.xorBelascoDec)
        self.xorBelascoButtonDec_5.clicked.connect(self.xorBelascoDec)



        #---------------- Giải mã XOR Trithemius
        self.xorTrithemiusButtonDec_2.clicked.connect(self.xorTrithemiusDec)
        self.xorTrithemiusButtonDec_3.clicked.connect(self.xorTrithemiusDec)
        self.xorTrithemiusButtonDec_4.clicked.connect(self.xorTrithemiusDec)
        self.xorTrithemiusButtonDec_5.clicked.connect(self.xorTrithemiusDec)

        


        # Tạo global var 
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.var = ''

        

        # ---------------------------------------------------------------------------------------
    
    # Xử lí sự kiện đăng kí tài khoản
    def register(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        confirmPassword = self.confirmPassword.text()

        self.cursor.execute("SELECT COUNT(*) FROM Account WHERE username=?", (username,))
        checkAccount = self.cursor.fetchone() # lấy một tuple chứa kết quả của truy vấn

        # Check validate
        if password != confirmPassword:
            QMessageBox.information(self, "Thông báo", "Mật khẩu chưa trùng khớp!")  
        elif not username or not password:
            QMessageBox.information(self, "Thông báo", "Tên đăng nhập và mật khẩu không được để trống!") 
        elif len(username) < 6 and len(password) <6:
            QMessageBox.information(self, "Thông báo", "Tên đăng nhập và mật khẩu phải có độ dài hơn 6 ký tự!")  
        elif checkAccount[0]>0: # kiểm tra xem giá trị checkAccount[0] có lớn hơn 0 không. Nếu có, nghĩa là đã tìm thấy ít nhất một dòng thỏa mãn điều kiện và tên đăng nhập đã tồn tại trong cơ sở dữ liệu.
            QMessageBox.information(self, "Thông báo", "Tên đăng nhập đã được sử dụng")  
        else:
            username_Enc = mahoasha3.MaHoaSha3(username) #mã hóa tên đăng nhập
            password_Enc = mahoasha3.MaHoaSha3(password) # mã hóa mật khẩu
            self.cursor.execute("INSERT INTO Account (username, password) VALUES (?, ?)", (username_Enc, password_Enc))
            self.conn.commit()
            QMessageBox.information(self, "Thông báo", "Đăng ký tài khoản thành công")  
            self.showLoginPage()

            self.cursor.execute("SELECT * FROM Account")
            accounts = self.cursor.fetchall()

            for account in accounts:
                print("account_id:", account[0])
                print("username:", account[1])
                print("password:", account[2])
                print()
    

    # Xử lí sự kiện đăng nhập
    def login(self):
        username = self.usernameInput_2.text()
        password = self.passwordInput_2.text()
        username_Enc = mahoasha3.MaHoaSha3(username) #mã hóa tên đăng nhập
        password_Enc = mahoasha3.MaHoaSha3(password) #mã hóa mật khẩu
        
        self.cursor.execute("SELECT * FROM Account WHERE username = ? AND password = ?", (username_Enc, password_Enc))
        account = self.cursor.fetchone()
        print(account)

        if account:
            self.showOptions()
        else:
            QMessageBox.information(self, "Thông báo", "Tên đăng nhập hoặc mật khẩu không đúng. Vui lòng thử lại!") 



    #Hàm hiển thị mặt khẩu ở trang đăng nhập
    def showPassword(self):
        # Chuyển đổi giữa Password và Normal
        current_mode = self.passwordInput_2.echoMode()
        new_mode = QLineEdit.Normal if current_mode == QLineEdit.Password else QLineEdit.Password
        self.passwordInput_2.setEchoMode(new_mode)

    #Hàm hiển thị mặt khẩu ở trang đăng ký
    def showPassword2(self):
        # Chuyển đổi giữa Password và Normal
        current_mode = self.passwordInput.echoMode()
        new_mode = QLineEdit.Normal if current_mode == QLineEdit.Password else QLineEdit.Password
        self.passwordInput.setEchoMode(new_mode)

    def showPassword3(self):
        # Chuyển đổi giữa Password và Normal
        current_mode = self.confirmPassword.echoMode()
        new_mode = QLineEdit.Normal if current_mode == QLineEdit.Password else QLineEdit.Password
        self.confirmPassword.setEchoMode(new_mode)

    #Tạo hàm chuyển đến trang Đăng nhập
    def showLoginPage(self):
        default_text = ""
        self.usernameInput_2.setText(default_text)
        self.passwordInput_2.setText(default_text)
        self.usernameInput_2.setFocus()
        self.stackedWidget.setCurrentWidget(self.Login)

    def ShowSignUpPage(self):
        self.stackedWidget.setCurrentWidget(self.SignUp)
    
    #Tạo hàm mỡ bảng lựa chọn phương thức (Options)
    def showOptions(self):
        self.stackedWidget.setCurrentWidget(self.Options)

    # Tạo hàm mã hóa bằng phương pháp thay thế SubEnc
    def showSubEncPage(self):
        self.stackedWidget.setCurrentWidget(self.SubEncPage)

    # Tạo hàm giải mã bằng phương pháp thay thế SubDec
    def showSubDecPage(self):
        self.stackedWidget.setCurrentWidget(self.SubDecPage)

    #Tạo hàm trở về trang Options
    def backOptionsPage(self):
        self.stackedWidget.setCurrentWidget(self.Options)

    # Tạo hàm chọn phương thức mã hóa Caesar
    def caesarEnc(self):
        self.stackedWidget.setCurrentWidget(self.CaesarEncPage)

    #Tạo hàm chọn phương thức giải mã Caesar
    def caesarDec(self):
        self.stackedWidget.setCurrentWidget(self.CaesarDecPage)


    # Tạo hàm chọn phương thức mã hóa vignere
    def vignereEnc(self):
        self.stackedWidget.setCurrentWidget(self.VignereEncPage)
    # Tạo hàm chọn phương thức giải mã vignere
    def vignereDec(self):
        self.stackedWidget.setCurrentWidget(self.VignereDecPage)


    # Tạo hàm chọn phương thức mã hóa với belasco
    def belascoEnc(self):
        self.stackedWidget.setCurrentWidget(self.BelascoEncPage)

    # Tạo hàm chọn phương thức giải mã với belasco
    def belascoDec(self):
        self.stackedWidget.setCurrentWidget(self.BelascoDecPage)

     # Tạo hàm chọn phương thức mã hóa với Trithemius
    def trithemiusEnc(self):
        self.stackedWidget.setCurrentWidget(self.TrithemiusEncPage)

    def trithemiusDec(self):    
        self.stackedWidget.setCurrentWidget(self.TrithemiusDecPage)


    #------------------------------------------------------------------- Phương pháp chuyển vị


    #Tạo hàm mở trang chọn phương pháp mã hóa chuyển vị
    def showTransEncPage(self):
        self.stackedWidget.setCurrentWidget(self.TransEncPage)

    # Tạo hàm mở trang chọn phương pháp giải mã chuyển vị
    def showTransDecPage(self):
        self.stackedWidget.setCurrentWidget(self.TransDecPage)


    #Tạo hàm chọn phương thức mã hóa chuyển vị 2 dòng
    def twoRowsEnc(self):
        self.stackedWidget.setCurrentWidget(self.TransTwoRowsEncPage)
    
    #Tạo hàm chọn phương thức giải mã chuyển vị 2 dòng
    def twoRowsDec(self):
        self.stackedWidget.setCurrentWidget(self.TransTwoRowsDecPage)


    #Tạo hàm chọn phương thức mã hóa chuyển vị 2 dòng
    def multiRowsEnc(self):
        self.stackedWidget.setCurrentWidget(self.TransMultiRowsEncPage)


    def multiRowsDec(self):
        self.stackedWidget.setCurrentWidget(self.TransMultiRowsDecPage)

    #------------------------------------------------------------------Phương pháp XOR
    # ----------------- Tạo hàm vào trang chọn phương thức mã hóa XOR
    def showXorEncPage(self):
        self.stackedWidget.setCurrentWidget(self.XorEncPage)

    #------------------Tạo hàm chọn phương thức mã hóa với Xor Ceasar
    def xorCeasarEnc(self):
        self.stackedWidget.setCurrentWidget(self.XorCeasarEncPage)

    # ----------------- Tạo hàm vào trang chọn phương thức giải mã XOR
    def showXorDecPage(self):
        self.stackedWidget.setCurrentWidget(self.XorDecPage)
     #------------------Tạo hàm chọn phương thức giải mã với Xor Ceasar
    def xorCeasarDec(self):
        self.stackedWidget.setCurrentWidget(self.XorCeasarDecPage)

    #-------------------- Tạo hàm chọn phương thức mã hóa với phương pháp XOR Vignere
    def xorVignereEnc(self):
        self.stackedWidget.setCurrentWidget(self.XorVignereEncPage)

    #-------------------- Tạo hàm  chọn phương thức giải mã với phương pháp XOR Vignere
    def xorVignereDec(self):
        self.stackedWidget.setCurrentWidget(self.XorVignereDecPage)

    #-------------------- Tạo hàm chọn phương thức mã hóa với phương pháp XOR Belasco
    def xorBelascoEnc(self):
        self.stackedWidget.setCurrentWidget(self.XorBelascoEncPage)

    #-------------------- Tạo hàm  chọn phương thức giải mã với phương pháp XOR Belasco
    def xorBelascoDec(self):
        self.stackedWidget.setCurrentWidget(self.XorBelascoDecPage)



    #-------------------- Tạo hàm  chọn phương thức mã hóa với phương pháp XOR Trithemius
    def xorTrithemiusEnc(self):
        self.stackedWidget.setCurrentWidget(self.XorTrithemiusEncPage)

    #-------------------- Tạo hàm chọn phương thức mã hóa với phương pháp XOR Trithemius
    def xorTrithemiusDec(self):
        self.stackedWidget.setCurrentWidget(self.XorTrithemiusDecPage)


    #------------------------------------------------------------- Tạo hàm chọn phương pháp mã hóa RSA
    def showRSAEncpage(self):
        self.stackedWidget.setCurrentWidget(self.RsaEncPage)
    
    #------------------------------------------------------------- Tạo hàm chọn phương pháp giải mã RSA
    def showRSADecpage(self):
        self.stackedWidget.setCurrentWidget(self.RsaDecPage)

    #------------------------------------------------------------- Tạo hàm chọn phương pháp mã hóa DES
    def showDesEncpage(self):
        self.stackedWidget.setCurrentWidget(self.DesEncPage)

    def showDesDecPage(self):
        self.stackedWidget.setCurrentWidget(self.DesDecPage)

    def showMD5EncPage(self):
        self.stackedWidget.setCurrentWidget(self.MD5EncPage)

    def showSHA256EncPage(self):
        self.stackedWidget.setCurrentWidget(self.SHA_256EncPage)
        
    def showSHA3EncPage(self):
        self.stackedWidget.setCurrentWidget(self.SHA_3EncPage)
    #------------------------------------------------ Caesar Cipher

    #Tạo hàm mã hóa bằng phương pháp thay thế Caesar
    def execEnc3(self):
        self.textk = self.txtKey_3.toPlainText() 
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_3.setFocus()
        else:
            textpl = self.txtPlainText_3.toPlainText()
            if not textpl:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_3.setFocus()
            else:
                cCeasar= CCeasar(textpl,int(self.textk)) 
                c = cCeasar.MaHoa() 
                self.txtCipherText_3.setPlainText(c) 
    def execOpen3(self):
        filePath, _ = QFileDialog.getOpenFileName(self.CaesarEncPage, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_3.setPlainText(fileContent)
    def execSave3(self):
        filePath, _ = QFileDialog.getSaveFileName(self.CaesarEncPage, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.textk)
                file.write('\n')
                file.write(self.txtCipherText_3.toPlainText())

            
    #Tạo hàm giải mã bằng phương pháp thay thế Caesar
    def execDec13(self):
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_13.setFocus()
        else:
            textci = self.txtCipherText_13.toPlainText() 
            if not textci:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_13.setFocus()
            else:
                cCeasar= CCeasar("",int(self.textk),textci)
                s = cCeasar.GiaiMa() 
                print(int(self.textk))
                print(textci)
                self.txtOriText_13.setPlainText(s)
    def execOpen13(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.readline()
                self.txtKey_13.setPlainText(self.textk)
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.txtCipherText_13.setPlainText(s)
                
    def execSave13(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtOriText_13.toPlainText())


    #----------------------------------------------------------------------------- Vignere cipher
    # Mã hóa với Vignere
    def execEnc2(self):
        self.textk = self.txtKey_2.toPlainText() 
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_2.setFocus()
        else:
            textpl = self.txtPlainText_2.toPlainText() 
            if not textpl:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_2.setFocus()
            else:
                cVignere = CVignere(textpl,self.textk)
                c = cVignere.MaHoa()
                self.txtCipherText_2.setPlainText(c)
    def execOpen2(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_2.setPlainText(fileContent)
    def execSave2(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.textk)
                file.write('\n')
                file.write(self.txtCipherText_2.toPlainText())

    # Giải mã với Vignere
    def execDec14(self):
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_14.setFocus()
        else:
            textci = self.txtCipherText_14.toPlainText()
            if not textci:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_14.setFocus()
            else:
                cVignere = CVignere("",self.textk,textci)
                s = cVignere.GiaiMa()
                print(len(self.textk))
                self.txtOriText_14.setPlainText(s)

                
    def execOpen14(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk  = file.readline().rstrip('\n')
                self.txtKey_14.setPlainText(self.textk)
                s = file.read()
                self.txtCipherText_14.setPlainText(s)
                
    def execSave14(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtOriText_14.toPlainText())



    #----------------------------------------------------------------------- Mã hóa với Belasco
    def execEnc4(self):
        self.textk = self.txtKey_4.toPlainText() 
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_4.setFocus()
        else:
            textpl = self.txtPlainText_4.toPlainText()
            if not textpl:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_4.setFocus()
            else:
                cBelasco = CBelasco(textpl,self.textk)
                c = cBelasco.MaHoa()
                print(c)
                self.txtCipherText_4.setPlainText(c)
    def execOpen4(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_4.setPlainText(fileContent)
    def execSave4(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.textk)
                file.write('\n')
                file.write(self.txtCipherText_4.toPlainText())

    # Giải mã với Belasco

    def execDec15(self):
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_15.setFocus()
        else:
            textci = self.txtCipherText_15.toPlainText()
            if not textci:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_15.setFocus()
            else:
                cBelasco = CBelasco("",self.textk,textci)
                s = cBelasco.GiaiMa()
                print(self.textk)
                print(textci)
                self.txtOriText_15.setPlainText(s)

                
    def execOpen15(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk  = file.readline().rstrip('\n')
                self.txtKey_15.setPlainText(self.textk)
                s = file.read()
                self.txtCipherText_15.setPlainText(s)
                
    def execSave15(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtOriText_15.toPlainText())


   #----------------------------------------------------------------------- Mã hóa với Trithemius
    def execEnc5(self):
        textpl = self.txtPlainText_5.toPlainText()
        if not textpl:
            QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.openFile_5.setFocus()
        else:
            cTrithemius = CTrithemius(textpl)
            c = cTrithemius.MaHoa()
            self.txtCipherText_5.setPlainText(c)
    def execOpen5(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_5.setPlainText(fileContent)
    def execSave5(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCipherText_5.toPlainText())

    
    # Giải mã với Trithemius
    def execDec28(self):
        textci = self.txtCipherText_16.toPlainText() 
        if not textci:
            QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.openFile_16.setFocus()
        else:
            cTrithemius = CTrithemius("",textci)
            s = cTrithemius.GiaiMa()
            print(textci)
            self.txtOriText_16.setPlainText(s)

                
    def execOpen28(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s = file.read()
                print("aaaaaaaaaaaaaaa")
                print(s)
                self.txtCipherText_16.setPlainText(s)
                
    def execSave28(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtOriText_16.toPlainText())



    #--------------------------------------------------------------- Phương pháp chuyển vị
    #Mã hóa với chuyển vị hai dòng
    def execEnc6(self):
        textpl = self.txtPlainText_6.toPlainText() 
        if not textpl:
            QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.openFile_6.setFocus()
        else:
            cHaiDong= CChuyenViHaiDong(textpl) #
            self.c = cHaiDong.MaHoa() 
            self.txtCipherText_6.setPlainText(self.c) 
    def execOpen6(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_6.setPlainText(fileContent)
    def execSave6(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.c)

    #Giải mã với chuyển vị hai dòng
    def execDec7(self):
        textci = self.txtCipherText_7.toPlainText() 
        if not textci:
            QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile.setFocus()
        else:
            cHaiDong= CChuyenViHaiDong("",textci) 
            c = cHaiDong.GiaiMa() 
            self.txtOriText_7.setPlainText(c) 
    def execOpen7(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.txtCipherText_7.setPlainText(s)
                
    def execSave7(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtOriText_7.toPlainText())


    #Mã hóa với chuyển vị nhiều dòng
    def execEnc8(self):
        self.textk = self.txtKey_8.toPlainText() 
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_8.setFocus()
        else:
            textpl = self.txtPlainText_8.toPlainText()
            if not textpl:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_8.setFocus()
            else:
                cChuyenViNhieuDong= CChuyenViNhieuDong(textpl) #khai báo đối tượng của lớp CNhieuDong
                n = int(self.textk)
                self.k = cChuyenViNhieuDong.CreateKey(n)
                cChuyenViNhieuDong.SetKey(self.k)
                c = cChuyenViNhieuDong.MaHoa() 
                self.txtCipherText_8.setPlainText(c)
    def execOpen8(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_8.setPlainText(fileContent)
    def execSave8(self):
        # Lưu file dữ liệu đã mã hoá ciphertext
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                s = ''
                for item in self.k:
                    s += str(item) + " "
                s = s.rstrip()  # Loại bỏ dấu cách cuối cùng
                print(s)
                file.write(s)
                file.write('\n')
                file.write(self.txtCipherText_8.toPlainText())
        

    #Giải mã với chuyển vị nhiều dòng
    def execDec9(self):
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_17.setFocus()
        else:
            textci = self.txtCipherText_17.toPlainText() 
            if not textci:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_17.setFocus()
            else:
                cChuyenViNhieuDong= CChuyenViNhieuDong("",None,textci) 
                k = [ int(item) for item in self.textk.split(' ') ]
                cChuyenViNhieuDong.SetKey(k)
                s = cChuyenViNhieuDong.GiaiMa() 
                self.txtOriText_17.setPlainText(s) 

                
    def execOpen9(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk  = file.readline().rstrip('\n')
                self.txtKey_17.setPlainText(self.textk)
                s = file.read()
                self.txtCipherText_17.setPlainText(s)
       
                
                
    def execSave9(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtOriText_17.toPlainText())



    #-------------------------------------- Mã hóa với XOR Ceasar
    def execEnc10(self):
        self.textk = self.txtKey_19.toPlainText() 
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_19.setFocus()
        else:
            textpl = self.txtPlainText_19.toPlainText()
            if not textpl:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_19.setFocus()
            else:
                cXORCeasar= CXORCeasar() 
                c = cXORCeasar.MaHoa(textpl,int(self.textk)) 
                self.txtCipherText_19.setPlainText(c) 

    def execOpen10(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_19.setPlainText(fileContent)
    def execSave10(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.textk)
                file.write('\n')
                file.write(self.txtCipherText_19.toPlainText())


     #-------------------------------------- Giải mã với XOR Ceasar
    def execDec11(self):
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_20.setFocus()
        else:
            textci = self.txtCipherText_20.toPlainText() 
            if not textci:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_20.setFocus()
            else:
                cCeasar= CXORCeasar()
                s = cCeasar.MaHoa(textci,int(self.textk)) 
                self.txtOriText_20.setPlainText(s) 


                
    def execOpen11(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk  = file.readline().rstrip('\n')
                self.txtKey_20.setPlainText(self.textk)
                s = file.read()
                self.txtCipherText_20.setPlainText(s)
       
                
                
    def execSave11(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtOriText_20.toPlainText())


    #----------------------------------------- Mã hóa với XOR Vignere

    def execEnc12(self):
        self.textk = self.txtKey_22.toPlainText() 
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_22.setFocus()
        else:
            textpl = self.txtPlainText_22.toPlainText()
            if not textpl:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_22.setFocus()
            else:
                cXORVignere= CXORVignere() 
                c = cXORVignere.MaHoa(textpl,self.textk)
                self.txtCipherText_22.setPlainText(c) 
    def execOpen12(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_22.setPlainText(fileContent)
    def execSave12(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.textk)
                file.write('\n')
                file.write(self.txtCipherText_22.toPlainText())


    #------------------------------------------- Giải mã với XOR Vignere
    def execDec16(self):
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_23.setFocus()
        else:
            textci = self.txtCipherText_23.toPlainText() 
            if not textci:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_XORVignere_Dec.setFocus()
            else:
                cXORVignere= CXORVignere()
                s = cXORVignere.GiaiMa(textci,self.textk) 
                self.txtOriText_23.setPlainText(s) 


                
    def execOpen16(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk  = file.readline().rstrip('\n')
                self.txtKey_23.setPlainText(self.textk)
                s = file.read()
                self.txtCipherText_23.setPlainText(s)
       
                
                
    def execSave16(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtOriText_23.toPlainText()) 


    #----------------------------------- Mã hóa với Xor Belasco
    def execEnc26(self):
        self.textk = self.txtKey_30.toPlainText() 
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_30.setFocus()
        else:
            textpl = self.txtPlainText_30.toPlainText()
            if not textpl:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_30.setFocus()
            else:
                cXORBelasco= CXORBelasco() 
                c = cXORBelasco.MaHoa(textpl,self.textk)
                self.txtCipherText_30.setPlainText(c) 
    def execOpen26(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_30.setPlainText(fileContent)
    def execSave26(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.textk)
                file.write('\n')
                file.write(self.txtCipherText_30.toPlainText())

    #----------------------------------- giải mã với Xor Belasco
    def execDec27(self):
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_31.setFocus()
        else:
            textci = self.txtCipherText_31.toPlainText() 
            if not textci:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_31.setFocus()
            else:
                cXORBelasco= CXORBelasco()
                s = cXORBelasco.MaHoa(textci,self.textk) 
                self.txtOriText_31.setPlainText(s) 
       
    def execOpen27(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk  = file.readline().rstrip('\n')
                self.txtKey_31.setPlainText(self.textk)
                s = file.read()
                self.txtCipherText_31.setPlainText(s)          
                
    def execSave27(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtOriText_31.toPlainText()) 


    # Mã hóa với Trithemius
    def execEnc17(self):
        textpl = self.txtPlainText_24.toPlainText()
        if not textpl:
            QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.openFile_24.setFocus()
        else:
            cXORTrithemius= CXORTrithemius() 
            c = cXORTrithemius.MaHoa(textpl) 
            self.txtCipherText_24.setPlainText(c) 

    def execOpen17(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_24.setPlainText(fileContent)
    def execSave17(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCipherText_24.toPlainText())


    # Giải mã với XOR Trithemius
    def execDec18(self):
        textci = self.txtCipherText_25.toPlainText() 
        if not textci:
            QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.openFile_XORTrithemius_Dec.setFocus()
        else:
            cXORTrithemius= CXORTrithemius()
            s = cXORTrithemius.MaHoa(textci) 
            self.txtOriText_25.setPlainText(s) 


                
    def execOpen18(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s = file.read()
                self.txtCipherText_25.setPlainText(s)
       
                
                
    def execSave18(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtOriText_25.toPlainText())


    # Mã hóa với RSA
    def execEnc19(self):
        e=65537; n=4255903; d=2480777
        textpl = self.txtPlainText_11.toPlainText()
        if not textpl:
            QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.openFile_11.setFocus()
        else:
            cRSA= CRSA() 
            c = cRSA.MaHoa(textpl,e,n) 
            self.var = c
            self.txtCipherText_11.setPlainText(str(c)) 

    def execOpen19(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_11.setPlainText(fileContent)
    def execSave19(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCipherText_11.toPlainText())


    # Giải mã với RSA
    def execDec20(self):
        e=65537; n=4255903; d=2480777
        textci = self.txtCipherText_18.toPlainText() 
        if not textci:
            QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.openFile_18.setFocus()
        else:
            cRSA= CRSA()
            string = textci
            integer_list = [int(item) for item in string.strip('[]').split(', ')]
            s = cRSA.GiaiMa(integer_list,d,n) 
            self.txtOriText_18.setPlainText(s) 

    def execOpen20(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s = file.read()
                self.txtCipherText_18.setPlainText(s)
                
    def execSave20(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtOriText_20.toPlainText())    


    #mã hóa với DESSSSS
    def execEnc21(self):
        self.textk = self.txtKey_10.toPlainText() 
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_10.setFocus()
        else:
            textpl = self.txtPlainText_10.toPlainText()
            if not textpl:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_10.setFocus()
            else:
                self.c = mahoaSDES.MaHoa(textpl,self.textk) 
                self.txtCipherText_10.setPlainText(self.c) 
    def execOpen21(self):
        filePath, _ = QFileDialog.getOpenFileName(self.CaesarEncPage, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_10.setPlainText(fileContent)
    def execSave21(self):
        filePath, _ = QFileDialog.getSaveFileName(self.CaesarEncPage, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.textk)
                file.write('\n')
                file.write(self.txtCipherText_10.toPlainText())

    # giải mã với DES
    def execDec22(self):
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey_26.setFocus()
        else:
            textci = self.txtCipherText_26.toPlainText() 
            if not textci:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.openFile_26.setFocus()
            else:
                
                self.s = mahoaSDES.GiaiMa(textci,self.textk) 
                self.txtOriText_26.setPlainText(self.s) 


                
    def execOpen22(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk  = file.readline().rstrip('\n')
                self.txtKey_26.setPlainText(self.textk)
                s = file.read()
                self.txtCipherText_26.setPlainText(s)
       
                
                
    def execSave22(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtOriText_26.toPlainText())


    #----------- Mã hóa với MD5
    def execEnc23(self):
        textpl = self.txtPlainText_27.toPlainText()
        if not textpl:
            QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.openFile_27.setFocus()
        else:
            c = mahoamd5.MaHoaMD5(textpl) 
            self.txtCipherText_27.setPlainText(c)  

    def execOpen23(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_27.setPlainText(fileContent)
    def execSave23(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCipherText_27.toPlainText())

    #----------- Mã hóa với SHA-256
    def execEnc24(self):
        textpl = self.txtPlainText_28.toPlainText()
        if not textpl:
            QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.openFile_28.setFocus()
        else:
            c = mahoasha256.MaHoaSha256(textpl) 
            self.txtCipherText_28.setPlainText(c) 

    def execOpen24(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_28.setPlainText(fileContent)
    def execSave24(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCipherText_28.toPlainText())    

   

    #------------------ mã hóa với SHA-3
    def execEnc25(self):
        textpl = self.txtPlainText_29.toPlainText()
        if not textpl:
            QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.openFile_29.setFocus()
        else:
            c = mahoasha3.MaHoaSha3(textpl) 
            self.txtCipherText_29.setPlainText(c) 

    def execOpen25(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")                                                 
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlainText_29.setPlainText(fileContent)
    def execSave25(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCipherText_29.toPlainText())



    #---------------------------------------------------------- Thông báo chưa chọn phương pháp mã hóa hoặc giải mã
    def notify(self):
        QMessageBox.information(self,"Thông báo", "Bạn chưa chọn phương pháp mã hóa")

    def notify1(self):
        QMessageBox.information(self,"Thông báo", "Bạn chưa chọn phương pháp giải mã")

    #------------------------------------------------------------------------- Main
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())