#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import VentanaAgregar
import controller
import VentanaEdicion
import CreacionGrupo
import VentanaEliminarGrupo
from PySide import QtGui, QtCore
from VentanaUsuarios import Ui_Ventana

class Usuarios(QtGui.QWidget):

    def __init__(self):
        super(Usuarios, self).__init__()
        self.ui =  Ui_Ventana()
        self.ui.setupUi(self)
        self.load_usuarios()
        self.show()
        self.set_signals()
        
        
    #Carga usuarios en la grilla
    def load_usuarios(self, usuarios=None):
        if usuarios is None:
            usuarios = controller.get_usuarios()
            busqueda = QtGui.QCompleter(map(lambda c: c["username"], usuarios), self) 
            busqueda.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            self.ui.search_box.setCompleter(busqueda)				
        self.model = QtGui.QStandardItemModel(len(usuarios), 6)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"grupo"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Username"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Nombre"))			
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Apellidos"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Email"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Fecha Nacimiento"))
        r = 0
        for row in usuarios:
            index = self.model.index(r, 0, QtCore.QModelIndex()); 
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 1, QtCore.QModelIndex()); 
            self.model.setData(index, row['Username'])
            index = self.model.index(r, 2, QtCore.QModelIndex()); 
            self.model.setData(index, row['Nombres'])
            index = self.model.index(r, 3, QtCore.QModelIndex()); 
            self.model.setData(index, row['Apellidos'])
            index = self.model.index(r, 4, QtCore.QModelIndex()); 
            self.model.setData(index, row['Email'])
	    index = self.model.index(r, 5, QtCore.QModelIndex()); 
            self.model.setData(index, row['fecha_nacimiento'])
            
            r = r+1

        self.ui.table_usuarios.setModel(self.model)
        self.ui.table_usuarios.setColumnWidth(0, 80)
        self.ui.table_usuarios.setColumnWidth(1, 150)
        self.ui.table_usuarios.setColumnWidth(2, 150)
        self.ui.table_usuarios.setColumnWidth(3, 150)
        self.ui.table_usuarios.setColumnWidth(4, 170)
        self.ui.table_usuarios.setColumnWidth(5, 150)
	
	
    def set_signals(self):#Acciones de Botones
		self.ui.btn_search.clicked.connect(self.delete)
		self.ui.btn_search2.clicked.connect(self.formulario)
		self.ui.btn_search3.clicked.connect(self.formulario2)  
		self.ui.btn_search4.clicked.connect(self.formulario3)
		#self.ui.btn_search5.clicked.connect(self.formulario4)
		self.ui.btn_search6.clicked.connect(self.formulario5)
		self.ui.btn_search7.clicked.connect(self.buscar_usuario)
	
    def formulario(self):#Accion boton Editar
		model=self.ui.table_usuarios.model()
		index=self.ui.table_usuarios.currentIndex()	
		if index.row()== -1:# No se ha seleccionado fila
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage("Debe seleccionar una fila")
			return False
		else:
			formu2=VentanaEdicion.Ventana2(self)
		
		
    def formulario2(self):#Accion boton Agregar
		formu=VentanaAgregar.Ventana(self)
	
	
    def formulario3(self):
		formu3=CreacionGrupo.Ventana_grupos(self)
		
		
    def formulario5(self):
		formu4=VentanaEliminarGrupo.Ventana_eliminar(self)
		
    def buscar_usuario(self):
        user = self.ui.search_box.text()
        usuarios = controller.buscar_usuario(user)
        self.load_usuarios(usuarios)
        
        		
    def delete(self):#elimina usuarios
		model=self.ui.table_usuarios.model()
		index=self.ui.table_usuarios.currentIndex()
		
		if index.row()==-1:# No se ha seleccionado fila
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage("Debe seleccionar una fila")
			return False
			
		else:
			codigo=model.index(index.row(),1,QtCore.QModelIndex()).data()		
			if(controller.delete(codigo)):#llama a metodo delete 
				self.load_usuarios()#Carga en la grilla el nuevo usuario
				msgBox = QtGui.QMessageBox()
				msgBox.setText("El Usuario fue eliminado.")
				msgBox.exec_()
				return True
#123456789111111111122222222223333333333444444444455555555556666666666777777777					
			else:
				self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
				self.ui.errorMessageDialog.showMessage("Error al eliminar el registro")
				return False
    
					
def run():
    app = QtGui.QApplication(sys.argv)
    main = Usuarios()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
