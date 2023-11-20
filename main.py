import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from qfluentwidgets import *
from qframelesswindow import FramelessWindow
from PyQt5.QtWidgets import QMessageBox
import validasi
import tesdb
import cb

class Window(FramelessWindow):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main.ui", self)
        self.titleBar.raise_()
        self.setGeometry(20,30, 1333, 650)
        # self.setFixedHeight(650)
        # self.setFixedWidth(1333)
        self.logo.setPixmap(QPixmap("logo OS.png").scaled(250, 250))
        self.btn_login.clicked.connect(self.login)
        self.PushButton_2.clicked.connect(lambda: self.searchdata("guest"))
        self.PushButton_4.clicked.connect(lambda: self.searchdata("admin"))
        self.stackedWidget.setCurrentIndex(3)
        self.btn_guest.clicked.connect(self.loginguest)
        self.btn_logout.clicked.connect(self.logout)
        self.btn_logout2.clicked.connect(self.logout)
        self.btn_logout3.clicked.connect(self.logout)
        self.combobox()
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
    
    # def UserPage(self):
    #     self.stackedWidget.setCurrentIndex(2)
    #     nim = self.Ledit_NIM_g.text()
    #     data = tesdb.get_data_by_nim(nim)
    #     if data:
    #         self.nama_g.setText(data["nama"])
    #         self.nim_g.setText(data["NIM"])
    #         self.prodi_g.setText(data["prodi"])
    #         self.skor_g.setText(str(data["skor"]))


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

    def combobox(self):
        rules = cb.load_rules()
        self.ComboBox.addItem("pilih kesalahan")
        for rule in rules:
            self.ComboBox.addItem(rule["kesalahan"])

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
