#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import hashlib
import controller
from PySide import QtGui, QtCore
from Ingreso import Ui_Ventana

class Ventana(QtGui.QDialog):
	
    def __init__(self,parent=None):
	QtGui.QDialog.__init__(self,parent)
	self.ui=Ui_Ventana()
	self.ui.setupUi(self)
	self.load_grupos()
	self.show()
	self.set_listeners()
		
		
    def load_grupos(self):#cargar los grupos
	grupos = controller.get_grupos()
	for grupo in grupos:
	    self.ui.combo_grupos.addItem(grupo["nombre"], grupo["id_grupo"])	
	
	
    def agregar_usuario(self):#agrega usuarios a la grilla
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
        if clave==clave2 or (clave=="" and clave2==""):#compara contraseñas
            #Verifica que los campos obligatorios estes rellenos
	    if (username and nombres and apellidos and email)=="":
	        self.errorMessageDialog=QtGui.QErrorMessage(self)
		self.errorMessageDialog.showMessage("Debe Ingresar Username-Nombres-Apellidos-Email ")
				
	    else:
		#crea el nuevo usuario llamando al metodo agregar
		resultado = controller.agregar(username,clave,nombres,apellidos,email,fecha_nacimiento,id_grupo)
		self.errorMessageDialog=QtGui.QErrorMessage(self)
		self.errorMessageDialog.showMessage("Se a creado correctamente el Usuario")
		self.reject()
	else:
	    self.errorMessageDialog=QtGui.QErrorMessage(self)
	    self.errorMessageDialog.showMessage("Password incorrectas vuelva a intentarlo :)")
	
	
    def set_listeners(self):#Acciones de botones
	self.ui.button1.clicked.connect(self.agregar_usuario)
	self.ui.button2.clicked.connect(self.cancel)

	
    def cancel(self):
	self.reject()
