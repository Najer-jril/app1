import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from qfluentwidgets import *
from qframelesswindow import FramelessWindow
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



    def login(self):
        username = self.ledit_username.text()
        password =self.ledit_pw.text()
        user_data = validasi.login(username, password)
        if user_data["role"] == "user":
            self.stackedWidget.setCurrentIndex(2)
            self.userpage.setProperty("user_data", user_data)
            print(self.userpage.property("user_data"))
        elif user_data["role"] == "admin":
            self.stackedWidget.setCurrentIndex(3)
        else:
            print("failed")


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
