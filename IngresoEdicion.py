# -*- coding: utf-8 -*-

   
from PySide import QtCore, QtGui

class Ui_Ventana_editar(object):
	
    def setupUi(self,Window):
	Window.setObjectName("Window")
	Window.resize(390,500)
	#Boton Editar
	self.button1= QtGui.QPushButton(Window)
	self.button1.setGeometry(QtCore.QRect(100,400,70,50))
	self.button1.setObjectName("button1")
	#Boton Salir
	self.button2= QtGui.QPushButton(Window)
	self.button2.setGeometry(QtCore.QRect(210,400,70,50))
	self.button2.setObjectName("button2")
	#Username
	self.search_box1 = QtGui.QLineEdit(Window)
	self.search_box1.setGeometry(QtCore.QRect(130,60,230,25))
	self.search_box1.setObjectName("search_box1")
	self.label1 = QtGui.QLabel(Window)
	self.label1.setGeometry(QtCore.QRect(38,50,90,35))
	self.label1.setObjectName("label")
	#Password
	self.search_box2 = QtGui.QLineEdit(Window)
	self.search_box2.setGeometry(QtCore.QRect(130,100,230, 25))
	self.search_box2.setObjectName("search_box2")
	self.search_box2.setEchoMode(QtGui.QLineEdit.Password)
	self.label2 = QtGui.QLabel(Window)
	self.label2.setGeometry(QtCore.QRect(38,90,80, 35))
	self.label2.setObjectName("label")
	#Repita Password
	self.search_box3 = QtGui.QLineEdit(Window)
	self.search_box3.setGeometry(QtCore.QRect(170,140,190, 25))
	self.search_box3.setObjectName("search_box3")
	self.search_box3.setEchoMode(QtGui.QLineEdit.Password)
	self.label3 = QtGui.QLabel(Window)
	self.label3.setGeometry(QtCore.QRect(38,130,120, 35))
	self.label3.setObjectName("label")
	#Nombres
	self.search_box4 = QtGui.QLineEdit(Window)
	self.search_box4.setGeometry(QtCore.QRect(130,180,230, 25))
	self.search_box4.setObjectName("search_box4")
	self.label4 = QtGui.QLabel(Window)
	self.label4.setGeometry(QtCore.QRect(38,170,80, 35))
	self.label4.setObjectName("label")
	#apellidos
	self.search_box5 = QtGui.QLineEdit(Window)
	self.search_box5.setGeometry(QtCore.QRect(130,220,230, 25))
	self.search_box5.setObjectName("search_box5")
	self.label5 = QtGui.QLabel(Window)
	self.label5.setGeometry(QtCore.QRect(38,210,80, 35))
	self.label5.setObjectName("label")
	#Email
	self.search_box6 = QtGui.QLineEdit(Window)
	self.search_box6.setGeometry(QtCore.QRect(130,260,230, 25))
	self.search_box6.setObjectName("search_box6")
	self.label6 = QtGui.QLabel(Window)
	self.label6.setGeometry(QtCore.QRect(38,250,120, 35))
	self.label6.setObjectName("label")
	#Fecha Nacimiento
	self.search_box7 = QtGui.QLineEdit(Window)
	self.search_box7.setGeometry(QtCore.QRect(170,300,190, 25))
	self.search_box7.setObjectName("search_box6")
	self.label7 = QtGui.QLabel(Window)
	self.label7.setGeometry(QtCore.QRect(38,290,120, 35))
        self.label7.setObjectName("label")
	#Grupos
	self.combo_grupos = QtGui.QComboBox(Window)
	self.combo_grupos.setGeometry(QtCore.QRect(190, 20, 101, 25))
	self.combo_grupos.setObjectName("combo_grupos")
	self.label = QtGui.QLabel(Window)
	self.label.setGeometry(QtCore.QRect(38, 25, 150, 16))
	self.label.setObjectName("label")
	self.retranslateUi(Window)
	QtCore.QMetaObject.connectSlotsByName(Window)
	    
	   
    def retranslateUi(self, Window):
	Window.setWindowTitle(QtGui.QApplication.translate("Window", "Formulario Edición Usuarios", None, QtGui.QApplication.UnicodeUTF8))
	self.button1.setText(QtGui.QApplication.translate("Window", "Editar", None, QtGui.QApplication.UnicodeUTF8))
	self.button2.setText(QtGui.QApplication.translate("Window", "Salir", None, QtGui.QApplication.UnicodeUTF8))
	self.label1.setText(QtGui.QApplication.translate("Window", "Username  :", None, QtGui.QApplication.UnicodeUTF8))
	self.label2.setText(QtGui.QApplication.translate("Window", "Password  :", None, QtGui.QApplication.UnicodeUTF8))
	self.label3.setText(QtGui.QApplication.translate("Window", "Repita Password:", None, QtGui.QApplication.UnicodeUTF8))
	self.label4.setText(QtGui.QApplication.translate("Window", "Nombres:", None, QtGui.QApplication.UnicodeUTF8))
	self.label5.setText(QtGui.QApplication.translate("Window", "Apellidos:", None, QtGui.QApplication.UnicodeUTF8))
	self.label6.setText(QtGui.QApplication.translate("Window", "Email:", None, QtGui.QApplication.UnicodeUTF8))
	self.label7.setText(QtGui.QApplication.translate("Window", "Fecha Nacimiento:", None, QtGui.QApplication.UnicodeUTF8))
	self.label.setText(QtGui.QApplication.translate("ProductosWindow", "Seleccione un grupo", None, QtGui.QApplication.UnicodeUTF8))
