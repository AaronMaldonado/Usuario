# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui

class Ui_Ventana(object):


    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(700, 450)
        
        #crear tabla usuarios
        self.table_usuarios= QtGui.QTableView(Window)
        self.table_usuarios.setGeometry(QtCore.QRect(20,65,650,360))
        self.table_usuarios.setObjectName("table_usuarios")
        self.table_usuarios.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_usuarios.setAlternatingRowColors(True)
        self.table_usuarios.setSortingEnabled(True)
        
	#eliminar
        self.btn_search = QtGui.QPushButton(Window)
        self.btn_search.setGeometry(QtCore.QRect(585, 15, 87, 27))
        self.btn_search.setObjectName("btn_search")
	#editar
	self.btn_search2 = QtGui.QPushButton(Window)
	self.btn_search2.setGeometry(QtCore.QRect(495, 15, 87, 27))
	self.btn_search2.setObjectName("btn_search2")
        
        #nuevo producto
        self.btn_search3 = QtGui.QPushButton(Window)
	self.btn_search3.setGeometry(QtCore.QRect(370, 15, 120, 27))
	self.btn_search3.setObjectName("btn_search3")
	
	self.search_box = QtGui.QLineEdit(Window)
        self.search_box.setGeometry(QtCore.QRect(20, 18, 300, 25))
        self.search_box.setObjectName("search_box")
        
        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)
        
        
    def retranslateUi(self, Window):
        Window.setWindowTitle(QtGui.QApplication.translate("Window", "Usuarios", None, QtGui.QApplication.UnicodeUTF8))
	self.btn_search.setText(QtGui.QApplication.translate("Window","Eliminar", None, QtGui.QApplication.UnicodeUTF8))
	self.btn_search2.setText(QtGui.QApplication.translate("Window", "Editar", None, QtGui.QApplication.UnicodeUTF8))
	self.btn_search3.setText(QtGui.QApplication.translate("Window", "Nuevo Usuario", None, QtGui.QApplication.UnicodeUTF8))
	self.search_box.setPlaceholderText(QtGui.QApplication.translate("Window", "Busque aquí", None, QtGui.QApplication.UnicodeUTF8))
