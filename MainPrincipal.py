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

class MainPrincipal(QtGui.QWidget):

    def __init__(self):
        super(MainPrincipal, self).__init__()
        self.ui =  Ui_Ventana()
        self.ui.setupUi(self)
        self.load_usuarios()
        self.show()
        self.set_signals()
        
        
    #Carga usuarios en la grilla
    def load_usuarios(self, usuarios=None):
        if usuarios is None:
            usuarios = controller.get_usuarios()
            #Completa busqueda 
            busqueda = QtGui.QCompleter(map(lambda c: c["username"],\
                       usuarios), self) 
            busqueda.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            self.ui.search_box.setCompleter(busqueda)	
        #Creamos nuestra grilla			
        self.model = QtGui.QStandardItemModel(len(usuarios), 8)
        self.model.setHorizontalHeaderItem(0,QtGui.QStandardItem(u"grupo"))
        self.model.setHorizontalHeaderItem(1,QtGui.QStandardItem \
        (u"id_usuario"))
        self.model.setHorizontalHeaderItem(2,QtGui.QStandardItem(u"Username"))
        self.model.setHorizontalHeaderItem(3,QtGui.QStandardItem(u"Password"))
        self.model.setHorizontalHeaderItem(4,QtGui.QStandardItem(u"Nombre"))			
        self.model.setHorizontalHeaderItem(5,QtGui.QStandardItem(u"Apellidos"))
        self.model.setHorizontalHeaderItem(6,QtGui.QStandardItem(u"Email"))
        self.model.setHorizontalHeaderItem(7,QtGui.QStandardItem \
        (u"Fecha Nacimiento"))
        r = 0

        for row in usuarios:#le agregamos los elementos 
            index = self.model.index(r, 0, QtCore.QModelIndex()); 
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 1, QtCore.QModelIndex()); 
            self.model.setData(index, row['id_usuario'])
            index = self.model.index(r, 2, QtCore.QModelIndex()); 
            self.model.setData(index, row['Username'])
            index = self.model.index(r, 3, QtCore.QModelIndex()); 
            self.model.setData(index, row['Password'])
            index = self.model.index(r, 4, QtCore.QModelIndex()); 
            self.model.setData(index, row['Nombres'])
            index = self.model.index(r, 5, QtCore.QModelIndex()); 
            self.model.setData(index, row['Apellidos'])
            index = self.model.index(r, 6, QtCore.QModelIndex()); 
            self.model.setData(index, row['Email'])
	    index = self.model.index(r, 7, QtCore.QModelIndex()); 
            self.model.setData(index, row['fecha_nacimiento'])
            
            r = r+1
	#creamos las dimenciones de las columnas de la grilla
        self.ui.table_usuarios.setModel(self.model)
        self.ui.table_usuarios.setColumnWidth(0, 110)
        self.ui.table_usuarios.hideColumn(1)
        self.ui.table_usuarios.setColumnWidth(2, 150)
        self.ui.table_usuarios.hideColumn(3)
        self.ui.table_usuarios.setColumnWidth(4, 150)
        self.ui.table_usuarios.setColumnWidth(5, 150)
        self.ui.table_usuarios.setColumnWidth(6, 170)
        self.ui.table_usuarios.setColumnWidth(7, 170)
	
	
    def set_signals(self):#Acciones de Botones
	self.ui.btn_search.clicked.connect(self.delete)#boton eliminar usuario
	self.ui.btn_search2.clicked.connect(self.editar)#boton editar usuario
	self.ui.btn_search3.clicked.connect(self.formulario2)#Boton crear usuario  
	self.ui.btn_search4.clicked.connect(self.formulario3)#boton crear grupo
	#self.ui.btn_search5.clicked.connect(self.formulario4)#boton Editar grupo
	self.ui.btn_search6.clicked.connect(self.formulario5)#boton eliminar grupo
	self.ui.btn_search7.clicked.connect(self.buscar_usuario)#boton buscar
		
		
    def formulario2(self):#Acción botón Agregar
	formu=VentanaAgregar.Ventana(self)
	
	
    def formulario3(self):#Acción botón Crear Grupo
	formu3=CreacionGrupo.Ventana_grupos(self)
		
		
    def formulario5(self):#Acción botón eliminar grupo
	formu4=VentanaEliminarGrupo.Ventana_eliminar(self)
		

    def buscar_usuario(self):#buscar los usuarios 
        user = self.ui.search_box.text()
        usuarios = controller.buscar_usuario(user)
        self.load_usuarios(usuarios)
        
        		
    def editar(self):
        model = self.ui.table_usuarios.model()
        index = self.ui.table_usuarios.currentIndex()
        if index.row() == 0: #No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False

        else:
            codigo =str(model.index(index.row(), 1, \
            QtCore.QModelIndex()).data())

            formu2 = VentanaEdicion.Ventana2(self,codigo)
            formu2.exec_()


    def delete(self):#elimina usuarios
        model=self.ui.table_usuarios.model()
        index=self.ui.table_usuarios.currentIndex()
		
        if index.row()==0:# No se ha seleccionado fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
			
        else:
            codigo=model.index(index.row(),1,QtCore.QModelIndex()).data()		
            if(controller.delete(codigo)):#llama a metodo y elimina
                self.load_usuarios()#Carga en la grilla el nuevo usuario
                msgBox = QtGui.QMessageBox()
                msgBox.setText("El Usuario fue eliminado.")
                msgBox.exec_()
                return True
				
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage("Error al eliminar \
                el registro")
                return False
		
			
def run():
    app = QtGui.QApplication(sys.argv)
    main = MainPrincipal()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
