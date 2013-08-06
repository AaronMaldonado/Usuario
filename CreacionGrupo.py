#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import controller
from PySide import QtGui, QtCore
from CreaGrupo import Ui_Ventana_grupo

class Ventana_grupos(QtGui.QDialog):
	
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui=Ui_Ventana_grupo()
        self.ui.setupUi(self)
        self.show()
        self.set_listeners()
		
		
    def agregar_grupo(self):#agrega usuarios a la grilla
        nombre = self.ui.search_box.text()
        if nombre=="":
            self.errorMessageDialog=QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe ingresar nombre del grupo")
        else:
	    #llama al metodo que crea el grupo    
            resultado = controller.crear(nombre)
            msgBox = QtGui.QMessageBox()
            msgBox.setText("El Grupo fue creado.")
            msgBox.exec_()
            self.reject()


    def set_listeners(self):#Acciones de botones
        self.ui.button1.clicked.connect(self.agregar_grupo)
        self.ui.button2.clicked.connect(self.cancel)

	
    def cancel(self):
        self.reject()
