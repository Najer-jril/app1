import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from qfluentwidgets import *
from qframelesswindow import FramelessWindow
from PyQt5.QtWidgets import QMessageBox
import validasi
import tesdb

class Window(FramelessWindow):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main.ui", self)
        self.titleBar.raise_()
        self.logo.setPixmap(QPixmap("logo OS.png").scaled(250, 250))
        self.btn_login.clicked.connect(self.login)
        self.PushButton_2.clicked.connect(lambda: self.searchdata("guest"))
        self.PushButton_4.clicked.connect(lambda: self.searchdata("admin"))
        self.stackedWidget.setCurrentIndex(0)
        self.btn_guest.clicked.connect(self.loginguest)
        self.btn_logout.clicked.connect(self.logout)
        self.btn_logout2.clicked.connect(self.logout)
        self.btn_logout3.clicked.connect(self.logout)
        self.ComboBox.addItem("Meninggalkan materi saat sesi materi berlangsung dengan durasi yang sangat lama, secara berulang tanpa adanya keterangan yang jelas serta tidak mendapatkan izin dari LO (Sedang)", "5")
        self.ComboBox.addItem("tes1 -5", "5")
        self.ComboBox.addItem("tes2 -15", "152366")
        # self.ComboBox.adjustSize()
        # def combo
    
        

    # def updateskor(self):
        # print(skor)


    def login(self):
        username = self.ledit_username.text()
        password =self.ledit_pw.text()
        try:
            user_data = validasi.login(username, password)
            if user_data["role"] == "user":
                self.stackedWidget.setCurrentIndex(2)
                self.userpage.setProperty("user_data", user_data)
                print(self.userpage.property("user_data"))
            elif user_data["role"] == "admin":
                self.stackedWidget.setCurrentIndex(3)
        except:
            # print("failed")
            msg = QMessageBox()
            msg.setText("username atau password salah")
            msg.setWindowTitle("salah oi")
            msg.exec_()
            

    def loginguest(self):
        self.stackedWidget.setCurrentIndex(1)
    

    def searchdata(self, role):
        if role == "admin":
            nim = self.Ledit_NIM.text()
            data = tesdb.get_data_by_nim(nim)
            if data:
                self.nama_a.setText(data["nama"])
                self.nim_a.setText(data["NIM"])
                self.prodi_a.setText(data["prodi"])
                self.skor_a.setText(str(data["skor"]))
            else:
                print("failed")
        elif role == "guest":
            nim = self.Ledit_NIM_g.text()
            data = tesdb.get_data_by_nim(nim)
            if data:
                self.nama_g.setText(data["nama"])
                self.nim_g.setText(data["NIM"])
                self.prodi_g.setText(data["prodi"])
                self.skor_g.setText(str(data["skor"]))
            else:
                print("failed")

    def logout(self):
        self.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
