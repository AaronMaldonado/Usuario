#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import controller
from PySide import QtGui, QtCore
from VentanaUsuarios import Ui_Ventana
from IngresoEdicion import Ui_Ventana_editar

class Ventana2(QtGui.QDialog):
	
    def __init__(self,parent=None):
	QtGui.QDialog.__init__(self,parent)
	self.ui=Ui_Ventana_editar()
	
	self.ui.setupUi(self)
	self.show()
	self.set_listeners()
		
		
    def load_grupos(self):#Carga los grupos en un combobox
	grupos = controller.get_grupos()
	for grupo in grupos:
	    self.ui.combo_grupos.addItem(grupo["nombre"], grupo["id_grupo"])


    def editar_usuario(self):#metodo incompleto 
	model=self.ui.table_usuarios.model()
	index=self.ui.table_usuarios.currentIndex()	
	if index.row()== -1:# No se ha seleccionado fila
	    self.errorMessageDialog = QtGui.QErrorMessage(self)
	    self.errorMessageDialog.showMessage("Debe seleccionar una fila")
	    return False
		

    def set_listeners(self):#Acciones de botones editar y salir
	self.ui.button1.clicked.connect(self.editar_usuario)
	self.ui.button2.clicked.connect(self.cancel)

		
    def cancel(self):#Accion boton salir 
	self.reject()
