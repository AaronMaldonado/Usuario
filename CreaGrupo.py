# -*- coding: utf-8 -*-

   
from PySide import QtCore, QtGui

class Ui_Ventana_grupo(object):
	
    def setupUi(self,Window):
	Window.setObjectName("Window")
	Window.resize(300,150)
	#Boton Agregar
	self.button1= QtGui.QPushButton(Window)
	self.button1.setGeometry(QtCore.QRect(80,70,70,50))
	self.button1.setObjectName("button1")
	#Boton Salir
	self.button2= QtGui.QPushButton(Window)
	self.button2.setGeometry(QtCore.QRect(160,70,70,50))
	self.button2.setObjectName("button2")
	self.search_box = QtGui.QLineEdit(Window)
	self.search_box.setGeometry(QtCore.QRect(120,20,150, 25))
	self.search_box.setObjectName("search_box6")
	self.label = QtGui.QLabel(Window)
	self.label.setGeometry(QtCore.QRect(10,15,120, 35))
	self.label.setObjectName("label")
	
	self.retranslateUi(Window)
	QtCore.QMetaObject.connectSlotsByName(Window)
	    	

    def retranslateUi(self, Window):
	Window.setWindowTitle(QtGui.QApplication.translate("Window", "Formulario Creación Grupos", None, QtGui.QApplication.UnicodeUTF8))
	self.button1.setText(QtGui.QApplication.translate("Window", "Crear", None, QtGui.QApplication.UnicodeUTF8))
	self.button2.setText(QtGui.QApplication.translate("Window", "Salir", None, QtGui.QApplication.UnicodeUTF8))
	self.label.setText(QtGui.QApplication.translate("Window", "Nombre Grupo :", None, QtGui.QApplication.UnicodeUTF8))
