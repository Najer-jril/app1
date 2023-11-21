# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
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
        self.setFixedSize(1333, 650)
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
        self.tableWidget.setColumnWidth(0, 540)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 355)
        self.tableWidget.setColumnWidth(3, 100)
        self.tabledata()
        
    def tabledata(self):
        file = open("db.json", "r")
        data = json.load(file)
        row = 0
        c = 0
        for a in range(1,23):
            if a < 10:
                b = len(data["0" + str(a)])
                c += b
            else:
                b = len(data[str(a)])
                c += b
        self.tableWidget.setRowCount(c)
        for i in range(1,23):
            if i < 10:
                for j in data["0" + str(i)]:
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(j["nama"]))
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(j["NIM"]))
                    self.tableWidget.setItem(row, 2, QTableWidgetItem(j["prodi"]))
                    self.tableWidget.setItem(row, 3, QTableWidgetItem(str(j["skor"])))
                    row += 1
            else:
                for j in data[str(i)]:
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(j['nama']))
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(j["NIM"]))
                    self.tableWidget.setItem(row, 2, QTableWidgetItem(j['prodi']))
                    self.tableWidget.setItem(row, 3, QTableWidgetItem(str(j['skor'])))
                    row += 1

    def login(self):
        username = self.ledit_username.text()
        password =self.ledit_pw.text()
        try:
            user_data = validasi.login(username, password)
            if user_data["role"] == "user":
                self.stackedWidget.setCurrentIndex(2)
                self.userpage.setProperty("user_data", user_data)
                print(self.userpage.property("user_data"))
                self.user_nama.setText(str(user_data["nama"]))
                self.user_nim.setText(str(user_data["NIM"]))
                self.user_skor.setText(str(user_data[str("skor")]))
                self.user_prodi.setText(str(user_data["prodi"]))
            elif user_data["role"] == "admin":
                self.stackedWidget.setCurrentIndex(3)
        except:
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
