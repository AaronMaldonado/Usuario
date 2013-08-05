# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui

class Ui_Ventana(object):


    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(700, 450)
        
        #crear tabla usuarios
        self.table_usuarios= QtGui.QTableView(Window)
        self.table_usuarios.setGeometry(QtCore.QRect(20,80,650,360))
        self.table_usuarios.setObjectName("table_usuarios")
        self.table_usuarios.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_usuarios.setAlternatingRowColors(True)
        self.table_usuarios.setSortingEnabled(True)       
	    #eliminar
        self.btn_search = QtGui.QPushButton(Window)
        self.btn_search.setGeometry(QtCore.QRect(575, 15, 120, 27))
        self.btn_search.setObjectName("btn_search")
	    #editar
        self.btn_search2 = QtGui.QPushButton(Window)
        self.btn_search2.setGeometry(QtCore.QRect(463, 15, 110, 27))
        self.btn_search2.setObjectName("btn_search2")
        #nuevo Usuario
        self.btn_search3 = QtGui.QPushButton(Window)
        self.btn_search3.setGeometry(QtCore.QRect(340, 15, 120, 27))
        self.btn_search3.setObjectName("btn_search3")
		#Busqueda Instantanea
        self.search_box = QtGui.QLineEdit(Window)
        self.search_box.setGeometry(QtCore.QRect(20, 18, 300, 25))
        self.search_box.setObjectName("search_box")
        #Nuevo Grupo
        self.btn_search4 = QtGui.QPushButton(Window)
        self.btn_search4.setGeometry(QtCore.QRect(340, 45, 120, 27))
        self.btn_search4.setObjectName("btn_search3")
        #Editar Grupo
        self.btn_search5 = QtGui.QPushButton(Window)
        self.btn_search5.setGeometry(QtCore.QRect(463, 45, 110, 27))
        self.btn_search5.setObjectName("btn_search3")
        #Eliminar Grupo
        self.btn_search6 = QtGui.QPushButton(Window)
        self.btn_search6.setGeometry(QtCore.QRect(575, 45, 120, 27))
        self.btn_search6.setObjectName("btn_search3")
         #eliminar
        self.btn_search7 = QtGui.QPushButton(Window)
        self.btn_search7.setGeometry(QtCore.QRect(20, 45, 120, 27))
        self.btn_search7.setObjectName("btn_search")
        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)
        
        
    def retranslateUi(self, Window):
        Window.setWindowTitle(QtGui.QApplication.translate("Window", "Usuarios", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_search.setText(QtGui.QApplication.translate("Window","Eliminar Usuarios", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_search2.setText(QtGui.QApplication.translate("Window", "Editar Usuarios", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_search3.setText(QtGui.QApplication.translate("Window", "Nuevo Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_search4.setText(QtGui.QApplication.translate("Window", "Nuevo Grupo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_search5.setText(QtGui.QApplication.translate("Window", "Editar Grupos", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_search6.setText(QtGui.QApplication.translate("Window", "Eliminar Grupos", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_search7.setText(QtGui.QApplication.translate("Window", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.search_box.setPlaceholderText(QtGui.QApplication.translate("Window", "Busque aquí", None, QtGui.QApplication.UnicodeUTF8))
