#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import hashlib
import controller
from PySide import QtGui, QtCore
from VentanaUsuarios import Ui_Ventana
from IngresoEdicion import Ui_Ventana_editar

class Ventana2(QtGui.QDialog):
	
    def __init__(self,parent=None):
	QtGui.QDialog.__init__(self,parent)
	self.ui=Ui_Ventana_editar()
	self.ui.setupUi(self)
	self.load_grupos()
	self.show()
	self.set_listeners()
		
		
    def load_grupos(self):#Carga los grupos en un combobox
	grupos = controller.get_grupos()
	for grupo in grupos:
	    self.ui.combo_grupos.addItem(grupo["nombre"], grupo["id_grupo"])


    def editar_usuario(self):#metodo incompleto 
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
	resultado = controller.editar(username,clave,nombres,apellidos,email,fecha_nacimiento,id_grupo)
        if resultado:
            self.reject()#sale de la ventana al momento de editar
        else:
            self.ui.message.setText("Los datos fueron mal ingresados")


    def set_listeners(self):#Acciones de botones editar y salir
	self.ui.button1.clicked.connect(self.editar_usuario)
	self.ui.button2.clicked.connect(self.cancel)

		
    def cancel(self):#Accion boton salir 
	self.reject()
