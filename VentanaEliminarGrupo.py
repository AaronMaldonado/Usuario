#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import controller
from EliminarGrupo import Ui_Ventana_Eliminar_Grupo

class Ventana_eliminar(QtGui.QDialog):
	
    def __init__(self,parent=None):
	QtGui.QDialog.__init__(self,parent)
	self.ui=Ui_Ventana_Eliminar_Grupo()
	self.ui.setupUi(self)
	self.load_grupos()
	self.show()
	self.set_listeners()
    #Carga grupos en la grilla
    def load_grupos(self, grupos=None):
        if grupos is None:
            grupos = controller.get_grupos()				
        self.model = QtGui.QStandardItemModel(len(grupos), 1)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"nombre"))
        r = 0
        for row in grupos:
            index = self.model.index(r, 0, QtCore.QModelIndex()); 
            self.model.setData(index, row['nombre'])

            r = r+1

        self.ui.table_grupos.setModel(self.model)
        self.ui.table_grupos.setColumnWidth(0,150)


    def delete(self):#elimina usuarios
	model=self.ui.table_grupos.model()
	index=self.ui.table_grupos.currentIndex()
		
	if index.row()==-1:# No se ha seleccionado fila
		self.errorMessageDialog = QtGui.QErrorMessage(self)
		self.errorMessageDialog.showMessage("Debe seleccionar una fila")
		return False
			
	else:
		codigo=model.index(index.row(),0,QtCore.QModelIndex()).data()		
		if(controller.delete_grupo(codigo)):#llama a metodo delete_grupo 
			self.load_grupos()#Carga en la grilla el nuevo usuario
			msgBox = QtGui.QMessageBox()
			msgBox.setText("El Grupo fue eliminado.")
			msgBox.exec_()
			return True
#123456789111111111122222222223333333333444444444455555555556666666666777777777					
		else:
			self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
			self.ui.errorMessageDialog.showMessage("Error al eliminar el registro")
			return False
	
	
    def set_listeners(self):#Acciones de botones
	self.ui.button1.clicked.connect(self.delete)
	self.ui.button2.clicked.connect(self.cancel)

	
    def cancel(self):
	self.reject()
