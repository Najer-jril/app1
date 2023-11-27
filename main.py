# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.uic import loadUi
from qfluentwidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import validasi
import tesdb
import cb

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main.ui", self)
        # self.titleBar.raise_()
        self.setGeometry(20,50, 1333, 650)
        self.setFixedSize(1333, 650)
        self.setWindowTitle("OFFSCORE")
        self.setWindowIcon(QtGui.QIcon('OFFSCORE_LOGO.png'))

        # self.labelbackground = BodyLabel(self)
        # self.labelbackground.
        self.setFixedSize(1333, 650)
        self.bg.setPixmap(QPixmap("LOGIN.png"))

        self.setFixedSize(1333, 650)
        self.Gu.setPixmap(QPixmap("G.png"))
        self.ava.setPixmap(QPixmap("ava.png"))

        self.setFixedSize(1333, 650)
        self.admbg.setPixmap(QPixmap("G.png"))

        self.setFixedSize(1333, 650)
        self.usrbg.setPixmap(QPixmap("G.png"))

        self.btn_login.clicked.connect(self.login)
        self.PushButton_2.clicked.connect(lambda: self.searchdata("guest"))
        self.PushButton_4.clicked.connect(lambda: self.searchdata("admin"))
        self.PushButton_12.clicked.connect(lambda: self.searchtable())
        # self.PushButton_4.clicked.connect(lambda: self.skoring())
        self.stackedWidget.setCurrentIndex(3)
        self.btn_guest.clicked.connect(self.loginguest)
        self.btn_logout.clicked.connect(self.logout)
        self.btn_logout2.clicked.connect(self.logout)
        self.btn_logout3.clicked.connect(self.logout)
        self.tableWidget.setColumnWidth(0, 540)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 355)
        self.tableWidget.setColumnWidth(3, 100)
        self.tabledata()
        self.combobox()
        self.update_skor.clicked.connect(lambda: self.skoring(self.ComboBox.currentText()))
        
    def tabledata(self):
        self.tableWidget.setSortingEnabled(False)
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
                    item = QTableWidgetItem()
                    item.setData(Qt.EditRole, int(j["skor"]))
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(j["nama"]))
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(j["NIM"]))
                    self.tableWidget.setItem(row, 2, QTableWidgetItem(j["prodi"]))
                    self.tableWidget.setItem(row, 3, item)
                    row += 1
            else:
                for j in data[str(i)]:
                    item = QTableWidgetItem()
                    item.setData(Qt.EditRole, int(j["skor"]))
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(j['nama']))
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(j["NIM"]))
                    self.tableWidget.setItem(row, 2, QTableWidgetItem(j['prodi']))
                    self.tableWidget.setItem(row, 3, item)
                    row += 1
            # self.tableWidget.sortItems(3, QtCore.Qt.AscendingOrder)
        self.tableWidget.setSortingEnabled(True)
        

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
            msg.setWindowTitle("Ooops...")
            msg.exec_()
            
    def loginguest(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def searchdata(self, role):
        try:
            if role == "admin":
                nim = self.Ledit_NIM.text()
                data = tesdb.get_data_by_nim(nim)        
                if data:
                        self.nama_a.setText(data["nama"])
                        self.nim_a.setText(data["NIM"])
                        self.prodi_a.setText(data["prodi"])
                        self.skor_a.setText(str(data["skor"]))
                else:
                    msg = QMessageBox()
                    msg.setText("NIM tidak terdaftar")
                    msg.setWindowTitle("Ooops...")
                    msg.exec_()
           

            elif role == "guest":
                    nim = self.Ledit_NIM_g.text()
                    data = tesdb.get_data_by_nim(nim)
                    if data:
                        self.nama_g.setText(data["nama"])
                        self.nim_g.setText(data["NIM"])
                        self.prodi_g.setText(data["prodi"])
                    else:
                        msg = QMessageBox()
                        msg.setText("NIM tidak terdaftar")
                        msg.setWindowTitle("Ooops...")
                        msg.exec_()
            
            elif role == "user":
                    nim = self.leditSearchNIM_6.text()
                    data = tesdb.get_data_by_nim(nim)
                    if data:
                        self.nama_g.setText(data["nama"])
                        self.nim_g.setText(data["NIM"])
                        self.prodi_g.setText(data["prodi"])
                        self.skor_g.setText(str(data["skor"]))  
                    else:
                        msg = QMessageBox()
                        msg.setText("NIM tidak terdaftar")
                        msg.setWindowTitle("Ooops...")
                        msg.exec_()
        except IndexError:
                        msg = QMessageBox()
                        msg.setText("Masukkan NIM")
                        msg.setWindowTitle("Ooops...")
                        msg.exec_()
    
    def searchtable(self):
        s = self.leditSearchNIM_6.text()
        data = tesdb.get_data_by_nim(s)
        items = self.tableWidget.findItems(data["nama"], Qt.MatchContains)
        try:
            if items:  # we have found something
                item = items[0]  # take the first
                self.tableWidget.setCurrentItem(item)
        except:
             print("gagal")
   
    def logout(self):
        self.stackedWidget.setCurrentIndex(0)

    def combobox(self):
        rules = cb.load_rules()
        for rule in rules:
            self.ComboBox.addItem(rule["kesalahan"])

    def skoring(self, selected):
        file2 = open("rule1.json", "r")
        data2 = json.load(file2)
        file = open("db.json", "r")
        data = json.load(file)
        nim = self.Ledit_NIM.text()

        try:
            prodi = nim[0] + nim[1]
            for i in data[prodi]:
                 if i["NIM"] == nim:
                    data_m = dict(i)
                    print (data_m)

            rules = data2["rule"]

            msg = QMessageBox()
            msg.setText("APAKAH")
            msg.setWindowTitle("wett")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msg.exec()

            if returnValue == QMessageBox.Ok:
                 
                for j in rules:
                    if selected == j["kesalahan"]:
                        print (j)
                        poin = 0
                        poin += int(j['poin'])
                skor1 = data_m["skor"]
                skor_up = skor1 - poin
                print(skor_up)

                for mhs in data[prodi]:
                    if mhs["NIM"] == nim:
                        mhs["skor"] = skor_up

            with open('db.json', 'w') as file:
                json.dump(data, file, indent=4)

                

            
        except IndexError:
                        msg = QMessageBox()
                        msg.setText("Masukkan NIM yang akan diubah terlebih dahulu")
                        msg.setWindowTitle("Ooops...")
                        msg.exec_()
                            
        file.close()
        file2.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
