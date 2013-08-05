# -*- coding: utf-8 -*-

   
from PySide import QtCore, QtGui

class Ui_Ventana_Eliminar_Grupo(object):
	
    def setupUi(self,Window):
	Window.setObjectName("Window")
	Window.resize(310,350)
		        
        #crear tabla grupos
        self.table_grupos= QtGui.QTableView(Window)
        self.table_grupos.setGeometry(QtCore.QRect(20,60,150,250))
        self.table_grupos.setObjectName("table_usuarios")
        self.table_grupos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_grupos.setAlternatingRowColors(True)
        self.table_grupos.setSortingEnabled(True) 
        #Boton Eliminar
	self.button1= QtGui.QPushButton(Window)
	self.button1.setGeometry(QtCore.QRect(200,70,70,50))
	self.button1.setObjectName("button1")
	#Boton Salir
	self.button2= QtGui.QPushButton(Window)
	self.button2.setGeometry(QtCore.QRect(200,150,70,50))
	self.button2.setObjectName("button2")
	self.label = QtGui.QLabel(Window)
	self.label.setGeometry(QtCore.QRect(10,5,300, 35))
	self.label.setObjectName("label")
	self.label2 = QtGui.QLabel(Window)
	self.label2.setGeometry(QtCore.QRect(10,30,300, 35))
	self.label2.setObjectName("label")
	self.retranslateUi(Window)
	QtCore.QMetaObject.connectSlotsByName(Window)
	    	

    def retranslateUi(self, Window):
	Window.setWindowTitle(QtGui.QApplication.translate("Window", "Eliminar Grupo", None, QtGui.QApplication.UnicodeUTF8))
	self.button1.setText(QtGui.QApplication.translate("Window", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
	self.button2.setText(QtGui.QApplication.translate("Window", "Salir", None, QtGui.QApplication.UnicodeUTF8))
	self.label.setText(QtGui.QApplication.translate("Window", "ADVERTENCIA: Si elimina un grupo se", None, QtGui.QApplication.UnicodeUTF8))
	self.label2.setText(QtGui.QApplication.translate("Window", "eliminan TODOS los usuarios de ese grupo", None, QtGui.QApplication.UnicodeUTF8))

