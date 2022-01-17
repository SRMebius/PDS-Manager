#!/usr/bin/env python
#coding:utf-8
# =============================================================================
# Created on 2020/4/15/7:36:56 PM
# @ author SRMebius
# =============================================================================

import pickle, wmi, base64

from PySide2.QtWidgets import QApplication, QTableWidgetItem, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt

import resource

class Interface:
    
    def __init__(self):
        self.ui = QUiLoader().load('UIs/tablewindow.ui')
        self.set_connect()
        self.__import()
        self.ui.show()
        
    def set_connect(self):
        self.ui.button_1.clicked.connect(self.add)
        self.ui.button_2.clicked.connect(self.delete)
        self.ui.button_3.clicked.connect(self.search)
        self.ui.button_4.clicked.connect(self.save)
        self.ui.button_5.clicked.connect(app.quit)
    
    def __import(self):
        with open('pds.pkl', 'rb') as f:
            self.__data = pickle.load(f)
        
        for k, v in self.__data.items():
            nrow = self.ui.table.rowCount()
            self.ui.table.insertRow(nrow)
            self.ui.table.setItem(nrow, 0, QTableWidgetItem(k))
            self.ui.table.setItem(nrow, 1, QTableWidgetItem(v[0]))
            self.ui.table.setItem(nrow, 2, QTableWidgetItem(v[1]))
    
    def add(self):
        nrow = self.ui.table.rowCount()
        self.ui.table.insertRow(nrow)
        self.ui.table.selectRow(nrow)

    def delete(self):
        row = self.ui.table.currentRow()
        self.ui.table.removeRow(row)        
        
    def search(self):
        keyword = self.ui.lineEdit.text()
        if keyword != '':
            result = ''
            for k in list(self.__data.keys()):
                if keyword in k:
                    result += f'\nRow.{list(self.__data.keys()).index(k)+1}  {k}  {self.__data[k][0]}  {self.__data[k][1]}\n'
            
            if result != '':
                QMessageBox.about(self.ui, 'Results', result)
            else:
                QMessageBox.about(self.ui, 'Results', '\t\t\n   None!\n\t\t')
    
    def save(self):
        nrow = self.ui.table.rowCount()
        self.__data = {self.ui.table.item(i, 0).text() : \
                [self.ui.table.item(i, 1).text(), self.ui.table.item(i, 2).text()] \
                 for i in range(nrow)}
        with open('pds.pkl', 'wb') as f:
            pickle.dump(self.__data, f)
        
        QMessageBox.about(self.ui,
                          'Message',
                          "\t\t\n    Saved!\n\t\t")


class Login():
    
    with open('pds.pkl', 'rb') as f:
        __data = pickle.load(f)
    try:
        __username, __password  = __data['PDS Manager'][0], __data['PDS Manager'][1]
    except Exception:
        __username, __password = '', ''

    def __init__(self):
        self.ui = QUiLoader().load('UIs/login.ui')
        
        self.ui.button_1.clicked.connect(self.call_interface)
        self.ui.button_2.clicked.connect(app.quit)
        self.ui.show()
        
    def call_interface(self):
        username = self.ui.lineEdit_1.text()
        password = self.ui.lineEdit_2.text()
        if username == Login.__username and password == Login.__password:
            self.ui.close()
            self.interface = Interface()


class Signin:
    
    def __init__(self):
        self.__serial_number = wmi.WMI().Win32_Processor()[0].ProcessorId.strip()
        self.ascii()
        self.vertify()

    def ascii(self):
        self.ascii_serial_number = [str(ord(i)) for i in self.__serial_number]
        for i in range(5, len(self.ascii_serial_number), 5):
            self.ascii_serial_number.insert(i, '-')
        self.ascii_serial_number = ''.join(self.ascii_serial_number)
    
    def vertify(self):
        with open('reg.dll', 'r') as f:
            self.str = f.read()
        
        if self.__serial_number == base64.b64decode(self.str).decode():
            self.login = Login()
        else:
            self.signin_ui()
        
    def signin_ui(self):
        self.ui = QUiLoader().load('UIs/Signin.ui')
        
        self.ui.label_2.setText(self.ascii_serial_number)
        self.ui.label_2.setTextInteractionFlags(self.ui.label_2.textInteractionFlags() \
                                                | Qt.TextSelectableByMouse)
        
        self.ui.button_1.clicked.connect(self.savecode)
        self.ui.button_2.clicked.connect(app.quit)
        self.ui.show()
    
    def savecode(self):
        self.code = self.ui.lineEdit.text()
        try:
            self.decode = base64.b64decode(self.code).decode()
        except Exception:
            self.decode = ''
        
        if self.__serial_number == self.decode:
            with open('reg.dll', 'w') as f:
                f.write(self.code)
                
            QMessageBox.about(self.ui,
                              'Message',
                              '\nSIGN UP SUCCEEDED, WELLCOME!')
            self.ui.close()
            self.login = Login()
        else:
            QMessageBox.about(self.ui,
                              'Message',
                              '\nInvalid Code!')


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('logo.png'))
    signin = Signin()
    app.exec_()