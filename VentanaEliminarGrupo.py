#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import controller
from PySide import QtGui, QtCore
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
        #se crea la grilla			
        self.model = QtGui.QStandardItemModel(len(grupos), 2)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"id_grupo"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"nombre"))
        r = 0
        for row in grupos:#agrega los grupos a la grilla
	    index = self.model.index(r, 0, QtCore.QModelIndex()); 
            self.model.setData(index, row['id_grupo'])
            index = self.model.index(r, 1, QtCore.QModelIndex()); 
            self.model.setData(index, row['nombre'])

            r = r+1

        self.ui.table_grupos.setModel(self.model)
        self.ui.table_grupos.hideColumn(0)
        self.ui.table_grupos.setColumnWidth(1,150)


    def delete(self):#elimina usuarios
        model=self.ui.table_grupos.model()
        index=self.ui.table_grupos.currentIndex()
		
	if index.row()==-1:# No se ha seleccionado fila
	    self.errorMessageDialog = QtGui.QErrorMessage(self)
	    self.errorMessageDialog.showMessage("Debe seleccionar una fila")
	    return False
			
	else:
            codigo=model.index(index.row(),1,QtCore.QModelIndex()).data()		
            if(controller.delete_grupo(codigo)):#llama a metodo delete_grupo 
	        self.load_grupos()#Carga en la grilla el nuevo usuario
		msgBox = QtGui.QMessageBox()
		msgBox.setText("El Grupo fue eliminado.")
		msgBox.exec_()
                self.reject()
		return True
					
	    else:
		self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
		self.ui.errorMessageDialog.showMessage("Error al eliminar el registro")
		return False
	
	
    def set_listeners(self):#Acciones de botones
        self.ui.button1.clicked.connect(self.delete)
        self.ui.button2.clicked.connect(self.cancel)

	
    def cancel(self):
        self.reject()
