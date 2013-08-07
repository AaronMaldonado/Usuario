#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import hashlib
import controller
from PySide import QtGui, QtCore
from VentanaUsuarios import Ui_Ventana
from IngresoEdicion import Ui_Ventana_editar

class Ventana2(QtGui.QDialog):
	
    def __init__(self,parent=None,username=None):
	QtGui.QDialog.__init__(self,parent)
	self.ui=Ui_Ventana_editar()
	self.ui.setupUi(self)
	self.load_grupos()
	self.show()
	self.set_listeners()
	self.username=username
	temp=controller.obtener_username(username)#obtengo los datos de un usuario
	for i in temp:
            #agrego los campos obtenidos en la grilla y los agrego a la ventana edicion
	    self.ui.search_box1.setText(temp[1])#username
	    password=str(temp[2])#password
	    self.ui.search_box2.setText(password)
	    password2=str(temp[2])#repite password
	    self.ui.search_box3.setText(password2)
	    self.ui.search_box4.setText(temp[3])#nombre
	    self.ui.search_box5.setText(temp[4])#apellidos
	    self.ui.search_box6.setText(temp[5])#correo
	    fecha_nacimiento=str(temp[6])#fecha nacimiento
	    self.ui.search_box7.setText(fecha_nacimiento)


    def load_grupos(self):#Carga los grupos en un combobox
	grupos = controller.get_grupos()
	for grupo in grupos:
	    self.ui.combo_grupos.addItem(grupo["nombre"], grupo["id_grupo"])


    def editar_usuario(self):#metodo incompleto
	anterior=self.username
	#campos nuevos que se ingresaran 
        id_grupo= self.ui.combo_grupos.itemData(self.ui.combo_grupos.currentIndex())
        username = self.ui.search_box1.text()
        password = self.ui.search_box2.text()
	password2 = self.ui.search_box3.text()
	nombres = self.ui.search_box4.text()
	apellidos = self.ui.search_box5.text()
	email = self.ui.search_box6.text()
	fecha_nacimiento = self.ui.search_box7.text()
	clave=hashlib.sha512(password).hexdigest()#Transforma password a algoritmo SHA512
	clave2=hashlib.sha512(password2).hexdigest()
	resultado = controller.editar(username,clave,nombres,apellidos,email,\
	fecha_nacimiento,id_grupo)
        if resultado:
            self.reject()#sale de la ventana al momento de editar
        else:
	    self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Los datos fueron mal \
            ingresados")


    def set_listeners(self):#Acciones de botones editar y salir
	self.ui.button1.clicked.connect(self.editar_usuario)
	self.ui.button2.clicked.connect(self.cancel)

		
    def cancel(self):#Accion boton salir 
	self.reject()
