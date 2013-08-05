#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import controller
from CreaGrupo import Ui_Ventana_grupo

class Ventana_grupos(QtGui.QDialog):
	
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Ventana_grupo()
		self.ui.setupUi(self)
		#self.load_grupos()
		self.show()
		self.set_listeners()
		
		
	def agregar_grupo(self):#agrega usuarios a la grilla
		nombre = self.ui.search_box.text()
		resultado = controller.crear(nombre)
		msgBox = QtGui.QMessageBox()
		msgBox.setText("El Grupo fue creado.")
        	msgBox.exec_()
	def set_listeners(self):#Acciones de botones
		self.ui.button1.clicked.connect(self.agregar_grupo)
		self.ui.button2.clicked.connect(self.cancel)

	
	def cancel(self):
		self.reject()
